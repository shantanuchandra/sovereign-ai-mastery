import copy
import json
import unittest
from pathlib import Path
from discovery import ARTIFACTS, evaluate, fixtures, run

class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.c = fixtures()[0]
    def test_complete(self):
        r = evaluate(self.c)
        self.assertEqual(r['state'], 'ELIGIBLE_FOR_DISCOVERY')
        self.assertEqual(r['desirability'], 3.15)
    def test_fixture_states(self):
        self.assertEqual([r['state'] for r in run()['results']], ['ELIGIBLE_FOR_DISCOVERY','UNKNOWN','ELIGIBLE_FOR_DISCOVERY','BLOCKED','BLOCKED'])
    def test_no_mutation(self):
        original = copy.deepcopy(self.c)
        evaluate(self.c)
        self.assertEqual(original, self.c)
    def test_missing_each_evidence(self):
        for key in self.c['evidence']:
            with self.subTest(key=key):
                c = copy.deepcopy(self.c); del c['evidence'][key]
                self.assertEqual(evaluate(c)['state'], 'UNKNOWN')
                self.assertIsNone(evaluate(c)['desirability'])
    def test_contradictions_dominate(self):
        for key in self.c['evidence']:
            c = copy.deepcopy(self.c); c['evidence'][key]['state']='contradicted'; c['scores']={}
            self.assertEqual(evaluate(c)['state'], 'BLOCKED')
    def test_external_each_path(self):
        for artifact in (*ARTIFACTS, 'diagnostics-extra'):
            c = copy.deepcopy(self.c); c['proposal']['paths'][artifact]='other-uae-site'; c['evidence']={}
            self.assertEqual(evaluate(c)['state'], 'BLOCKED')
    def test_missing_each_path(self):
        for artifact in ARTIFACTS:
            c = copy.deepcopy(self.c); del c['proposal']['paths'][artifact]
            self.assertEqual(evaluate(c)['state'], 'UNKNOWN')
    def test_external_operator_malformed_paths(self):
        self.c['proposal'].update(paths=[], operator='remote')
        self.assertEqual(evaluate(self.c)['state'], 'BLOCKED')
    def test_airgap_network_malformed_paths(self):
        self.c.update(boundary='airgap'); self.c['proposal'].update(paths=None, network='internet')
        self.assertEqual(evaluate(self.c)['state'], 'BLOCKED')
    def test_airgap_reviews(self):
        for key in ('offline_update_review','media_review'):
            self.c.update(boundary='airgap'); self.c['proposal'].update(network='disconnected'); self.c['proposal'][key]=False
            self.assertEqual(evaluate(self.c)['state'], 'BLOCKED')
    def test_airgap_complete(self):
        self.c.update(boundary='airgap'); self.c['proposal'].update(network='disconnected', offline_update_review=True, media_review=True)
        self.assertEqual(evaluate(self.c)['state'], 'ELIGIBLE_FOR_DISCOVERY')
    def test_invalid_numbers(self):
        for x in (True, False, float('nan'), float('inf'), -1, 6, '5', None):
            self.c['scores']['value']['value']=x
            self.assertEqual(evaluate(self.c)['state'], 'UNKNOWN')
    def test_score_requires_reference(self):
        self.c['scores']['value']['evidence']='invented'
        self.assertIsNone(evaluate(self.c)['desirability'])
    def test_provenance_required(self):
        for key in ('source','checked','owner'):
            c=copy.deepcopy(self.c); c['evidence']['pain'][key]=''
            self.assertEqual(evaluate(c)['state'], 'UNKNOWN')
    def test_unknown_not_zero(self):
        self.c['scores']['value']['value']=None
        self.assertIsNone(evaluate(self.c)['desirability'])
    def test_necessity_not_desirability(self):
        before=evaluate(self.c)['desirability']; self.c['necessity']='preferred'
        self.assertEqual(evaluate(self.c)['desirability'],before)
    def test_region_rejection(self):
        self.c.update(boundary='approved-region'); self.c['proposal']['region_review']=False
        self.assertEqual(evaluate(self.c)['state'],'BLOCKED')
    def test_malformed(self):
        for key in ('proposal','evidence','scores','boundary'):
            c=copy.deepcopy(self.c); c[key]=None
            self.assertEqual(evaluate(c)['state'],'UNKNOWN')
    def test_malformed_sovereignty_record(self):
        self.c["evidence"]["sovereignty"] = []
        self.assertEqual(evaluate(self.c)["state"], "UNKNOWN")
    def test_extreme_scores_do_not_override_conflict(self):
        self.c["proposal"]["paths"]["telemetry"] = "external"
        for value in self.c["scores"].values(): value["value"] = 5
        self.assertEqual(evaluate(self.c)["state"], "BLOCKED")
        self.assertIsNone(evaluate(self.c)["desirability"])
    def test_activation_with_missing_paths(self):
        self.c["proposal"]["paths"] = {"activation": "external"}
        self.assertEqual(evaluate(self.c)["state"], "BLOCKED")
    def test_malformed_extra_path_with_conflict(self):
        self.c["proposal"]["paths"].update(extra=[], telemetry="external")
        self.assertEqual(evaluate(self.c)["state"], "BLOCKED")
    def test_malformed_extra_path(self):
        self.c["proposal"]["paths"]["extra"] = []
        self.assertEqual(evaluate(self.c)["state"], "UNKNOWN")
    def test_malformed_boundary_list(self):
        self.c["boundary"] = []
        self.assertEqual(evaluate(self.c)["state"], "UNKNOWN")
    def test_huge_integers_are_unknown(self):
        for value in (10**400, -(10**400)):
            with self.subTest(value_sign=value > 0):
                c = copy.deepcopy(self.c)
                c['scores']['value']['value'] = value
                result = evaluate(c)
                self.assertEqual(result['state'], 'UNKNOWN')
                self.assertIsNone(result['desirability'])
    def test_huge_integers_preserve_known_conflict(self):
        for value in (10**400, -(10**400)):
            with self.subTest(value_sign=value > 0):
                c = copy.deepcopy(self.c)
                c['scores']['value']['value'] = value
                c['proposal']['paths']['telemetry'] = 'external'
                result = evaluate(c)
                self.assertEqual(result['state'], 'BLOCKED')
                self.assertIn('external:telemetry', result['conflicts'])
                self.assertIsNone(result['desirability'])
    def test_top_level_non_dict_is_unknown(self):
        for value in (None, [], 'invalid', 42, True):
            with self.subTest(value=value):
                result = evaluate(value)
                self.assertEqual(result['state'], 'UNKNOWN')
                self.assertIn('case:invalid', result['unknowns'])
                self.assertIsNone(result['desirability'])
    def test_retained_actual_run(self):
        self.assertEqual(run(),json.loads(Path(__file__).with_name('observed-discovery-run.json').read_text()))

if __name__=='__main__': unittest.main()
