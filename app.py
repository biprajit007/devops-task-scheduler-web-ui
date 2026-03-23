#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import json, os, subprocess
TASKS_FILE='tasks.json'
def load_tasks(): return json.load(open(TASKS_FILE)) if os.path.exists(TASKS_FILE) else []
def save_tasks(tasks): json.dump(tasks, open(TASKS_FILE,'w'), indent=2)
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        tasks=load_tasks(); rows=''.join(f"<tr><td>{t['name']}</td><td>{t['command']}</td><td>{t.get('last_run','never')}</td></tr>" for t in tasks)
        body=f"<html><body><h1>Task Scheduler</h1><form method='post'>Name <input name='name'> Command <input name='command'><button>Add</button></form><table border='1'><tr><th>Name</th><th>Command</th><th>Last Run</th></tr>{rows}</table></body></html>"
        self.send_response(200); self.end_headers(); self.wfile.write(body.encode())
    def do_POST(self):
        length=int(self.headers['Content-Length']); data=parse_qs(self.rfile.read(length).decode()); tasks=load_tasks()
        tasks.append({'name': data['name'][0], 'command': data['command'][0]}); save_tasks(tasks)
        self.send_response(303); self.send_header('Location','/'); self.end_headers()
HTTPServer(('0.0.0.0', 8080), H).serve_forever()
