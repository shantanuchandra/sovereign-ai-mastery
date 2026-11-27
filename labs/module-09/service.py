#!/usr/bin/env python3
"""Synthetic CPU HTTP service. No model, customer input, persistence or external calls."""
import argparse
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from threading import BoundedSemaphore
import time

class Handler(BaseHTTPRequestHandler):
    server_version = 'CourseSyntheticService'
    sys_version = ''

    def log_message(self, *_):
        pass

    def reply(self, status, body):
        content = json.dumps(body).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self):
        if self.path == '/health':
            return self.reply(200, {'synthetic': True, 'ready': True})
        if self.path != '/work':
            return self.reply(404, {'error': 'unknown synthetic route'})
        if not self.server.capacity.acquire(blocking=False):
            return self.reply(503, {'error': 'synthetic concurrency limit'})
        try:
            value = b'invented-factory-fixture'
            for _ in range(1000):
                value = hashlib.sha256(value).digest()
            time.sleep(self.server.delay_ms / 1000)
            self.reply(200, {'synthetic': True, 'result': value.hex()})
        finally:
            self.server.capacity.release()

def make_server(port=0, workers=2, delay_ms=10):
    if type(port) is not int or not 0 <= port <= 65535:
        raise ValueError('valid local port required')
    if type(workers) is not int or not 1 <= workers <= 16:
        raise ValueError('workers must be an integer from 1 to 16')
    if type(delay_ms) is not int or not 0 <= delay_ms <= 100:
        raise ValueError('synthetic delay must be 0 to 100 ms')
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    server.daemon_threads = True
    server.capacity = BoundedSemaphore(workers)
    server.delay_ms = delay_ms
    return server

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8080)
    parser.add_argument('--workers', type=int, default=2)
    parser.add_argument('--delay-ms', type=int, default=10)
    args = parser.parse_args()
    server = make_server(args.port, args.workers, args.delay_ms)
    print(json.dumps({'synthetic': True, 'host': '127.0.0.1', 'port': server.server_port}), flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
