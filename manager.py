import asyncio, base64, contextlib, hmac, json, os, time
import aiohttp
from aiohttp import web

import bot  # your original bot.py (only main() signature changed)

TARGET_LEVEL   = int(os.environ.get("TARGET_LEVEL", 31))
CHECK_INTERVAL = int(os.environ.get("CHECK_INTERVAL", 60))       # running account: every 1 minute
REFRESH_INTERVAL = int(os.environ.get("REFRESH_INTERVAL", 300))  # other accounts (web details): every 5 minutes
API_URL        = os.environ.get("LEVEL_API", "http://s1.skynode.online:2003/ban-check?uid={}")
RELOGIN_AFTER  = 6 * 60 * 60                                      # same 6h restart as before
MAX_FAILS      = 3
ACCOUNTS_FILE  = os.environ.get("ACCOUNTS_FILE", "accounts.json")
STATE_FILE     = os.environ.get("STATE_FILE", "state.json")
PORT           = int(os.environ.get("PORT", 8080))
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "@Basanta6677")

accounts = []      # [{uid, password, account_id, name}]
rt = {}            # uid -> runtime info (status, level, info, last_check, error, fails)
current_uid = None
session = None


def log(*a):
    print("[MANAGER]", *a, flush=True)


# ---------------------------------------------------------------- storage
def norm(a):
    if not isinstance(a, dict):
        return None
    uid = str(a.get("uid", "")).strip()
    pw = str(a.get("password", "")).strip()
    if not uid or not pw:
        return None
    return {"uid": uid, "password": pw,
            "account_id": str(a.get("account_id") or "").strip(),
            "name": str(a.get("name") or uid).strip()}


def parse_accounts(raw):
    if isinstance(raw, dict):
        raw = raw.get("accounts", [raw])
    return [x for x in (norm(a) for a in raw) if x] if isinstance(raw, list) else []


def new_rt():
    return {"status": "pending", "level": None, "info": None,
            "last_check": None, "error": "", "fails": 0}


def save_accounts():
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=2, ensure_ascii=False)


def save_state():
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(rt, f, ensure_ascii=False)
    except Exception as e:
        log("state save error:", e)


def load_all():
    global accounts
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as f:
            accounts = parse_accounts(json.load(f))
    saved = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                saved = json.load(f)
        except Exception:
            pass
    for a in accounts:
        r = new_rt()
        r.update(saved.get(a["uid"], {}))
        if r["status"] in ("running", "checking"):
            r["status"] = "pending"
        rt[a["uid"]] = r
    log(f"{len(accounts)} accounts loaded")


# ---------------------------------------------------------------- level API
async def do_check(acc):
    """Returns 'done' | 'banned' | 'ok' | 'error'."""
    r = rt[acc["uid"]]
    aid = acc["account_id"] or (str(bot.account_id) if bot.account_id and acc["uid"] == current_uid else "")
    try:
        if not aid:
            raise RuntimeError("account_id missing")
        async with session.get(API_URL.format(aid), timeout=aiohttp.ClientTimeout(total=20)) as resp:
            data = await resp.json(content_type=None)
        ban = str(data.get("Ban Info", {}).get("Status", "")).upper()
        is_banned = "BANNED" in ban and "NOT" not in ban
        try:
            level = int(data["Account Info"]["Level"])
        except Exception:
            if not is_banned:
                raise
            level = (rt[acc["uid"]]["level"] or 0)
    except Exception as e:
        r["error"] = f"level check failed: {e}"
        r["last_check"] = time.time()
        save_state()
        return "error"

    r.update(level=level, info=data, last_check=time.time(), error="")
    save_state()
    log(f"{acc['name']} ({acc['uid']}) level {level}/{TARGET_LEVEL}")

    if is_banned:
        log(f"{acc['name']} ({acc['uid']}) BANNED: {ban}")
        return "banned"
    return "done" if level >= TARGET_LEVEL else "ok"


refresh_lock = asyncio.Lock()


async def refresh_all():
    """Fetch API details for every account (not only the running one)."""
    if refresh_lock.locked():
        return
    async with refresh_lock:
        sem = asyncio.Semaphore(10)

        async def one(acc):
            if acc["uid"] == current_uid:   # running account is checked by its own loop
                return
            async with sem:
                verdict = await do_check(acc)
            r = rt[acc["uid"]]
            if r["status"] == "pending" and verdict in ("done", "banned"):
                r["status"] = verdict
                save_state()

        await asyncio.gather(*(one(a) for a in list(accounts)), return_exceptions=True)
        log("all accounts refreshed")


