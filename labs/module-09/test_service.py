from threading import Thread
from urllib.error import HTTPError
from urllib.request import urlopen
import unittest
from unittest.mock import patch
from run_container import require_local_engine
from bench import benchmark
from service import make_server

class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.server = make_server(workers=1)
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.base = f'http://127.0.0.1:{self.server.server_port}'
    def tearDown(self):
        self.server.shutdown();self.server.server_close();self.thread.join()
    def test_actual_loopback_successful_probe(self):
        r = benchmark(self.base, 8, 1)
        self.assertEqual((r['requests'], r['successes'], r['errors']), (8, 8, 0))
        self.assertGreater(r['successful_rps'], 0)
        self.assertGreaterEqual(r['successful_p95_ms'], 0)
    def test_overload_errors_are_counted_without_fake_latency(self):
        self.server.capacity.acquire()
        try:
            r = benchmark(self.base, 4, 2)
            self.assertEqual((r['successes'], r['errors']), (0, 4))
            self.assertEqual(r['error_rate'], 1)
            self.assertIsNone(r['successful_p95_ms'])
        finally:
            self.server.capacity.release()
    def test_health_does_not_prove_work_capacity(self):
        self.server.capacity.acquire()
        try:
            self.assertEqual(urlopen(self.base + '/health').status, 200)
            with self.assertRaises(HTTPError) as error:
                urlopen(self.base + '/work')
            self.assertEqual(error.exception.code, 503)
        finally:
            self.server.capacity.release()
    def test_unknown_route_rejected(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(self.base + '/customer-data')
        self.assertEqual(error.exception.code, 404)
    def test_probe_rejects_remote_or_unbounded_requests(self):
        for base in ['https://example.com', 'http://localhost:8080', 'http://127.0.0.1:8080/?q=secret']:
            with self.assertRaises(ValueError):
                benchmark(base)
        for args in [dict(requests=True), dict(requests=1001), dict(concurrency=33)]:
            with self.assertRaises(ValueError):
                benchmark(self.base, **args)
    def test_container_runner_rejects_remote_targets_before_contact(self):
        with patch.dict('os.environ', {'DOCKER_HOST': 'ssh://remote.example'}, clear=True), patch('run_container.command') as command:
            with self.assertRaises(ValueError):
                require_local_engine()
            command.assert_not_called()
        with patch.dict('os.environ', {}, clear=True), patch('run_container.command', return_value='tcp://remote.example:2375'):
            with self.assertRaises(ValueError):
                require_local_engine()

        with patch.dict('os.environ', {'DOCKER_CONTEXT':'remote', 'DOCKER_HOST':'unix:///var/run/docker.sock'}, clear=True), patch('run_container.command', return_value='ssh://remote.example') as command:
            with self.assertRaises(ValueError):
                require_local_engine()
            self.assertEqual(command.call_args.args[-1], 'remote')

    def test_service_configuration_is_bounded(self):
        for args in [dict(workers=0), dict(port=-1), dict(delay_ms=101)]:
            with self.assertRaises(ValueError):
                make_server(**args)

if __name__ == '__main__':
    unittest.main()
