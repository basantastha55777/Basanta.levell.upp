import json, struct, ast, asyncio, aiohttp, urllib3, time, os, sys, ssl, uuid, random, socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from datetime import datetime
from colorama import Fore, Style
from message_ids import MESSAGE_ID_TO_NAME

urllib3.disable_warnings()

version_url = 'https://version.common.redflamenco.com'
aes_key = bytes.fromhex("5967267463254445756836255a635e38")
aes_iv  = bytes.fromhex("366f795a4472323245337963686a4d25")

game_version = None
release_version = None
login_url = None
gop_url_1 = None
gop_url_2 = None
vercfg_sign = None
field_106 = None
access_token = None
open_id = None
platform = None
account_id = None
region = None
jwt_token = None
server_url = None
timestamp = None
key = None
iv = None
stronghold_raw = None

online_writer = None


def start_solo_triple_wolves(game_version, region, key, iv):
    fields = {
        "1": 1,
        "2": {
            "1": '"',
            "2": 73,
            "7": [
                {
                    "1": "IDC1",
                    "2": 200,
                    "3": str(region)
                },
                {
                    "1": "IDC2",
                    "2": 760,
                    "3": str(region)
                },
                {
                    "1": "IDC3",
                    "2": 712,
                    "3": str(region)
                }
            ],
            "8": 1,
            "9": "b'\\x01\\x07\\t\\n\\x0b\\x12\\x19\\x1a \"\\')'",
            "11": 1,
            "12": {
                "1": "088B823F753E119A020101000000000D001300010005000254D34CBC0F0000004676251400000000000000000000000000000000000000ff00000000cacfa16d",
                "2": 108,
                "3": "b'\\x7fXUV\\x12\\x03\\x01E\\x04US\\x0c\\x01\\x0b\\x00R\\x05WZ\\x0f\\r\\x08\\x0c\\x04\\x0f\\x0b\\x06\\x03\\x06\\x00\\x03\\x01\\x00\\r\\x04Z\\x07U\\x01T\\x1a\\x07\\x05M|\\\\IGH\\x1a\\x01\\x15\\x07\\x1d\\x12\\x08\\x03E\\x03W|s\\nYl@c~saHDsoX}u\\x0fw\\x01fz\\x00xt\\x0b\\x17\\x00E{TaPtRtL{e~v_RutHRxU^[[XRbE\\x0c\\x1aP[_M\\x1ej{\\x1cuAI\\x07HfkfI\\x03BFTCZAf\\x12KqKF\\x0bhv~_Dk\\x1eO\\x0b\\x0c\\x11\\x00\\nJ^pM`lCUqKUlQ]\\tzmG\\x1a\\x04drBnCwv`\\x0e\\x12\\nMM\\x01d\\x1eRbk\\x1ck\\x0buJl^BRCpXH\\x19\\x7f\\x12YLBx\\x0c\\x1a\\x01Mvp[r^IASr_\\x1e\\x0bCxa\\x07|N@At[UV\\x0ecy\\x0c\\x1a\\x08E\\x04[gD_EMe{BsuVj\\x07HGxboCtk}S{l\\x0b\\x17\\x00\\x01MqI{xBn\\x06Q\\t\\x01Y\\x0b{KTwTB`h`B_bc^\\x01\\x04\\x15\\x07Mq\\x1a\\x08Wba\\x00}@\\x1f\\x03_\\x05Qe\\x04SD\\x12Y\\x07v\\x12w\\x12d\\x01\\x0f\\x12\\rJRH~PNyhs\\x00ho\\x01Chh\\x7f\\x06bFR\\x16EN\\x06~t|\\x0e\\x12\\x00\\x01EGs\\x07\\x12PPA\\x7fU}K]aeKCL\\x02\\x06J\\x7f\\nC]~Np\\x04\\x10\\x04N^OE]y__RrCPDT\\x1d`vQAZy`E\\x1e\\x00bnF\\x04'",
                "4": "x[_\\",
                "6": 12,
                "7": "b'\\x1dw\\x03\\x01|\\x0f\\x05~\\x15\\x1d'",
                "8": str(game_version),
                "9": 3,
                "10": 1,
                "11": "b'\\x03bbSQ60fJ5585AdV2KyoVlf7P5QAyHLjD7gD6iaZ6fc2s6cKUeUDd6tFWHQETP2VheA5t+8yuSjUAUUnGG9IeCZP+leQ7kjM+lsq7p/PX7sWjVJKTBPXS036BJgsvhF4PKGq4NEAaOyA62ej+6ICqKV551uOJC0l2V8X+BCg7+zS67F2THxhRrXhYMQx2bRzO4HOS8nQ90t3ZVD4GpBnqHZOvReH5VUXHaAY6hVaYN3uG4fU/WaJhGLWwo4jnNzRYKZqL1c1/Sd35vCYjS5MrGCSJREaea13unAe1ZrQ/gkOaRabv5tB9/mkZkPgGBtadBR3+8xseUIsj9UtGdA0IEjZRgZRtd3U8qNDJ53LSPn0+JT8YDpTaK/HA7I6kaVfedLgJt2T1LlBYqIV4rawcoaeTtYfVZXU+3bg5jr0ciGziEqgQWYYuQhbgaPBlN7HnpVuYN9Kr7BqU6UBQcpmedOtML+BpIFWa5WlRmF1fGRk+lmxPI0Hv3mN8vGrixl6lc02zfTZ5uNHqQbmX1nBi06A+kRj1KWddwGhud0jeIDC3mlMGtgxl+igx7PzsSv7gcYlSbBoEDKB9I5eufN3QxHUKLHegxQdivi/vaGIWzRXFk2ppML1LLlCKQJUX8CxaDI36/LRxT3Ko/qonJIKJR4aA0x103axwVmCWG6GWOkXziYQb7G8fxWoXxtar'"
            },
            "20": [
                {
                    "1": 3,
                    "2": 394
                },
                {
                    "1": 4,
                    "2": 391
                },
                {
                    "1": 5,
                    "2": 192
                },
                {
                    "1": 29,
                    "2": 204
                },
                {
                    "1": 22,
                    "2": 120
                },
                {
                    "1": 14,
                    "2": 175
                },
                "b'\\x08\\x15'"
            ],
            "21": "a_6534489873065906362"
        }
    }

    return create_packet(encode_protobuf(fields), '0324', key, iv)


def _build_sync_time_ack(server_tick):
    o = bytearray()
    _put_varint(o, int(server_tick) & 0xFFFFFFFF)
    return bytes(o)


def _rd_varint(b, p):
    v = 0
    sh = 0
    while p < len(b):
        c = b[p]; p += 1
        v |= (c & 0x7F) << sh
        if not (c & 0x80):
            return v, p
        sh += 7
        if sh > 70:
            break
    return v, p


def _wr_varint(o, v):
    v = int(v) & 0xFFFFFFFFFFFFFFFF
    while v >= 0x80:
        o.append((v & 0x7F) | 0x80); v >>= 7
    o.append(v)


def _wr_zig(o, v):
    _wr_varint(o, (int(v) << 1) ^ (int(v) >> 63))


def _wr_str(o, s):
    b = s.encode("utf-8") if isinstance(s, str) else bytes(s)
    _wr_zig(o, len(b)); o.extend(b)


def _wr_byte(o, v):
    o.append(int(v) & 0xFF)


