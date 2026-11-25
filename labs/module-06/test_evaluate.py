"""Synthetic decision regression tests, not assurance of a real AI system."""
import copy
import json
from pathlib import Path
import unittest
from evaluate import evaluate, LIFECYCLE

class GovernanceTests(unittest.TestCase):
    def setUp(self):
        self.case=json.loads(Path(__file__).with_name('cases.json').read_text())[0]
    def test_complete_record_still_requires_review(self):
        self.assertEqual(evaluate(self.case)['status'],'REVIEW_REQUIRED')
    def test_aggregate_does_not_hide_language_failure(self):
        self.case['groups']=[{'id':'en','n':9800,'errors':98},{'id':'ar','n':200,'errors':60}]
        r=evaluate(self.case)
        self.assertAlmostEqual(r['aggregate_error'],.0158)
        self.assertIn('group_error:ar',r['blockers'])
        self.assertIn('group_disparity',r['blockers'])
    def test_all_lifecycle_paths_enforce_physical_site(self):
        for kind in LIFECYCLE:
            with self.subTest(kind=kind):
                c=copy.deepcopy(self.case)
                next(f for f in c['flows'] if f['kind']==kind)['site']='OTHER-SITE'
                self.assertIn('site:'+kind,evaluate(c)['blockers'])
    def test_airgap_forbids_each_network_path(self):
        for kind in LIFECYCLE:
            with self.subTest(kind=kind):
                c=copy.deepcopy(self.case);c['boundary']='airgap'
                next(f for f in c['flows'] if f['kind']==kind)['network']=True
                self.assertIn('network:'+kind,evaluate(c)['blockers'])
    def test_missing_flow_is_unverified(self):
        self.case['flows'].pop()
        self.assertEqual(evaluate(self.case)['status'],'UNVERIFIED')
    def test_country_scope_is_distinct_from_site_scope(self):
        self.case['boundary']='country';self.case['flows'][0]['site']='OTHER-SITE'
        self.assertEqual(evaluate(self.case)['status'],'REVIEW_REQUIRED')
        self.case['flows'][0]['country']='OTHER-COUNTRY'
        self.assertEqual(evaluate(self.case)['status'],'BLOCKED')
    def test_out_of_intended_use_blocks(self):
        self.case['intended_use']='automatic_machine_control'
        self.assertIn('intended_use',evaluate(self.case)['blockers'])
    def test_small_or_zero_sample_is_not_a_pass(self):
        for n in [0,5]:
            self.case['groups'][0].update(n=n,errors=0)
            self.assertEqual(evaluate(self.case)['status'],'UNVERIFIED')
    def test_numeric_and_type_attacks_are_gaps(self):
        for v in [True,-1,'100',float('nan'),float('inf')]:
            with self.subTest(value=v):
                c=copy.deepcopy(self.case);c['groups'][0]['n']=v
                self.assertEqual(evaluate(c)['status'],'UNVERIFIED')
        for value in [True,float('nan'),float('inf'),10**1000,'0.10']:
            c=copy.deepcopy(self.case);c['criteria']['error_limit']=value
            self.assertEqual(evaluate(c)['status'],'UNVERIFIED')
        for obj in [None,[],42,True]:
            self.assertEqual(evaluate(obj)['status'],'UNVERIFIED')
    def test_duplicates_and_impossible_counts_are_gaps(self):
        for mutation in ['group','flow','control','count']:
            c=copy.deepcopy(self.case)
            if mutation=='count':c['groups'][0]['errors']=1000
            else:
                field={'group':'groups','flow':'flows','control':'controls'}[mutation]
                c[field].append(copy.deepcopy(c[field][0]))
            self.assertEqual(evaluate(c)['status'],'UNVERIFIED')
            if mutation in ('group','count'):self.assertIsNone(evaluate(c)['aggregate_error'])
    def test_stale_build_missing_provenance_and_future_date_are_gaps(self):
        for field,value in [('build_id','old'),('evidence',''),('date','2099-01-01'),('date','not-a-date')]:
            c=copy.deepcopy(self.case);c['controls'][0][field]=value
            self.assertEqual(evaluate(c)['status'],'UNVERIFIED')
    def test_control_failure_and_incident_block(self):
        self.case['controls'][0]['outcome']='fail'
        self.assertEqual(evaluate(self.case)['status'],'BLOCKED')
        self.case['incident_open']=True
        self.assertIn('open_incident',evaluate(self.case)['blockers'])
    def test_separation_and_owner_gaps(self):
        self.case['roles']['validator']=self.case['roles']['responsible']
        self.assertIn('role_separation',evaluate(self.case)['gaps'])
        self.case['roles']['accountable']=''
        self.assertIn('role:accountable',evaluate(self.case)['gaps'])
    def test_known_violation_survives_missing_data_and_acceptance(self):
        self.case['incident_open']=True;self.case['groups']=None
        self.case['risk_acceptance']='CEO approved'
        self.assertEqual(evaluate(self.case)['status'],'BLOCKED')
    def test_no_mutation_or_production_pass(self):
        original=copy.deepcopy(self.case);r=evaluate(self.case)
        self.assertEqual(original,self.case)
        self.assertIn('not production assurance',r['limits'])
    def test_case_manifest_has_declared_expected_statuses(self):
        cases=json.loads(Path(__file__).with_name('cases.json').read_text())
        self.assertGreaterEqual(len(cases),14)
        self.assertEqual(len({c['id'] for c in cases}),len(cases))
        for c in cases:
            self.assertEqual(evaluate(c)['status'],c['expected_status'],c['id'])

if __name__=='__main__':unittest.main()
