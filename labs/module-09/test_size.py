import copy
import json
from pathlib import Path
import unittest
from size import estimate

class CapacityTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads(Path(__file__).with_name('factory.json').read_text())
    def result(self, **changes):
        return estimate({**self.case, **changes})
    def test_fixture_arithmetic_and_assumption_state(self):
        r = self.result()
        self.assertEqual(r['state'], 'UNVERIFIED')
        self.assertEqual(r['kv_gib'], 2)
        self.assertAlmostEqual(r['weights_gib'], 3.2596, places=4)
        self.assertEqual(r['required_installed_replicas'], 2)
        self.assertEqual(r['monthly_energy_cost'], 18)
        self.assertEqual(r['cost_per_1000_successes'], 20.18)
    def test_favorable_declared_test_only_requires_review(self):
        self.assertEqual(self.result(profile_evidence='deployment_test')['state'], 'REVIEW_REQUIRED')
    def test_memory_budget_blocks(self):
        self.assertEqual(self.result(available_memory_gib=4)['state'], 'BLOCKED')
    def test_context_and_concurrency_increase_kv(self):
        self.assertEqual(self.result(context_tokens=8192)['kv_gib'], 4)
        self.assertEqual(self.result(concurrent_sequences=8)['kv_gib'], 4)
    def test_spare_failure_budget_is_not_optional_in_arithmetic(self):
        self.assertEqual(self.result(installed_replicas=1)['state'], 'BLOCKED')
        self.assertEqual(self.result(arrival_rps=4)['required_installed_replicas'], 3)
    def test_site_conflict_survives_favorable_performance(self):
        self.assertEqual(self.result(compute_site='OFFSITE', profile_evidence='deployment_test')['state'], 'BLOCKED')
    def test_country_conflict_blocks(self):
        self.assertEqual(self.result(compute_country='OTHER')['state'], 'BLOCKED')
    def test_airgap_rejects_external_runtime_dependency(self):
        self.assertEqual(self.result(external_network_dependencies=True)['state'], 'BLOCKED')
    def test_every_lifecycle_route_remains_protected(self):
        for i in range(len(self.case['routes'])):
            c = copy.deepcopy(self.case);c['routes'][i]['site'] = 'OFFSITE'
            self.assertEqual(estimate(c)['state'], 'BLOCKED', c['routes'][i]['id'])
    def test_network_route_conflict(self):
        self.case['routes'][0]['network'] = True
        self.assertEqual(estimate(self.case)['state'], 'BLOCKED')
    def test_connected_mode_does_not_relax_site(self):
        self.case['physical_airgap'] = False
        self.case['routes'][0].update(site='OFFSITE', network=True)
        self.assertEqual(estimate(self.case)['state'], 'BLOCKED')
    def test_missing_routes_are_unknown(self):
        self.assertEqual(self.result(routes=[], profile_evidence='synthetic_test')['state'], 'UNVERIFIED')
    def test_unknown_and_duplicate_cannot_hide_conflicts(self):
        self.case['routes'] += [dict(id='unknown', site='OFFSITE', country='UAE', network=True), dict(self.case['routes'][0])]
        r = estimate(self.case)
        self.assertEqual(r['state'], 'BLOCKED')
        self.assertTrue(any('Unclassified' in x for x in r['gaps']))
        self.assertTrue(any('Duplicate' in x for x in r['gaps']))
    def test_stale_profile_needs_new_evidence(self):
        self.assertEqual(self.result(profile_evidence='deployment_test', profile_build='old')['state'], 'UNVERIFIED')
    def test_slo_failures_block_even_with_review_label(self):
        for change in [dict(p95_ms=300), dict(error_rate=.1)]:
            self.assertEqual(self.result(profile_evidence='deployment_test', **change)['state'], 'BLOCKED')
    def test_boolean_nan_and_infinity_are_not_numbers(self):
        for value in [True, float('nan'), float('inf'), 10**1000, '12']:
            with self.assertRaises(ValueError):
                self.result(available_memory_gib=value)
    def test_zero_divisors_ranges_and_fractional_counts(self):
        for change in [dict(profile_rps=0), dict(target_utilization=1), dict(monthly_successful_requests=0), dict(context_tokens=1.5), dict(spare_replicas=-1), dict(headroom_fraction=-.2)]:
            with self.assertRaises(ValueError):
                self.result(**change)
    def test_malformed_policies_and_routes(self):
        for change in [dict(physical_airgap='false'), dict(required_site=''), dict(routes=[False]), dict(profile_evidence='certified')]:
            with self.assertRaises(ValueError):
                self.result(**change)

if __name__ == '__main__':
    unittest.main()
