#!/usr/bin/env python3
"""W028 controlled-origin backend for W027. Standard-library only; research harness, not production."""
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json, pathlib, threading

ROOT = pathlib.Path(__file__).resolve().parent
HARNESS = ROOT / "W027-true-origin-execution-harness.html"
OPS = {}
LOCK = threading.Lock()

class Handler(BaseHTTPRequestHandler):
    def send_json(self, code, payload):
        body=json.dumps(payload).encode()
        self.send_response(code); self.send_header("Content-Type","application/json")
        self.send_header("Cache-Control","no-store"); self.send_header("Content-Length",str(len(body)))
        self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        u=urlparse(self.path)
        if u.path in ("/", "/w027"):
            body=HARNESS.read_bytes(); self.send_response(200); self.send_header("Content-Type","text/html; charset=utf-8"); self.send_header("Content-Length",str(len(body))); self.end_headers(); self.wfile.write(body); return
        if u.path=="/w027/status":
            op=parse_qs(u.query).get("id", [None])[0]
            with LOCK: value=OPS.get(op) if op else (OPS[list(OPS)[-1]] if OPS else None)
            return self.send_json(200,{"state":"confirmed","record":value} if value else {"state":"not-found"})
        return self.send_json(404,{"state":"not-found"})
    def do_POST(self):
        u=urlparse(self.path); q=parse_qs(u.query); op=q.get("id",[None])[0]; mode=q.get("mode",["confirm"])[0]
        if u.path!="/w027/operation" or not op: return self.send_json(400,{"state":"known-failure","reason":"missing operation id"})
        if mode=="reject": return self.send_json(422,{"state":"known-failure","operationId":op})
        if mode=="drop-before": self.close_connection=True; return
        with LOCK: OPS[op]={"operationId":op,"committed":True}
        if mode=="drop-after": self.close_connection=True; return
        return self.send_json(200,{"state":"confirmed","operationId":op})

if __name__=="__main__":
    print("W028 controlled origin: http://127.0.0.1:8028/w027")
    ThreadingHTTPServer(("127.0.0.1",8028),Handler).serve_forever()