def build_join_post_body(named):
    b = bytearray()
    _wr_varint(b, named["account_id"])
    _wr_varint(b, named["match_id"])
    _wr_byte(b, named["const_1"])
    _wr_byte(b, named["game_mode"])
    _wr_varint(b, named["match_id_again"])
    _wr_byte(b, named["map_id"])
    _wr_byte(b, named["zero_7"])
    _wr_varint(b, named["zero_8"])
    _wr_varint(b, named["zero_9"])
    _wr_byte(b, named["zero_10"])
    _wr_byte(b, named["is_emulator"])
    _wr_byte(b, named["zero_12"])
    _wr_byte(b, named["one_13"])
    _wr_byte(b, named["two_14"])
    _wr_byte(b, named["three_15"])
    _wr_byte(b, named["antihack_tick"])
    _wr_byte(b, named["one_17"])
    _wr_str(b, named["country"])
    _wr_varint(b, named["zero_19"])
    _wr_byte(b, named["one_20"])
    _wr_byte(b, named["two_21"])
    _wr_byte(b, named["zero_22"])
    _wr_byte(b, named["one_23"])
    _wr_byte(b, named["zero_24"])
    _wr_byte(b, named["zero_25"])
    _wr_byte(b, named["four_26"])
    _wr_str(b, named["client_version"])
    _wr_str(b, named["client_version_code"])
    _wr_str(b, named["client_url"])
    _wr_byte(b, named["zero_30"])
    _wr_byte(b, named["zero_31"])
    _wr_varint(b, named["friend_count"])
    _wr_byte(b, named["zero_33"])
    _wr_varint(b, named["drift_owner_id"])
    _wr_str(b, named["drift_owner_name"])
    _wr_byte(b, named["one_36"])
    _wr_str(b, named["empty_37"])
    _wr_str(b, named["empty_38"])
    _wr_byte(b, named["zero_39"])
    _wr_varint(b, named["zero_40"])
    _wr_varint(b, named["zero_41"])
    _wr_byte(b, named["zero_42"])
    _wr_byte(b, named["zero_43"])
    _wr_byte(b, named["zero_44"])
    _wr_varint(b, named["zero_45"])
    _wr_str(b, named["empty_46"])
    _wr_varint(b, named["zero_47"])
    _wr_byte(b, named["zero_48"])
    _wr_byte(b, named["one_49"])
    _wr_byte(b, named["zero_50"])
    _wr_byte(b, named["zero_51"])
    _wr_varint(b, named["zero_52"])
    _wr_varint(b, named["zero_53"])
    _wr_byte(b, named["zero_54"])
    _wr_byte(b, named["one_55"])
    _wr_str(b, named["empty_56"])
    _wr_varint(b, named["zero_57"])
    _wr_byte(b, named["zero_58"])
    _wr_byte(b, named["zero_59"])
    _wr_byte(b, named["zero_60"])
    _wr_byte(b, named["match_mode"])
    _wr_byte(b, named["zero_62"])
    _wr_varint(b, named["session_tag"])
    _wr_byte(b, named["two_64"])
    _wr_byte(b, named["zero_65"])
    _wr_str(b, named["client_ip"])
    _wr_str(b, named["client_fingerprint"])
    _wr_str(b, named["token_part2"])
    return bytes(b)


def split_jwt_token(jwt):
    raw = int(len(jwt) * 0.85)
    p1  = raw - (raw % 40)
    while 40 + 100 + p1 > 1300 and p1 > 40:
        p1 -= 40
    return jwt[:p1], jwt[p1:]


def _put_varint(o, v):
    while v >= 0x80:
        o.append((v & 0x7F) | 0x80); v >>= 7
    o.append(v)


def _put_zig(o, v):
    _put_varint(o, (v << 1) ^ (v >> 63))


def _put_string(o, s):
    raw = s.encode() if isinstance(s, str) else s
    _put_zig(o, len(raw)); o += raw


def build_join_prepare_body(tok1):
    o = bytearray()
    _put_string(o, tok1)
    return bytes(o)


def decode_udp(pkt, key, order):
    if len(pkt) < 8:
        return None
    k  = key[0]
    kk = k | (k << 8)
    mk, crc = pkt[0], pkt[1]
    if not (90 <= mk <= 110):
        return None
    if crc7_buf(0, pkt[2:]) != crc:
        return None
    reliable = mk < 100
    hdr = 10 if reliable else 8
    if len(pkt) < hdr:
        return None
    off = 2
    f   = {2: 0}
    for fid in order:
        if fid == 2 and not reliable:
            continue
        if fid in (0, 3):
            f[fid] = pkt[off] ^ k
            off += 1
        else:
            f[fid] = struct.unpack_from("<H", pkt, off)[0] ^ kk
            off += 2
    payload = pkt[hdr:]
    body = tea_decrypt(payload, key) if f.get(3, 0) & 1 else payload
    return {
        "MsgKey":     mk,
        "Cmd":        f.get(1, 0),
        "OrderID":    f.get(2, 0),
        "Flags":      f.get(3, 0),
        "SendOption": f.get(0, 0),
        "reliable":   reliable,
        "body":       body,
    }


def build_448_named_payload(json_data, f5, region_v, game_version_v, stronghold_str, part2, fingerprint_v):
    return {
        "account_id":int(json_data.get(1)),
        "match_id":int(f5.get(1)),
        "const_1":1,
        "game_mode":int(f5.get(7)),
        "match_id_again":int(f5.get(1)),
        "map_id":int(f5.get(6)),
        "zero_7":0,
        "zero_8":0,
        "zero_9":0,
        "zero_10":0,
        "is_emulator":0,
        "zero_12":0,
        "one_13":1,
        "two_14":1,
        "three_15":3,
        "antihack_tick":1,
        "one_17":1,
        "country":str(region_v),
        "zero_19":0,
        "one_20":1,
        "two_21":1,
        "zero_22":0,
        "one_23":1,
        "zero_24":0,
        "zero_25":0,
        "four_26":4,
        "client_version":str(game_version_v),
        "client_version_code":"2019121229",
        "client_url":stronghold_str,
        "zero_30":0,
        "zero_31":0,
        "friend_count":4,
        "zero_33":0,
        "drift_owner_id":0,
        "drift_owner_name":"",
        "one_36":1,
        "empty_37":"",
        "empty_38":"",
        "zero_39":0,
        "zero_40":0,
        "zero_41":0,
        "zero_42":0,
        "zero_43":0,
        "zero_44":0,
        "zero_45":0,
        "empty_46":"",
        "zero_47":0,
        "zero_48":0,
        "one_49":1,
        "zero_50":0,
        "zero_51":0,
        "zero_52":4,
        "zero_53":0,
        "zero_54":0,
        "one_55":1,
        "empty_56":"",
        "zero_57":0,
        "zero_58":0,
        "zero_59":0,
        "zero_60":3,
        "match_mode":int(f5.get(8)),
        "zero_62":0,
        "session_tag":int(time.time() * 1_000_000) & 0xFFFFFFFFFFFFFFFF,
        "two_64":2,
        "zero_65":0,
        "client_ip":f5.get(2).split(":")[0],
        "client_fingerprint":fingerprint_v,
        "token_part2":part2,
    }


