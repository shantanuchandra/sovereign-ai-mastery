#!/usr/bin/env python3
"""Bounded loopback-only HTTP probe; never an LLM benchmark."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import math
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import urlopen

def benchmark(base, requests=32, concurrency=1):
    url = urlsplit(base)
    if (url.scheme != 'http' or url.hostname != '127.0.0.1' or not url.port
        or url.username or url.password or url.path not in ('', '/') or url.query or url.fragment):
        raise ValueError('explicit IPv4 loopback HTTP base URL and port required')
    if type(requests) is not int or not 1 <= requests <= 1000:
        raise ValueError('requests must be 1 to 1000')
    if type(concurrency) is not int or not 1 <= concurrency <= 32:
        raise ValueError('concurrency must be 1 to 32')
    def one(_):
        start = time.perf_counter()
        try:
            with urlopen(base.rstrip('/') + '/work', timeout=5) as response:
                status = response.status
                body = json.loads(response.read(4096))
                if body.get('synthetic') is not True:
                    raise ValueError('not the course synthetic service')
        except HTTPError as error:
            status = error.code
            error.close()
        except (URLError, TimeoutError, OSError):
            status = 0
        return status, (time.perf_counter() - start) * 1000
    started = time.perf_counter()
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        rows = list(pool.map(one, range(requests)))
    elapsed = time.perf_counter() - started
    successes = sorted(ms for status, ms in rows if status == 200)
    return {
        'synthetic_http_only': True, 'requests': requests, 'concurrency': concurrency,
        'successes': len(successes), 'errors': requests - len(successes),
        'error_rate': (requests - len(successes)) / requests,
        'elapsed_seconds': round(elapsed, 6),
        'successful_rps': round(len(successes) / elapsed, 4),
        'successful_p95_ms': round(successes[math.ceil(.95 * len(successes)) - 1], 4) if successes else None,
        'limits': 'Nearest-rank p95 of successful requests only; read error rate alongside it. Fixed hash work plus explicit synthetic delay; no model or hardware-capacity claim.'
    }

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', default='http://127.0.0.1:8080')
    parser.add_argument('--requests', type=int, default=32)
    parser.add_argument('--concurrency', type=int, default=1)
    args = parser.parse_args()
    print(json.dumps(benchmark(args.base, args.requests, args.concurrency), indent=2))
