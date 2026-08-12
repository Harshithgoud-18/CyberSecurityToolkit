"""Vercel serverless entry point for the deployable toolkit features."""

from __future__ import annotations

import hashlib

from flask import Flask, jsonify, request

import password_checker


app = Flask(__name__)
MAX_UPLOAD_BYTES = 5 * 1024 * 1024


@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Cache-Control"] = "no-store"
    return response


def uploaded_bytes(field_name: str) -> bytes:
    uploaded = request.files.get(field_name)
    if uploaded is None or not uploaded.filename:
        raise ValueError(f"Upload a file for '{field_name}'.")
    content = uploaded.read(MAX_UPLOAD_BYTES + 1)
    if len(content) > MAX_UPLOAD_BYTES:
        raise ValueError("Files must be 5 MB or smaller.")
    return content


@app.errorhandler(ValueError)
def handle_value_error(error):
    return jsonify(error=str(error)), 400


@app.get("/")
def home():
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Cyber Security Toolkit</title><style>
:root{color-scheme:dark;font-family:system-ui,sans-serif;background:#0e1117;color:#e6edf3}body{max-width:900px;margin:2rem auto;padding:0 1rem}h1{margin-bottom:.25rem}p{color:#a9b4c2}section{background:#161b22;border:1px solid #30363d;border-radius:12px;padding:1.2rem;margin:1rem 0}input,textarea,button{font:inherit;padding:.65rem;border-radius:7px;border:1px solid #475569}input,textarea{background:#0d1117;color:#e6edf3;width:min(100%,600px);box-sizing:border-box}textarea{min-height:90px}button{background:#238636;color:#fff;cursor:pointer;margin-top:.6rem}pre{overflow:auto;white-space:pre-wrap;background:#0d1117;padding:.8rem;border-radius:7px}small{color:#9ca3af}</style></head><body>
<h1>🔐 Cyber Security Toolkit</h1><p>Serverless edition for Vercel. Files are processed only for the current request and are not stored.</p>
<section><h2>Password Strength</h2><input id="password" type="password" placeholder="Enter a password"><br><button onclick="passwordCheck()">Check password</button><pre id="password-result"></pre></section>
<section><h2>SHA-256 Text Hash</h2><textarea id="text" placeholder="Enter text"></textarea><br><button onclick="textHash()">Generate hash</button><pre id="text-result"></pre></section>
<section><h2>File SHA-256 / Compare</h2><input id="file-one" type="file"><br><input id="file-two" type="file"><br><button onclick="fileHash()">Hash first file</button> <button onclick="compareFiles()">Compare files</button><pre id="file-result"></pre><small>Maximum upload size: 5 MB per file.</small></section>
<section><h2>Log Analyzer</h2><input id="log-file" type="file" accept=".log,.txt,text/plain"><br><button onclick="analyzeLog()">Analyze log</button><pre id="log-result"></pre></section>
<section><h2>Deployment limitations</h2><p>Packet capture, port/vulnerability scanning, and persistent password/encryption-key storage are intentionally unavailable in this public serverless deployment. They require privileged networking or durable private storage.</p></section>
<script>
async function post(path, body){const r=await fetch(path,{method:'POST',body});const d=await r.json();if(!r.ok)throw Error(d.error||'Request failed');return d}
function output(id,data){document.getElementById(id).textContent=typeof data==='string'?data:JSON.stringify(data,null,2)}
async function passwordCheck(){try{output('password-result',await post('/tool/password',new URLSearchParams({password:document.getElementById('password').value})))}catch(e){output('password-result',e.message)}}
async function textHash(){try{output('text-result',await post('/tool/text-hash',new URLSearchParams({text:document.getElementById('text').value})))}catch(e){output('text-result',e.message)}}
async function fileHash(){try{const f=document.getElementById('file-one').files[0],d=new FormData();d.append('file',f);output('file-result',await post('/tool/file-hash',d))}catch(e){output('file-result',e.message)}}
async function compareFiles(){try{const a=document.getElementById('file-one').files[0],b=document.getElementById('file-two').files[0],d=new FormData();d.append('first',a);d.append('second',b);output('file-result',await post('/tool/compare-files',d))}catch(e){output('file-result',e.message)}}
async function analyzeLog(){try{const f=document.getElementById('log-file').files[0],d=new FormData();d.append('file',f);output('log-result',await post('/tool/log-analyzer',d))}catch(e){output('log-result',e.message)}}
</script></body></html>"""


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.post("/tool/password")
def password_strength():
    password = request.form.get("password", "")
    if not password:
        raise ValueError("Enter a password.")
    return jsonify(strength=password_checker.check_password(password), common_password=password_checker.common_password(password), suggestions=password_checker.password_suggestion(password))


@app.post("/tool/text-hash")
def text_hash():
    text = request.form.get("text", "")
    if not text:
        raise ValueError("Enter text to hash.")
    return jsonify(sha256=hashlib.sha256(text.encode("utf-8")).hexdigest())


@app.post("/tool/file-hash")
def file_hash():
    return jsonify(sha256=hashlib.sha256(uploaded_bytes("file")).hexdigest())


@app.post("/tool/compare-files")
def compare_files():
    first = hashlib.sha256(uploaded_bytes("first")).hexdigest()
    second = hashlib.sha256(uploaded_bytes("second")).hexdigest()
    return jsonify(identical=first == second, first_sha256=first, second_sha256=second)


@app.post("/tool/log-analyzer")
def log_analyzer():
    text = uploaded_bytes("file").decode("utf-8", errors="replace")
    return jsonify(info=sum("INFO" in line for line in text.splitlines()), warning=sum("WARNING" in line for line in text.splitlines()), error=sum("ERROR" in line for line in text.splitlines()))