async def refresh_loop():
    while True:
        try:
            await refresh_all()
        except Exception as e:
            log("refresh error:", e)
        await asyncio.sleep(REFRESH_INTERVAL)


async def stop_bot(task):
    if not task.done():
        task.cancel()
    with contextlib.suppress(asyncio.CancelledError, Exception):
        await task
    w = bot.online_writer
    if w is not None:
        with contextlib.suppress(Exception):
            w.close()
    bot.online_writer = None


# ---------------------------------------------------------------- runner
async def run_account(acc):
    global current_uid
    r = rt[acc["uid"]]
    current_uid = acc["uid"]
    try:
        r["status"] = "checking"
        verdict = await do_check(acc)
        if verdict in ("done", "banned"):
            r["status"] = verdict
            save_state()
            return

        while True:
            r["status"] = "running"
            save_state()
            log(f"START {acc['name']} ({acc['uid']})")
            task = asyncio.create_task(bot.main(int(acc["uid"]), acc["password"]))
            started = time.time()
            next_check = started + CHECK_INTERVAL

            while not task.done():
                now = time.time()
                if now - started >= RELOGIN_AFTER:
                    log("6h reached, re-login")
                    break
                wait = max(0.5, min(next_check, started + RELOGIN_AFTER) - now)
                await asyncio.wait({task}, timeout=wait)
                if task.done():
                    break
                if time.time() >= next_check:
                    next_check = time.time() + CHECK_INTERVAL
                    verdict = await do_check(acc)
                    if verdict in ("done", "banned"):
                        await stop_bot(task)
                        r["status"] = verdict
                        save_state()
                        log(f"{acc['name']} finished: {verdict}")
                        return

            ran_for = time.time() - started
            crashed = task.done()
            await stop_bot(task)
            if crashed:  # main() returned/raised on its own = login or runtime failure
                r["fails"] = 0 if ran_for > 600 else r["fails"] + 1
                r["error"] = f"bot stopped after {int(ran_for)}s (attempt {r['fails']}/{MAX_FAILS})"
                if r["fails"] >= MAX_FAILS:
                    r["status"] = "failed"
                    save_state()
                    return
                await asyncio.sleep(15)
    finally:
        current_uid = None
        if r["status"] in ("running", "checking"):
            r["status"] = "pending"
        save_state()


async def worker():
    while True:
        try:
            acc = next((a for a in accounts if rt[a["uid"]]["status"] == "pending"), None)
            if acc is None:
                await asyncio.sleep(5)
                continue
            await run_account(acc)
        except asyncio.CancelledError:
            raise
        except Exception as e:
            log("worker error:", e)
            await asyncio.sleep(5)


# ---------------------------------------------------------------- web
@web.middleware
async def auth(request, handler):
    if ADMIN_PASSWORD:
        ok = False
        h = request.headers.get("Authorization", "")
        if h.startswith("Basic "):
            try:
                pw = base64.b64decode(h[6:]).decode().split(":", 1)[1]
                ok = hmac.compare_digest(pw, ADMIN_PASSWORD)
            except Exception:
                pass
        if not ok:
            return web.Response(status=401, text="Login required",
                                headers={"WWW-Authenticate": 'Basic realm="bot"'})
    return await handler(request)


async def api_state(request):
    counts = {"total": len(accounts)}
    out = []
    for a in accounts:
        r = rt[a["uid"]]
        counts[r["status"]] = counts.get(r["status"], 0) + 1
        out.append({"uid": a["uid"], "account_id": a["account_id"], "name": a["name"],
                    "current": a["uid"] == current_uid, **r})
    return web.json_response({"target": TARGET_LEVEL, "interval": CHECK_INTERVAL,
                              "counts": counts, "accounts": out, "now": time.time()})


async def api_upload(request):
    raw = None
    async for part in await request.multipart():
        if part.name == "file":
            raw = await part.read(decode=False)
    if not raw:
        return web.json_response({"error": "no file"}, status=400)
    try:
        new = parse_accounts(json.loads(raw.decode("utf-8-sig")))
    except Exception as e:
        return web.json_response({"error": f"invalid json: {e}"}, status=400)
    if not new:
        return web.json_response({"error": "no valid accounts (need uid + password)"}, status=400)

    index = {a["uid"]: a for a in accounts}
    added = updated = 0
    for n in new:
        if n["uid"] in index:
            index[n["uid"]].update(n)
            updated += 1
        else:
            accounts.append(n)
            rt[n["uid"]] = new_rt()
            index[n["uid"]] = n
            added += 1
    save_accounts()
    save_state()
    log(f"upload: +{added} new, {updated} updated")
    asyncio.create_task(refresh_all())
    return web.json_response({"added": added, "updated": updated, "total": len(accounts)})