async def process_game_udp(json_data):
    if not isinstance(json_data, dict):
        return

    f5 = json_data.get(5)
    if not isinstance(f5, dict):
        return

    if not f5.get(2) or not f5.get(4):
        print(f"{Fore.RED}[UDP] missing server_addr/jwt{Style.RESET_ALL}")
        return

    sock = None
    try:
        ip, port = f5.get(2).split(":")
        port     = int(port)
        udp_key  = bytes.fromhex(f5.get(3))
        order    = parse_mask(str(f5.get(42)) if f5.get(42) else "01234")
        jwt_str  = f5.get(4)
        part1, part2 = split_jwt_token(jwt_str)

        if isinstance(stronghold_raw, (bytes, bytearray)):
            stronghold_str = stronghold_raw.decode("utf-8", errors="ignore")
        else:
            stronghold_str = str(stronghold_raw) if stronghold_raw else "csoversea.stronghold.freefiremobile.com"

        fingerprint_v = "70c7ccdca4c94a26c670c1571b9578c92c49bcfc2898922a73c5008401b94759"
        if isinstance(fingerprint_v, bytes):
            fingerprint_v = fingerprint_v.hex()

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setblocking(False)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1 << 20)
        sock.connect((ip, port))

        loop = asyncio.get_running_loop()

        def _log_send(pkt, label):
            print(f"{Fore.GREEN}[UDP] → SEND  {label}  {len(pkt)}B{Style.RESET_ALL}")
            print(f"{Fore.CYAN}  hex: {pkt.hex()}{Style.RESET_ALL}")

        def _log_recv(data, dec):
            if dec:
                cmd  = dec["Cmd"]
                name = MESSAGE_ID_TO_NAME.get(cmd, f"CMD_{cmd}")
                print(f"{Fore.CYAN}[UDP] ← RECV  Cmd={cmd} ({name})  {len(data)}B  reliable={dec['reliable']}  oid={dec['OrderID']}{Style.RESET_ALL}")
            else:
                print(f"{Fore.MAGENTA}[UDP] ← RECV  {len(data)}B (undecoded){Style.RESET_ALL}")
            print(f"{Fore.YELLOW}  hex: {data.hex()}{Style.RESET_ALL}")

        hello = build_udp_hello(json_data.get(1), prefix="0", key=udp_key, order=order)
        await loop.sock_sendall(sock, hello)
        _log_send(hello, "Cmd=1 (HELLO)")

        got_server_hello = False
        got_server_ack   = False
        deadline_hello   = loop.time() + 15.0
        last_send_hello  = loop.time()
        acked_hello_oids = set()

        while loop.time() < deadline_hello and not (got_server_hello and got_server_ack):
            try:
                data = await asyncio.wait_for(loop.sock_recv(sock, 65535), timeout=0.5)
            except asyncio.TimeoutError:
                if loop.time() - last_send_hello >= 1.0:
                    await loop.sock_sendall(sock, hello)
                    _log_send(hello, "Cmd=1 (HELLO) retry")
                    last_send_hello = loop.time()
                continue

            dec = decode_udp(data, udp_key, order)
            _log_recv(data, dec)

            if dec is None:
                continue

            if dec["Cmd"] == 1 and not got_server_hello:
                got_server_hello = True
                req = (dec["OrderID"] + 1) & 0xFFFF
                if dec["OrderID"] not in acked_hello_oids:
                    acked_hello_oids.add(dec["OrderID"])
                    ack_pkt = encode_udp(2, 0, 0, 0, struct.pack("<H", req), udp_key, order)
                    await loop.sock_sendall(sock, ack_pkt)
                    _log_send(ack_pkt, f"Cmd=2 (ACK for server HELLO)  req={req}")

            if dec["Cmd"] == 2 and not got_server_ack:
                got_server_ack = True
                print(f"{Fore.GREEN}[UDP] our HELLO acked by server{Style.RESET_ALL}")

        if not (got_server_hello and got_server_ack):
            print(f"{Fore.RED}[UDP] HELLO handshake incomplete (server_hello={got_server_hello}, ack={got_server_ack}) — abort{Style.RESET_ALL}")
            return

        print(f"{Fore.GREEN}[UDP] HELLO handshake complete — proceeding to 447{Style.RESET_ALL}")

        pkt_447 = encode_udp(447, 2, 0, 1, build_join_prepare_body(part1), udp_key, order)
        await loop.sock_sendall(sock, pkt_447)
        _log_send(pkt_447, f"Cmd=447 (JOIN_PREPARE)  tok1={len(part1)}B")

        got_ack_447 = False
        deadline_447 = loop.time() + 10.0
        last_send_447 = loop.time()
        acked_oids = set()

        while loop.time() < deadline_447 and not got_ack_447:
            try:
                data = await asyncio.wait_for(loop.sock_recv(sock, 65535), timeout=0.3)
            except asyncio.TimeoutError:
                if loop.time() - last_send_447 >= 1.0:
                    await loop.sock_sendall(sock, pkt_447)
                    _log_send(pkt_447, "Cmd=447 (JOIN_PREPARE) resend")
                    last_send_447 = loop.time()
                continue

            dec = decode_udp(data, udp_key, order)
            _log_recv(data, dec)

            if dec is None:
                continue

            if dec["Cmd"] == 2:
                got_ack_447 = True
                print(f"{Fore.GREEN}[UDP] 447 ACK received{Style.RESET_ALL}")
                break

            if dec["reliable"] and dec["OrderID"] not in acked_oids:
                acked_oids.add(dec["OrderID"])
                req = (dec["OrderID"] + 1) & 0xFFFF
                ack_pkt = encode_udp(2, 0, 0, 0, struct.pack("<H", req), udp_key, order)
                await loop.sock_sendall(sock, ack_pkt)
                _log_send(ack_pkt, f"Cmd=2 (ACK)  req={req}")

        if not got_ack_447:
            print(f"{Fore.RED}[UDP] 447 no ACK — abort{Style.RESET_ALL}")
            return

        try:
            named_448 = build_448_named_payload(json_data, f5, region, game_version, stronghold_str, part2, fingerprint_v)
            body_448  = build_join_post_body(named_448)
            pkt_448   = encode_udp(448, 2, 1, 1, body_448, udp_key, order)
            await loop.sock_sendall(sock, pkt_448)
            _log_send(pkt_448, f"Cmd=448 (JOIN_POST)  body={len(body_448)}B  tok2={len(part2)}B")
        except Exception as e:
            print(f"{Fore.RED}[UDP] 448 build error: {e}{Style.RESET_ALL}")
            import traceback; traceback.print_exc()

        PING_INTERVAL = 4.0
        next_ping = loop.time() + PING_INTERVAL
        main_acked_oids = set()

        while True:
            now = loop.time()

            if now >= next_ping:
                tick = int(time.time() * 1000) & 0xFFFFFFFF
                ping_body = bytearray()
                _put_zig(ping_body, tick)
                _put_zig(ping_body, 0)
                _put_zig(ping_body, 0)
                _put_zig(ping_body, 0)
                ping_pkt = encode_udp(3, 0, 0, 0, bytes(ping_body), udp_key, order)
                await loop.sock_sendall(sock, ping_pkt)
                next_ping = now + PING_INTERVAL

            try:
                data = await asyncio.wait_for(loop.sock_recv(sock, 65535), timeout=0.02)
            except asyncio.TimeoutError:
                continue

            dec = decode_udp(data, udp_key, order)
            _log_recv(data, dec)

            if dec is None:
                continue

            if dec["reliable"] and dec["OrderID"] not in main_acked_oids:
                main_acked_oids.add(dec["OrderID"])
                req = (dec["OrderID"] + 1) & 0xFFFF
                ack_pkt = encode_udp(2, 0, 0, 0, struct.pack("<H", req), udp_key, order)
                await loop.sock_sendall(sock, ack_pkt)
                _log_send(ack_pkt, f"Cmd=2 (ACK)  req={req}")

            if dec["Cmd"] == 2000 and dec["body"]:
                try:
                    st, _ = _rd_varint(dec["body"], 0)
                    ack_body = _build_sync_time_ack(st)
                    ack_pkt  = encode_udp(2000, 0, 0, 1, ack_body, udp_key, order)
                    await loop.sock_sendall(sock, ack_pkt)
                    _log_send(ack_pkt, f"Cmd=2000 (SYNC_TIME ack)  tick={st}")
                except Exception as e:
                    print(f"{Fore.RED}[UDP] SYNC_TIME error: {e}{Style.RESET_ALL}")

            if dec["Cmd"] == 103:
                print(f"{Fore.RED}[UDP] MATCH END{Style.RESET_ALL}")
                break

    except Exception as e:
        print(f"{Fore.RED}[UDP] error: {e}{Style.RESET_ALL}")
        import traceback; traceback.print_exc()
    finally:
        if sock:
            try: sock.close()
            except Exception: pass


