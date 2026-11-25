"""Adversarial tests for the fictional workflow register; no legal assurance."""
import copy
import json
from pathlib import Path
import unittest
from evaluate import evaluate_portfolio


class EvidenceGateTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path(__file__).with_name('cases.json').read_text())
        self.good = copy.deepcopy(self.data['workloads'][0])

    def evaluate(self, case):
        return evaluate_portfolio({'workloads': [case]})['results'][0]

    def test_complete_fictional_evidence_still_requires_review(self):
        result = self.evaluate(self.good)
        self.assertEqual(result['disposition'], 'REVIEW_REQUIRED')
        self.assertTrue(result['fictional_simulation'])

    def test_country_residency_does_not_satisfy_named_site(self):
        self.good['boundary'] = 'premises'
        self.good['flows'][0]['site'] = 'OTHER-SITE'
        self.assertEqual(self.evaluate(self.good)['disposition'], 'BLOCKED')

    def test_every_lifecycle_path_is_gated_independently(self):
        for i in range(len(self.good['flows'])):
            with self.subTest(path=self.good['flows'][i]['kind']):
                case = copy.deepcopy(self.good)
                case['boundary'] = 'premises'
                case['flows'][i]['site'] = 'OFFSITE-UAE'
                self.assertEqual(self.evaluate(case)['disposition'], 'BLOCKED')

    def test_airgap_forbids_inbound_activation_and_support_networks(self):
        for i in range(len(self.good['flows'])):
            case = copy.deepcopy(self.good)
            case['boundary'] = 'airgap'
            case['flows'][i]['network'] = True
            self.assertEqual(self.evaluate(case)['disposition'], 'BLOCKED')

    def test_unknown_destination_does_not_pass(self):
        self.good['flows'][0]['country'] = 'UNKNOWN'
        self.assertEqual(self.evaluate(self.good)['disposition'], 'UNVERIFIED')

    def test_missing_backup_is_unverified(self):
        self.good['flows'] = [x for x in self.good['flows'] if x['kind'] != 'backup']
        self.assertEqual(self.evaluate(self.good)['disposition'], 'UNVERIFIED')

    def test_contract_or_transfer_mechanism_does_not_override_boundary(self):
        self.good['flows'][0]['country'] = 'OUTSIDE'
        self.good['transfer_review'] = 'reviewed'
        self.assertEqual(self.evaluate(self.good)['disposition'], 'BLOCKED')

    def test_missing_or_rejected_legal_review_is_not_approval(self):
        self.good['legal_review'] = 'pending'
        self.assertEqual(self.evaluate(self.good)['disposition'], 'UNVERIFIED')
        self.good['legal_review'] = 'rejected'
        self.assertEqual(self.evaluate(self.good)['disposition'], 'BLOCKED')

    def test_recorded_test_failure_blocks_even_if_all_reviews_complete(self):
        self.good['flows'][0]['observation']['outcome'] = 'fail'
        self.assertEqual(self.evaluate(self.good)['disposition'], 'BLOCKED')

    def test_claimed_review_without_provenance_is_unverified(self):
        self.good['review_record']['reference'] = ''
        self.assertEqual(self.evaluate(self.good)['disposition'], 'UNVERIFIED')
        self.good['flows'][0]['observation']['evidence'] = ''
        self.assertEqual(self.evaluate(self.good)['disposition'], 'UNVERIFIED')

    def test_invalid_schema_and_duplicate_ids_fail_closed(self):
        for mutate in (
            lambda c: c.update(boundary='magic'),
            lambda c: c['flows'][0].update(network='false'),
            lambda c: c['flows'][0].update(kind='unrecognised'),
            lambda c: c['flows'].append(copy.deepcopy(c['flows'][0])),
            lambda c: c.update(legal_review='approved-by-score'),
        ):
            case = copy.deepcopy(self.good)
            mutate(case)
            with self.assertRaises(ValueError):
                self.evaluate(case)
        with self.assertRaises(ValueError):
            evaluate_portfolio({'workloads': [self.good, self.good]})

    def test_expected_scenario_dispositions(self):
        report = evaluate_portfolio(self.data)
        self.assertEqual({r['id']: r['disposition'] for r in report['results']},
                         self.data['expected'])


if __name__ == '__main__':
    unittest.main()