async def api_refresh(request):
    asyncio.create_task(refresh_all())
    return web.json_response({"started": True})


async def api_retry(request):
    n = 0
    for a in accounts:
        r = rt[a["uid"]]
        if r["status"] == "failed":
            r.update(status="pending", fails=0, error="")
            n += 1
    save_state()
    return web.json_response({"retried": n})


PAGE = r"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Level Bot</title>
<style>
:root{--bg:#0f1115;--card:#181b22;--line:#2a2f3a;--tx:#e6e8ec;--mu:#8b93a3;--ok:#3ecf8e;--run:#4da3ff;--bad:#ff6b6b;--warn:#f5b942}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:14px system-ui,sans-serif;padding:12px}
h1{font-size:18px;margin:0 0 10px}
.bar{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:10px}
.chip{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:6px 10px;cursor:pointer}
.chip.on{border-color:var(--run)}.chip b{margin-left:4px}
.box{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;margin-bottom:10px}
input[type=search]{width:100%;padding:9px;border-radius:8px;border:1px solid var(--line);background:var(--card);color:var(--tx);margin-bottom:10px}
button{background:var(--run);color:#fff;border:0;border-radius:8px;padding:8px 12px;font-size:14px}
button.sec{background:#2a2f3a}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px;margin-bottom:10px}
.card.current{border-color:var(--run);box-shadow:0 0 0 1px var(--run)}
.row{display:flex;justify-content:space-between;align-items:center;gap:8px}
.name{font-weight:600}.mu{color:var(--mu);font-size:12px}
.badge{font-size:11px;padding:2px 8px;border-radius:99px;border:1px solid var(--line)}
.running{color:var(--run);border-color:var(--run)}.done{color:var(--ok);border-color:var(--ok)}
.failed,.banned{color:var(--bad);border-color:var(--bad)}.checking{color:var(--warn);border-color:var(--warn)}
.prog{height:6px;background:#2a2f3a;border-radius:9px;overflow:hidden;margin:8px 0}
.prog i{display:block;height:100%;background:var(--run)}.done+.prog i,.prog.d i{background:var(--ok)}
pre{margin:6px 0 0;background:#0c0e12;border:1px solid var(--line);border-radius:8px;padding:8px;font-size:12px;white-space:pre-wrap;word-break:break-word}
.err{color:var(--bad);font-size:12px;margin-top:4px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:8px}
.grid div{background:#0c0e12;border:1px solid var(--line);border-radius:8px;padding:6px 8px;word-break:break-word}
.grid span{display:block;color:var(--mu);font-size:11px}.grid .wide{grid-column:1/3}
table{width:100%;border-collapse:collapse;margin-top:8px;font-size:12px}
th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);white-space:nowrap}th{color:var(--mu);font-weight:500}
.t-done{color:var(--ok)}.t-banned{color:var(--bad)}
</style></head><body>
<h1>Level Bot Dashboard</h1>
<div class="bar" id="chips"></div>
<div class="box"><div class="row"><b>Add accounts</b><span class="mu" id="upmsg"></span></div>
<div style="margin-top:8px;display:flex;gap:8px;flex-wrap:wrap">
<input type="file" id="file" accept=".json,application/json">
<button onclick="upload()">Upload accounts.json</button>
<button class="sec" onclick="retry()">Retry failed</button>
<button class="sec" onclick="refreshAll()">Refresh all API</button></div></div>
<div id="summary"></div>
<input type="search" id="q" placeholder="Search name / uid / account_id" oninput="render()">
<div id="list"></div>
<script>
let S=null,F="all";
const esc=s=>String(s??"").replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
const ago=t=>{if(!t)return"never";const s=Math.floor(Date.now()/1000-t);return s<60?s+"s ago":s<3600?Math.floor(s/60)+"m ago":Math.floor(s/3600)+"h ago"};
async function load(){try{S=await (await fetch("/api/state")).json();render()}catch(e){}}
const info=a=>(a.info&&a.info["Account Info"])||{};
const banSt=a=>(a.info&&a.info["Ban Info"]&&a.info["Ban Info"].Status)||"-";
const fmt=v=>v===undefined||v===null?"-":(typeof v==="number"?v.toLocaleString():v);
const label=a=>({done:"✅ Level "+S.target+" Complete",banned:"🚫 Banned",running:"▶ Running",pending:"⏳ Pending",checking:"🔎 Checking",failed:"⚠ Login failed"}[a.status]||a.status);
function fields(a){const i=info(a);return `<div class="grid"><div><span>Nickname</span>${esc(fmt(i.Nickname))}</div><div><span>Level</span>${esc(fmt(i.Level))}</div><div><span>Region</span>${esc(fmt(i.Region))}</div><div><span>Likes</span>${esc(fmt(i.Likes))}</div><div class="wide"><span>Status</span>${label(a)}${a.status=="banned"?" · "+esc(banSt(a)):""}</div></div>`}
function table(title,cls,arr){if(!arr.length)return"";
 const rows=arr.map(a=>{const i=info(a);return `<tr><td>${esc(fmt(i.Nickname))}</td><td>${esc(fmt(i.Level))}</td><td>${esc(fmt(i.Region))}</td><td>${esc(fmt(i.Likes))}</td><td>${a.status=="banned"?esc(banSt(a)):"Level "+S.target+" Complete"}</td></tr>`}).join("");
 return `<div class="box"><b class="${cls}">${title} (${arr.length})</b><div style="overflow-x:auto"><table><tr><th>Nickname</th><th>Level</th><th>Region</th><th>Likes</th><th>Status</th></tr>${rows}</table></div></div>`}
function render(){
 if(!S)return;const c=S.counts,q=document.getElementById("q").value.toLowerCase();
 const tabs=[["all","All",c.total],["running","Running",c.running||0],["pending","Pending",c.pending||0],["done","Done",c.done||0],["banned","Banned",c.banned||0],["failed","Failed",c.failed||0]];
 document.getElementById("chips").innerHTML=tabs.map(t=>`<div class="chip ${F==t[0]?"on":""}" onclick="F='${t[0]}';render()">${t[1]}<b>${t[2]}</b></div>`).join("");
 document.getElementById("summary").innerHTML=table("✅ Level "+S.target+" Complete","t-done",S.accounts.filter(a=>a.status=="done"))+table("🚫 Banned","t-banned",S.accounts.filter(a=>a.status=="banned"));
 let list=S.accounts.filter(a=>F=="all"||a.status==F);
 if(q)list=list.filter(a=>(a.name+a.uid+a.account_id+(info(a).Nickname||"")).toLowerCase().includes(q));
 list.sort((a,b)=>(b.current-a.current));
 document.getElementById("list").innerHTML=list.map(a=>{
  const lv=a.level??0,pct=Math.min(100,lv/S.target*100);
  return `<div class="card ${a.current?"current":""}"><div class="row"><div><div class="name">${esc(a.name)}</div>
  <div class="mu">uid ${esc(a.uid)} · id ${esc(a.account_id)}</div></div><span class="badge ${a.status}">${a.status}</span></div>
  ${fields(a)}
  <div class="mu" style="margin-top:8px">Level ${a.level??"?"} / ${S.target} · checked ${ago(a.last_check)}</div>
  <div class="prog ${a.status=="done"?"d":""}"><i style="width:${pct}%"></i></div>
  ${a.error?`<div class="err">${esc(a.error)}</div>`:""}
  ${a.info?"":'<div class="mu">No data yet</div>'}</div>`}).join("")||'<div class="mu">No accounts</div>';
}
async function upload(){const f=document.getElementById("file").files[0],m=document.getElementById("upmsg");
 if(!f){m.textContent="Choose a file first";return}
 const fd=new FormData();fd.append("file",f);
 const r=await fetch("/api/upload",{method:"POST",body:fd}),j=await r.json();
 m.textContent=r.ok?`+${j.added} new, ${j.updated} updated (total ${j.total})`:(j.error||"error");load()}
async function retry(){const j=await (await fetch("/api/retry",{method:"POST"})).json();
 document.getElementById("upmsg").textContent=`${j.retried} account(s) re-queued`;load()}
async function refreshAll(){await fetch("/api/refresh",{method:"POST"});
 document.getElementById("upmsg").textContent="Refreshing all accounts...";setTimeout(load,4000)}
load();setInterval(load,5000);
</script></body></html>"""


async def index(request):
    return web.Response(text=PAGE, content_type="text/html")


# ---------------------------------------------------------------- main
async def main():
    global session
    load_all()
    session = aiohttp.ClientSession()

    app = web.Application(middlewares=[auth], client_max_size=20 * 1024 * 1024)
    app.add_routes([web.get("/", index), web.get("/api/state", api_state),
                    web.post("/api/upload", api_upload), web.post("/api/retry", api_retry),
                    web.post("/api/refresh", api_refresh)])
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, "0.0.0.0", PORT).start()
    log(f"web on port {PORT}" + (" (password protected)" if ADMIN_PASSWORD else " (NO PASSWORD)"))

    refresher = asyncio.create_task(refresh_loop())
    try:
        await worker()
    finally:
        refresher.cancel()
        await session.close()
        await runner.cleanup()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log("stopped")
