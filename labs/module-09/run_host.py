#!/usr/bin/env python3
"""Run/probe an owned loopback service and shut it down; no Docker or downloads."""
import json
import platform
from threading import Thread
from bench import benchmark
from service import make_server

def main():
    server = make_server()
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        base = f'http://127.0.0.1:{server.server_port}'
        profiles = [benchmark(base, 32, c) for c in (1, 8)]
        assert profiles[0]['successes'] == 32
        report = {'environment': 'native Python CPU only', 'python': platform.python_version(),
                  'machine': platform.machine(), 'profiles': profiles}
    finally:
        server.shutdown();server.server_close();thread.join()
    report['owned_service_stopped'] = True
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