def _tea_enc_block(blk, k):
    y, z = struct.unpack("<2I", blk)
    s = 0
    for _ in range(16):
        s = (s + 0x9E3779B9) & 0xFFFFFFFF
        y = (y + ((((z << 4) & 0xFFFFFFFF) + k[0]) ^ (z + s) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF
        z = (z + ((((y << 4) & 0xFFFFFFFF) + k[2]) ^ (y + s) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF
    return struct.pack("<2I", y, z)


def _tea_dec_block(blk, k):
    y, z = struct.unpack("<2I", blk)
    s = (0x9E3779B9 << 4) & 0xFFFFFFFF
    for _ in range(16):
        z = (z - ((((y << 4) & 0xFFFFFFFF) + k[2]) ^ (y + s) ^ ((y >> 5) + k[3]))) & 0xFFFFFFFF
        y = (y - ((((z << 4) & 0xFFFFFFFF) + k[0]) ^ (z + s) ^ ((z >> 5) + k[1]))) & 0xFFFFFFFF
        s = (s - 0x9E3779B9) & 0xFFFFFFFF
    return struct.pack("<2I", y, z)


def tea_encrypt(data, key):
    SALT_LEN = 2
    ZERO_LEN = 7
    k = list(struct.unpack("<4I", key[:16]))
    n = 1 + SALT_LEN + len(data) + ZERO_LEN
    r = n % 8
    n += (8 - r if r else 0)
    pad_len = n - (1 + SALT_LEN + len(data) + ZERO_LEN)
    plain = bytearray(n)
    plain[0] = pad_len
    plain[1 + pad_len + SALT_LEN : 1 + pad_len + SALT_LEN + len(data)] = data
    out = bytearray(n)
    iv_p = iv_c = bytes(8)
    for off in range(0, n, 8):
        blk = bytes(a ^ b for a, b in zip(plain[off:off+8], iv_c))
        c = bytes(a ^ b for a, b in zip(_tea_enc_block(blk, k), iv_p))
        out[off:off+8] = c
        iv_p, iv_c = blk, c
    return bytes(out)


def tea_decrypt(buf, key):
    SALT_LEN = 2
    ZERO_LEN = 7
    if len(buf) < 16 or len(buf) % 8:
        return None
    k = list(struct.unpack("<4I", key[:16]))
    pad_len = _tea_dec_block(buf[0:8], k)[0] & 7
    out_len = len(buf) - pad_len - 1 - SALT_LEN - ZERO_LEN
    if out_len < 0:
        return None
    plain = bytearray(len(buf))
    iv_p = iv_c = bytes(8)
    for off in range(0, len(buf), 8):
        c = buf[off:off+8]
        t = bytes(a ^ b for a, b in zip(c, iv_p))
        blk = _tea_dec_block(t, k)
        plain[off:off+8] = bytes(a ^ b for a, b in zip(blk, iv_c))
        iv_p, iv_c = blk, c
    at = 1 + pad_len + SALT_LEN
    if bytes(plain[at + out_len:]) != bytes(ZERO_LEN):
        return None
    return bytes(plain[at:at + out_len])


def parse_mask(mask):
    if len(mask) != 5:
        return [0, 1, 2, 3, 4]
    o = [int(c) for c in mask]
    return o if sorted(o) == [0, 1, 2, 3, 4] else [0, 1, 2, 3, 4]


def _crc7_table():
    t = []
    for b in range(256):
        c = 0
        for i in range(8):
            top = ((c >> 6) & 1) ^ ((b >> (7 - i)) & 1)
            c = (c << 1) & 0x7F
            if top:
                c ^= 0x09
        t.append(c)
    return t


CRC7 = _crc7_table()


def crc7_byte(crc, b):
    return CRC7[((crc << 1) ^ b) & 0xFF]


def crc7_u16(crc, v):
    return crc7_byte(crc7_byte(crc, v & 0xFF), (v >> 8) & 0xFF)


def crc7_buf(crc, data):
    for b in data:
        crc = CRC7[((crc << 1) ^ b) & 0xFF]
    return crc


def is_reliable(cmd, so):
    if cmd == 2 or not 1 <= so <= 5:
        return False
    return bool((0x13 >> (so - 1)) & 1)


def gen_msg_key(cmd, so):
    if is_reliable(cmd, so):
        return random.randrange(90, 100)
    return random.randrange(100, 110)


def encode_udp(cmd, so, oid, flags, body, key, order):
    reliable = is_reliable(cmd, so)
    payload = tea_encrypt(body, key) if flags & 1 else body
    k = key[0]
    kk = k | (k << 8)
    m = {
        0: so ^ k,
        1: cmd ^ kk,
        2: oid ^ kk,
        3: flags ^ k,
        4: len(payload) ^ kk,
    }
    out = bytearray([gen_msg_key(cmd, so), 0])
    crc = 0
    for fid in order:
        if fid == 2 and not reliable:
            continue
        v = m[fid]
        if fid in (0, 3):
            crc = crc7_byte(crc, v)
            out.append(v)
        else:
            crc = crc7_u16(crc, v)
            out += struct.pack("<H", v)
    out += payload
    out[1] = crc7_buf(crc, payload)
    return bytes(out)


def build_udp_hello(account_id, prefix="0", key=None, order=None):
    if key is None or order is None:
        raise ValueError("build_udp_hello needs key and order")
    raw = f"{int(account_id)}_{prefix}".encode()
    body = struct.pack("<i", len(raw)) + raw + bytes(9)
    return encode_udp(1, 1, 0, 1, body, key, order)


async def process_0300(json_data):
    if not isinstance(json_data, dict):
        return
    f4 = json_data.get(4)
    f5 = json_data.get(5) if isinstance(json_data.get(5), dict) else None
    if not f5:
        return

    if f4 == 11:
        tag = f"{Fore.CYAN}[QUEUE]{Style.RESET_ALL}"
        try:
            acc_id   = json_data.get(1)
            map_id   = f5.get(1)
            mode_id  = f5.get(2)
            sub_type = f5.get(5)
            MODE_NAMES = {1: "Battle Royale", 15: "Clash Squad", 43: "Lone Wolf", 62: "Social Island", 23: "Training Ground"}
            LW_TYPE = {1: "Normal", 2: "Ranked", 5: "Normal"}
            mode_name = MODE_NAMES.get(mode_id, f"Unknown ({mode_id})")
            sub_label = LW_TYPE.get(sub_type, f"type={sub_type}") if mode_id == 43 else f"type={sub_type}"
            print(f"{tag} {Fore.CYAN}QUEUE INFO{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}account_id :{Style.RESET_ALL} {Fore.YELLOW}{acc_id}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}mode       :{Style.RESET_ALL} {Fore.MAGENTA}{mode_name}{Style.RESET_ALL} ({sub_label})")
            print(f"{tag} {Fore.GREEN}map_id     :{Style.RESET_ALL} {Fore.YELLOW}{map_id}{Style.RESET_ALL}")
        except Exception as e:
            print(f"{tag} {Fore.RED}ERROR: {e}{Style.RESET_ALL}")
        return

    if f4 == 5:
        tag = f"{Fore.GREEN}[MATCH]{Style.RESET_ALL}"
        try:
            acc_id      = json_data.get(1)
            match_id    = f5.get(1)
            server_addr = f5.get(2)
            token       = f5.get(3)
            jwt         = f5.get(4)
            map_val     = f5.get(6)
            mode_val    = f5.get(7)
            match_type  = f5.get(8)
            idc         = f5.get(42)
            MODE_NAMES = {1: "Battle Royale", 15: "Clash Squad", 43: "Lone Wolf", 62: "Social Island", 23: "Training Ground"}
            mode_name = MODE_NAMES.get(mode_val, f"Unknown ({mode_val})")
            print(f"{tag} {Fore.CYAN}MATCH FOUND{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}account_id :{Style.RESET_ALL} {Fore.YELLOW}{acc_id}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}match_id   :{Style.RESET_ALL} {Fore.YELLOW}{match_id}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}server     :{Style.RESET_ALL} {Fore.MAGENTA}{server_addr}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}key        :{Style.RESET_ALL} {Fore.BLUE}{token}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}jwt        :{Style.RESET_ALL} {Fore.BLUE}{jwt}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}map_id     :{Style.RESET_ALL} {Fore.YELLOW}{map_val}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}mode       :{Style.RESET_ALL} {Fore.MAGENTA}{mode_val} ({mode_name}){Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}match_type :{Style.RESET_ALL} {Fore.YELLOW}{match_type}{Style.RESET_ALL}")
            print(f"{tag} {Fore.GREEN}musk       :{Style.RESET_ALL} {Fore.YELLOW}{idc}{Style.RESET_ALL}")
            await process_game_udp(json_data)
        except Exception as e:
            print(f"{tag} {Fore.RED}ERROR: {e}{Style.RESET_ALL}")
        return


def decode_packet(data):
    def _varint(data, offset):
        result, shift = 0, 0
        while offset < len(data):
            b = data[offset]; offset += 1
            result |= (b & 0x7F) << shift
            if not (b & 0x80):
                return result, offset
            shift += 7
            if shift > 70:
                return None, offset
        return None, offset

    def _printable(raw):
        try:
            s = raw.decode('utf-8')
        except:
            return False
        if not s:
            return False
        return sum(1 for c in s if c.isprintable() or c in '\n\r\t') / len(s) >= 0.9

    def _parse(data, depth=0):
        if not data or depth > 20:
            return None, 0
        result = {}
        offset = 0
        n = len(data)
        while offset < n:
            try:
                key, offset = _varint(data, offset)
                if key is None or key == 0:
                    return None, 0
                field, wire = key >> 3, key & 7
                if field == 0:
                    return None, 0
                if wire == 0:
                    val, offset = _varint(data, offset)
                    if val is None:
                        return None, 0
                elif wire == 1:
                    if offset + 8 > n:
                        return None, 0
                    val = struct.unpack('<Q', data[offset:offset+8])[0]
                    offset += 8
                elif wire == 2:
                    length, offset = _varint(data, offset)
                    if length is None or offset + length > n:
                        return None, 0
                    raw = data[offset:offset+length]
                    offset += length
                    if not raw:
                        val = ""
                    elif _printable(raw):
                        val = raw.decode('utf-8', errors='replace')
                    else:
                        nested, consumed = _parse(raw, depth+1)
                        val = nested if nested and consumed == len(raw) else raw.hex()
                elif wire == 5:
                    if offset + 4 > n:
                        return None, 0
                    val = struct.unpack('<I', data[offset:offset+4])[0]
                    offset += 4
                else:
                    return None, 0
                if field in result:
                    if not isinstance(result[field], list):
                        result[field] = [result[field]]
                    result[field].append(val)
                else:
                    result[field] = val
            except:
                return None, 0
        return (result, offset) if offset == n else (None, 0)

    try:
        data = bytes.fromhex(data.replace(" ", "")) if isinstance(data, str) else data
        if not data:
            return None
        if len(data) > 5:
            declared = int.from_bytes(data[2:5], 'big')
            if declared == len(data) - 5:
                data = data[5:]
        result, _ = _parse(data)
        return result
    except:
        return None


def create_packet(Pk, N, K, V):
    Pk = bytes.fromhex(Pk) if isinstance(Pk, str) else bytes(Pk)
    N  = bytes.fromhex(N)  if isinstance(N, str)  else bytes(N)
    K  = bytes.fromhex(K)  if isinstance(K, str) else K
    V  = bytes.fromhex(V)  if isinstance(V, str) else V
    ct = AES.new(K, AES.MODE_CBC, V).encrypt(pad(Pk, 16))
    return N + len(ct).to_bytes(4, 'big') + ct


async def _heartbeat(writer, tag, interval=10):
    try:
        while True:
            await asyncio.sleep(interval)
            if writer is None or writer.is_closing():
                break
            try:
                writer.write(bytes.fromhex("0219"))
                await writer.drain()
                print(f"{Fore.BLUE}[{tag}] heartbeat sent: 0219{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}[{tag}] heartbeat error: {e}{Style.RESET_ALL}")
                break
    except asyncio.CancelledError:
        pass


def build_auth_packet(account_id, jwt_token, timestamp, key, iv, typee):
    ct = AES.new(key, AES.MODE_CBC, iv).encrypt(pad(jwt_token.encode(), AES.block_size))
    header = bytes.fromhex('7724') + int(account_id).to_bytes(8, 'big') + int(timestamp).to_bytes(4, 'big')
    if typee == 'online':
        header += b'\x00\x00\x00\x00'
    header += len(ct).to_bytes(4, 'big')
    return (header + ct).hex()


async def send_packet(packet, packet_type):
    global online_writer
    if packet_type == 'online':
        if online_writer is None or online_writer.is_closing():
            print(f"{Fore.RED}[PACKET] online_writer not ready{Style.RESET_ALL}")
            return None
        try:
            online_writer.write(packet)
            await online_writer.drain()
            print(f"{Fore.GREEN}[PACKET] online sent {len(packet)}B{Style.RESET_ALL} {Fore.CYAN}{packet.hex()}{Style.RESET_ALL}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[PACKET] online error: {e}{Style.RESET_ALL}")
            return None
    else:
        print(f"{Fore.RED}[PACKET] unknown type: {packet_type}{Style.RESET_ALL}")
        return None


async def tcp_online(ip, port, auth_packet, key, iv):
    global online_writer
    while True:
        try:
            reader, online_writer = await asyncio.open_connection(ip, int(port))

            print(f"{Fore.GREEN}[ONLINE] auth:{Style.RESET_ALL} {Fore.CYAN}{auth_packet.hex()}{Style.RESET_ALL}")

            online_writer.write(auth_packet)
            await online_writer.drain()
            print(f"{Fore.GREEN}[ONLINE] Connected{Style.RESET_ALL}")

            # Send solo Triple Wolves matchmaking immediately after connecting
            pkt = start_solo_triple_wolves(game_version, region, key, iv)
            await send_packet(pkt, 'online')
            print(f"{Fore.GREEN}[ONLINE] Solo Triple Wolves queue started{Style.RESET_ALL}")

            hb_task = asyncio.create_task(_heartbeat(online_writer, "ONLINE"))

            while True:
                try:
                    header = await reader.readexactly(5)
                    length = int.from_bytes(header[1:5], 'big')
                    body = await reader.readexactly(length) if length else b''
                except asyncio.IncompleteReadError:
                    print(f"{Fore.RED}[ONLINE] Disconnected{Style.RESET_ALL}")
                    break
                data = header + body
                print(f"{Fore.MAGENTA}[ONLINE] received:{Style.RESET_ALL} {Fore.CYAN}{data.hex()}{Style.RESET_ALL}")

                decoded = decode_packet(data)
                if decoded:
                    print(f"{Fore.YELLOW}[ONLINE] decoded: {json.dumps(decoded, indent=2, default=str)}{Style.RESET_ALL}")

                if data.startswith(bytes.fromhex("0300")):
                    await process_0300(decoded)

            hb_task.cancel()
            try:
                await hb_task
            except asyncio.CancelledError:
                pass

        except Exception as e:
            print(f"{Fore.RED}[ONLINE ERROR] {e}{Style.RESET_ALL}")
            online_writer = None
            await asyncio.sleep(1)


def decode_protobuf(data, raw_fields=None):
    if not isinstance(data, (bytes, bytearray)):
        return {}
    if raw_fields is None:
        raw_fields = ()
    result = {}
    pos = 0
    n = len(data)
    try:
        while pos < n:
            tag = 0; shift = 0; vb = 0
            while pos < n:
                b = data[pos]; pos += 1; vb += 1
                tag |= (b & 0x7F) << shift; shift += 7
                if not (b & 0x80): break
                if vb >= 10: return result
            else:
                return result
            field_num = tag >> 3; wire = tag & 0x07
            if field_num == 0: break
            if wire == 0:
                val = 0; shift = 0; vb = 0
                while pos < n:
                    b = data[pos]; pos += 1; vb += 1
                    val |= (b & 0x7F) << shift; shift += 7
                    if not (b & 0x80): break
                    if vb >= 10: return result
                else:
                    return result
                value = val
            elif wire == 1:
                if pos + 8 > n: return result
                raw8 = data[pos:pos+8]; pos += 8
                f = struct.unpack('<d', raw8)[0]
                value = struct.unpack('<Q', raw8)[0] if (f != f or abs(f) == float('inf')) else f
            elif wire == 2:
                ln = 0; shift = 0; vb = 0
                while pos < n:
                    b = data[pos]; pos += 1; vb += 1
                    ln |= (b & 0x7F) << shift; shift += 7
                    if not (b & 0x80): break
                    if vb >= 10: return result
                else:
                    return result
                if pos + ln > n: return result
                raw = bytes(data[pos:pos+ln]); pos += ln
                if field_num in raw_fields:
                    value = raw
                elif ln == 0:
                    value = ""
                else:
                    nested = decode_protobuf(raw, raw_fields) if len(raw) >= 4 else {}
                    value = raw
                    if nested:
                        enc = bytearray(); enc_ok = True
                        enc_stack = []
                        for ek, ev in nested.items():
                            enc_stack.append((int(ek), ev))
                        while enc_stack:
                            if not enc_ok: break
                            ek, ev = enc_stack.pop(0)
                            evs = ev if isinstance(ev, list) else [ev]
                            for item in evs:
                                if isinstance(item, bool): item = int(item)
                                if isinstance(item, int):
                                    tv = (ek << 3) | 0
                                    if tv < 0: tv &= 0xFFFFFFFFFFFFFFFF
                                    while True:
                                        tb = tv & 0x7F; tv >>= 7
                                        enc.append(tb | (0x80 if tv else 0))
                                        if not tv: break
                                    uv = item
                                    if uv < 0: uv &= 0xFFFFFFFFFFFFFFFF
                                    while True:
                                        ub = uv & 0x7F; uv >>= 7
                                        enc.append(ub | (0x80 if uv else 0))
                                        if not uv: break
                                elif isinstance(item, str):
                                    bb = item.encode('utf-8')
                                    tv = (ek << 3) | 2
                                    while True:
                                        tb = tv & 0x7F; tv >>= 7
                                        enc.append(tb | (0x80 if tv else 0))
                                        if not tv: break
                                    lv = len(bb)
                                    while True:
                                        lb = lv & 0x7F; lv >>= 7
                                        enc.append(lb | (0x80 if lv else 0))
                                        if not lv: break
                                    enc.extend(bb)
                                elif isinstance(item, (bytes, bytearray)):
                                    tv = (ek << 3) | 2
                                    while True:
                                        tb = tv & 0x7F; tv >>= 7
                                        enc.append(tb | (0x80 if tv else 0))
                                        if not tv: break
                                    lv = len(item)
                                    while True:
                                        lb = lv & 0x7F; lv >>= 7
                                        enc.append(lb | (0x80 if lv else 0))
                                        if not lv: break
                                    enc.extend(item)
                                elif isinstance(item, dict):
                                    sub = bytearray(); sub_ok = True
                                    sub_stack = []
                                    for sk, sv in item.items():
                                        sub_stack.append((int(sk), sv))
                                    while sub_stack:
                                        if not sub_ok: break
                                        sk, sv = sub_stack.pop(0)
                                        svs = sv if isinstance(sv, list) else [sv]
                                        for si in svs:
                                            if isinstance(si, bool): si = int(si)
                                            if isinstance(si, int):
                                                tv = (sk << 3) | 0
                                                while True:
                                                    tb = tv & 0x7F; tv >>= 7
                                                    sub.append(tb | (0x80 if tv else 0))
                                                    if not tv: break
                                                uv = si
                                                if uv < 0: uv &= 0xFFFFFFFFFFFFFFFF
                                                while True:
                                                    ub = uv & 0x7F; uv >>= 7
                                                    sub.append(ub | (0x80 if uv else 0))
                                                    if not uv: break
                                            elif isinstance(si, str):
                                                bb = si.encode('utf-8')
                                                tv = (sk << 3) | 2
                                                while True:
                                                    tb = tv & 0x7F; tv >>= 7
                                                    sub.append(tb | (0x80 if tv else 0))
                                                    if not tv: break
                                                lv = len(bb)
                                                while True:
                                                    lb = lv & 0x7F; lv >>= 7
                                                    sub.append(lb | (0x80 if lv else 0))
                                                    if not lv: break
                                                sub.extend(bb)
                                            elif isinstance(si, (bytes, bytearray)):
                                                tv = (sk << 3) | 2
                                                while True:
                                                    tb = tv & 0x7F; tv >>= 7
                                                    sub.append(tb | (0x80 if tv else 0))
                                                    if not tv: break
                                                lv = len(si)
                                                while True:
                                                    lb = lv & 0x7F; lv >>= 7
                                                    sub.append(lb | (0x80 if lv else 0))
                                                    if not lv: break
                                                sub.extend(si)
                                            else:
                                                sub_ok = False; break
                                        if not sub_ok: break
                                    if not sub_ok:
                                        enc_ok = False; break
                                    tv = (ek << 3) | 2
                                    while True:
                                        tb = tv & 0x7F; tv >>= 7
                                        enc.append(tb | (0x80 if tv else 0))
                                        if not tv: break
                                    lv = len(sub)
                                    while True:
                                        lb = lv & 0x7F; lv >>= 7
                                        enc.append(lb | (0x80 if lv else 0))
                                        if not lv: break
                                    enc.extend(sub)
                                else:
                                    enc_ok = False; break
                            if not enc_ok: break
                        if enc_ok and bytes(enc) == raw:
                            value = nested
                        else:
                            try:
                                s = raw.decode('utf-8')
                                ok = all(ord(c) >= 0x80 or 0x20 <= ord(c) <= 0x7E or c in '\t\n\r' for c in s)
                                value = s if ok else raw
                            except Exception:
                                value = raw
                    else:
                        try:
                            s = raw.decode('utf-8')
                            ok = all(ord(c) >= 0x80 or 0x20 <= ord(c) <= 0x7E or c in '\t\n\r' for c in s)
                            value = s if ok else raw
                        except Exception:
                            value = raw
            elif wire == 5:
                if pos + 4 > n: return result
                raw4 = data[pos:pos+4]; pos += 4
                f = struct.unpack('<f', raw4)[0]
                value = struct.unpack('<I', raw4)[0] if (f != f or abs(f) == float('inf')) else f
            else:
                break
            if field_num in result:
                if isinstance(result[field_num], list):
                    result[field_num].append(value)
                else:
                    result[field_num] = [result[field_num], value]
            else:
                result[field_num] = value
    except RecursionError:
        return {}
    except Exception:
        return result
    return result


def encode_protobuf(data):
    if not isinstance(data, dict):
        return b""
    out = bytearray()
    try:
        for k, v in data.items():
            f = int(k)
            items = v if isinstance(v, list) else [v]
            for item in items:
                if isinstance(item, str) and len(item) >= 3 and item[0] == 'b' and item[1] in ("'", '"') and item[-1] == item[1]:
                    try:
                        _tv = ast.literal_eval(item)
                        if isinstance(_tv, (bytes, bytearray)):
                            item = bytes(_tv)
                    except Exception:
                        pass
                if isinstance(item, bool):
                    item = int(item)
                if isinstance(item, int):
                    tv = (f << 3) | 0
                    if tv < 0:
                        tv &= 0xFFFFFFFFFFFFFFFF
                    while True:
                        tb = tv & 0x7F
                        tv >>= 7
                        out.append(tb | (0x80 if tv else 0))
                        if not tv:
                            break
                    uv = item
                    if uv < 0:
                        uv &= 0xFFFFFFFFFFFFFFFF
                    while True:
                        ub = uv & 0x7F
                        uv >>= 7
                        out.append(ub | (0x80 if uv else 0))
                        if not uv:
                            break
                elif isinstance(item, float):
                    tv = (f << 3) | 5
                    while True:
                        tb = tv & 0x7F
                        tv >>= 7
                        out.append(tb | (0x80 if tv else 0))
                        if not tv:
                            break
                    out.extend(struct.pack('<f', item))
                elif isinstance(item, str):
                    bb = item.encode('utf-8')
                    tv = (f << 3) | 2
                    while True:
                        tb = tv & 0x7F
                        tv >>= 7
                        out.append(tb | (0x80 if tv else 0))
                        if not tv:
                            break
                    lv = len(bb)
                    while True:
                        lb = lv & 0x7F
                        lv >>= 7
                        out.append(lb | (0x80 if lv else 0))
                        if not lv:
                            break
                    out.extend(bb)
                elif isinstance(item, (bytes, bytearray)):
                    tv = (f << 3) | 2
                    while True:
                        tb = tv & 0x7F
                        tv >>= 7
                        out.append(tb | (0x80 if tv else 0))
                        if not tv:
                            break
                    lv = len(item)
                    while True:
                        lb = lv & 0x7F
                        lv >>= 7
                        out.append(lb | (0x80 if lv else 0))
                        if not lv:
                            break
                    out.extend(item)
                elif isinstance(item, dict):
                    sub = encode_protobuf(item)
                    tv = (f << 3) | 2
                    while True:
                        tb = tv & 0x7F
                        tv >>= 7
                        out.append(tb | (0x80 if tv else 0))
                        if not tv:
                            break
                    lv = len(sub)
                    while True:
                        lb = lv & 0x7F
                        lv >>= 7
                        out.append(lb | (0x80 if lv else 0))
                        if not lv:
                            break
                    out.extend(sub)
    except Exception:
        return bytes(out)
    return bytes(out)


def encrypt_aes(data):
    return AES.new(aes_key, AES.MODE_CBC, aes_iv).encrypt(pad(data, 16))


async def update():
    try:
        game_version = '1.132.1'
        print(f"{Fore.CYAN}[UPDATE]{Style.RESET_ALL} play_version: {Fore.YELLOW}{game_version}{Style.RESET_ALL}")

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        url = f'{version_url}/live/ver.php?version={game_version}&lang=en&device=android&channel=android&appsttore=googleplay&region=BD&whitelist_version=1.3.0&whitelist_sp_version=1.0.0&device_name=google%20G011A&device_CPU=ARMv7%20VFPv3%20NEON%20VMH&device_GPU=Adreno%20(TM)%20640&device_mem=1993'

        headers = {
            "User-Agent": "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "X-GA-SV": str(int(time.time())),
            "X-Unity-Version": "2018.4.12f1",
        }

        timeout = aiohttp.ClientTimeout(total=5)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.get(url, headers=headers, ssl=ssl_context) as response:
                text_data = await response.text()
                json_data = json.loads(text_data)

                release_version = json_data.get('latest_release_version', None)
                login_url = json_data.get('server_url', None)
                game_version = json_data.get('remote_version', game_version)

                gop_url_raw = json_data.get('gop_url', '')
                gop_urls = [u.strip() for u in gop_url_raw.split(';') if u.strip()]
                gop_url_1 = gop_urls[0] if len(gop_urls) > 0 else "https://ffmconnect.ppmainecoonghj.com"
                gop_url_2 = gop_urls[1] if len(gop_urls) > 1 else "https://ffmmsdk.ppmainecoonghj.com"

                vercfg_sign = json_data.get('vercfg_sign', None)

                cdn_url = json_data.get('cdn_url', '')
                abhotupdate_cdn_url = json_data.get('abhotupdate_cdn_url', '')
                field_106 = f'{cdn_url}|{abhotupdate_cdn_url}|b6756df94c9ff39b46f783f0998378a7'

                print(f"{Fore.CYAN}[UPDATE]{Style.RESET_ALL} game_version: {Fore.GREEN}{game_version}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[UPDATE]{Style.RESET_ALL} release_version: {Fore.GREEN}{release_version}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[UPDATE]{Style.RESET_ALL} login_url: {Fore.MAGENTA}{login_url}{Style.RESET_ALL}")

                return game_version, release_version, login_url, gop_url_1, gop_url_2, vercfg_sign, field_106

    except asyncio.TimeoutError:
        print(f"{Fore.RED}[UPDATE] TimeoutError{Style.RESET_ALL}")
        return None, None, None, None, None, None, None
    except Exception as e:
        print(f"{Fore.RED}[UPDATE] Exception: {e}{Style.RESET_ALL}")
        return None, None, None, None, None, None, None


async def token_grant(uid, password, gop_url, game_version):
    try:
        gop_url = gop_url.rstrip("/")
        url  = f"{gop_url}/api/v2/oauth/guest/token:grant"
        host = gop_url.replace("https://", "").replace("http://", "").split("/")[0]
        ua_ver = game_version

        data = {
            "uid": int(uid),
            "password": str(password),
            "client_id": 100067,
            "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
            "client_type": 2,
            "response_type": "token"
        }

        headers = {
            "User-Agent": f"GarenaMSDK/4.0.42(SM-E135F ;Android 14;en;GB;app {ua_ver} 2019118332;)",
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
            "Cookie": "datadome=r_6Nar6zkzjU9DZ80_BcBzTGD1sLITCVeLbgwXdYLmz9SW~xsbeOJvtqxJvnAYLj9nub2EaOljgQZs5fCIyz_~Ys1xo1tiPPm05gkNHZuAEnAc9PI~N9NV6XN9TKPyAy",
        }

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url, headers=headers, json=data, ssl=ssl_context) as response:
                text = await response.text()

                if response.status != 200:
                    print(f"{Fore.RED}[TOKEN GRANT] Status: {response.status} | {text}{Style.RESET_ALL}")
                    return None, None, None

                json_data = json.loads(text)
                if json_data.get("code") != 0:
                    print(f"{Fore.RED}[TOKEN GRANT] Error: {json_data.get('error')}{Style.RESET_ALL}")
                    return None, None, None

                d = json_data.get("data", {})
                access_token = d.get("access_token")
                open_id      = d.get("open_id")
                platform     = d.get("platform")

                print(f"{Fore.CYAN}[TOKEN GRANT]{Style.RESET_ALL} access_token: {Fore.GREEN}{access_token}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[TOKEN GRANT]{Style.RESET_ALL} open_id: {Fore.GREEN}{open_id}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}[TOKEN GRANT]{Style.RESET_ALL} platform: {Fore.GREEN}{platform}{Style.RESET_ALL}")

                return access_token, open_id, platform

    except asyncio.TimeoutError:
        print(f"{Fore.RED}[TOKEN GRANT] TimeoutError{Style.RESET_ALL}")
        return None, None, None
    except Exception as e:
        print(f"{Fore.RED}[TOKEN GRANT] Exception: {e}{Style.RESET_ALL}")
        return None, None, None


def load_account(path="account.json"):
    try:
        if not os.path.exists(path):
            print(f"{Fore.RED}[LOAD] File not found: {path}{Style.RESET_ALL}")
            return None, None

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            data = data[0] if data else {}

        uid      = data.get("uid")
        password = data.get("password")

        if not uid or not password:
            print(f"{Fore.RED}[LOAD] uid/password missing in {path}{Style.RESET_ALL}")
            return None, None

        return int(uid), str(password)

    except Exception as e:
        print(f"{Fore.RED}[LOAD] Error: {e}{Style.RESET_ALL}")
        return None, None


async def get_payload(access_token, open_id, platform, version, field_106, vercfg_sign):
    device_id = f"Google|{uuid.uuid4()}"

    base = {
        "3":   str(datetime.now())[:-7],
        "4":   "free fire",
        "5":   1,
        "7":   str(version),
        "8":   "Android OS 14 / API-34 (UP1A.231005.007/E135FXXSEEZE2)",
        "9":   "Handheld",
        "10":  "Stay Home-Teletalk",
        "11":  "CarrierDataNetwork",
        "12":  1672,
        "13":  750,
        "14":  "338",
        "15":  "ARMv7 VFPv3 NEON | 2002 | 8",
        "16":  3702,
        "17":  "Mali-G52",
        "18":  "OpenGL ES 3.2 v1.r38p1-01bet0-mbs2v41_0.6d20ec041e51b2f2d25dfc265586ebe8",
        "19":  device_id,
        "20":  "103.230.104.1",
        "21":  "en",
        "22":  str(open_id),
        "23":  str(platform),
        "24":  "Handheld",
        "25":  "samsung SM-E135F",
        "26":  "BD",
        "29":  str(access_token),
        "30":  1,
        "41":  "Stay Home-Teletalk",
        "42":  "4G",
        "57":  "7428b253defc164018c604a1ebbfebdf",
        "60":  52037,
        "61":  1684,
        "62":  3723,
        "63":  3,
        "64":  1812,
        "65":  52037,
        "66":  1812,
        "67":  52037,
        "73":  2,
        "74":  "/data/app/~~11cX1I9a2OsbN_4l-XiBnQ==/com.dts.freefireth-kdI9kYLF2ST2SRTJZatjvg==/lib/arm",
        "76":  1,
        "77":  "b8e0cd5e295eee42f5860d3c86e483dd|/data/app/~~11cX1I9a2OsbN_4l-XiBnQ==/com.dts.freefireth-kdI9kYLF2ST2SRTJZatjvg==/base.apk",
        "78":  3,
        "79":  1,
        "81":  "32",
        "83":  "2019121229",
        "85":  3,
        "86":  "OpenGLES2",
        "87":  8191,
        "88":  int(platform),
        "92":  15024,
        "93":  "android",
        "94":  "KqsHT7nJH+WKsVGSOVmz8KCOtQTJsJVhiAYcAIeaNekTL/b5yRUY20o0+IqYJ3xvJgtq8YbcQ8mk/J+QECa+u/o5S9x/6ZfIFFCKLL3MpqpD6sOp",
        "95":  111207,
        "96":  '{"cur_rate":null,"support_etc2":false}',
        "97":  1,
        "100": str(platform),
        "102": "b'AWG@U\\x0e\\x0e\\x085'",
        "104": 31537,
        "105": 1,
        "106": field_106,
        "107": "c8e41b7a93f02d56e1a94c7b8203f5d1",
    }

    major = dict(base)
    major["99"] = str(platform)

    login_data = dict(base)
    login_data["90"]  = "Dhaka"
    login_data["91"]  = "C"
    login_data["99"]  = "0"
    login_data["103"] = 1

    proto1 = encode_protobuf(major)
    proto2 = encode_protobuf(login_data)

    return encrypt_aes(proto1), encrypt_aes(proto2)


async def major_login(payload, login_url, release_version):
    try:
        url = f"{login_url}MajorLogin"
        headers = {
            "Accept": "*/*",
            "Authorization": "Bearer ",
            "Content-Type": "application/x-www-form-urlencoded",
            "ReleaseVersion": str(release_version),
            "User-Agent": "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
            "X-GA": "v1 1",
            "X-GA-SV": str(int(time.time())),
            "X-Unity-Version": "2018.4.12f1"
        }

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        timeout = aiohttp.ClientTimeout(total=5)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url, headers=headers, data=payload, ssl=ssl_context) as response:
                content = await response.read()

                if response.status != 200:
                    print(f"{Fore.RED}[MAJOR LOGIN] Status: {response.status}{Style.RESET_ALL}")
                    return None

                decoded = decode_protobuf(content[64:], raw_fields={22, 23})

                if 1 in decoded and 8 in decoded:
                    return decoded

                print(f"{Fore.CYAN}[MAJOR LOGIN]{Style.RESET_ALL} response: {Fore.GREEN}{json.dumps(decoded, indent=2, default=str)}{Style.RESET_ALL}")
                return None

    except asyncio.TimeoutError:
        print(f"{Fore.RED}[MAJOR LOGIN] TimeoutError{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}[MAJOR LOGIN] Exception: {e}{Style.RESET_ALL}")
        return None


async def get_login_data(payload, jwt_token, server_url, release_version):
    try:
        url = f"{server_url}/GetLoginData"
        headers = {
            "Accept": "*/*",
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/x-www-form-urlencoded",
            "ReleaseVersion": str(release_version),
            "User-Agent": "UnityPlayer/2018.4.12f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
            "X-GA": "v1 1",
            "X-GA-SV": str(int(time.time())),
            "X-Unity-Version": "2018.4.12f1"
        }

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        timeout = aiohttp.ClientTimeout(total=5)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(url, headers=headers, data=payload, ssl=ssl_context) as response:
                content = await response.read()

                if response.status != 200:
                    print(f"{Fore.RED}[LOGIN DATA] Status: {response.status}{Style.RESET_ALL}")
                    return None

                decoded = decode_protobuf(content, raw_fields={44})
                return decoded

    except asyncio.TimeoutError:
        print(f"{Fore.RED}[LOGIN DATA] TimeoutError{Style.RESET_ALL}")
        return None
    except Exception as e:
        print(f"{Fore.RED}[LOGIN DATA] Exception: {e}{Style.RESET_ALL}")
        return None


async def main(guest_uid=None, guest_password=None):
    global game_version, release_version, login_url, gop_url_1, gop_url_2, vercfg_sign, field_106
    global access_token, open_id, platform, account_id, region, jwt_token, server_url
    global timestamp, key, iv, stronghold_raw

    if guest_uid is None or guest_password is None:
        guest_uid, guest_password = load_account("account.json")
    if not guest_uid or not guest_password:
        print(f"{Fore.RED}[MAIN] Account load failed!{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} uid: {Fore.YELLOW}{guest_uid}{Style.RESET_ALL}")

    game_version, release_version, login_url, gop_url_1, gop_url_2, vercfg_sign, field_106 = await update()

    if not gop_url_1 or not login_url or not game_version:
        print(f"{Fore.RED}[MAIN] update() failed — network/DNS issue{Style.RESET_ALL}")
        return

    access_token, open_id, platform = await token_grant(guest_uid, guest_password, gop_url_1, game_version)

    if not access_token:
        print(f"{Fore.RED}[MAIN] Token grant failed!{Style.RESET_ALL}")
        return

    major_login_payload, login_data_payload = await get_payload(access_token, open_id, platform, game_version, field_106, vercfg_sign)

    major_login_response = await major_login(major_login_payload, login_url, release_version)

    if not major_login_response:
        print(f"{Fore.RED}[MAIN] MajorLogin failed!{Style.RESET_ALL}")
        return

    account_id    = major_login_response.get(1)
    region        = major_login_response.get(2)
    jwt_token     = major_login_response.get(8)
    server_url    = major_login_response.get(10)
    timestamp     = major_login_response.get(21)
    key           = major_login_response.get(22)
    iv            = major_login_response.get(23)
    stronghold_raw = major_login_response.get(16, "")

    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} account_id: {Fore.GREEN}{account_id}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} region: {Fore.GREEN}{region}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} server_url: {Fore.MAGENTA}{server_url}{Style.RESET_ALL}")

    login_data_response = await get_login_data(login_data_payload, jwt_token, server_url, release_version)

    if not login_data_response:
        print(f"{Fore.RED}[MAIN] GetLoginData failed!{Style.RESET_ALL}")
        return

    online_server = login_data_response.get(14)
    nickname      = login_data_response.get(4)
    level         = login_data_response.get(6)

    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} nickname: {Fore.GREEN}{nickname}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} level: {Fore.YELLOW}{level}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[MAIN]{Style.RESET_ALL} online_server: {Fore.MAGENTA}{online_server}{Style.RESET_ALL}")

    online_ip, online_port = online_server.split(":")

    auth_online = bytes.fromhex(build_auth_packet(account_id, jwt_token, timestamp, key, iv, 'online'))

    print(f"{Fore.GREEN}[MAIN] Connecting to online server — Solo Triple Wolves only{Style.RESET_ALL}")

    await tcp_online(online_ip, online_port, auth_online, key, iv)


async def run():
    try:
        print(f"{Fore.CYAN}[RUNNER] Starting bot...{Style.RESET_ALL}")
        await asyncio.wait_for(main(), timeout=6 * 60 * 60)
    except asyncio.TimeoutError:
        print(f"{Fore.YELLOW}[RUNNER] 6h reached — restarting process...{Style.RESET_ALL}")
    except asyncio.CancelledError:
        raise
    except Exception as e:
        print(f"{Fore.RED}[RUNNER] Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}[RUNNER] Restarting in 3s...{Style.RESET_ALL}")


if __name__ == '__main__':
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[RUNNER] Shutting down...{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[RUNNER] Goodbye! Bot stopped cleanly.{Style.RESET_ALL}")
        sys.exit(0)

    print(f"{Fore.YELLOW}[RUNNER] Restarting Python process...{Style.RESET_ALL}")
    os.execv(sys.executable, [sys.executable] + sys.argv)
