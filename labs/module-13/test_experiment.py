import copy
import json
import math
import tempfile
import unittest
from pathlib import Path
from experiment import FILES,MODEL,REVISION,decide,digest,summarize,validate_record,verify_manifest

HERE=Path(__file__).parent

class MeasurementTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.record=json.loads((HERE/'observed-local-run.json').read_text())
        cls.cases=json.loads((HERE/'cases.json').read_text())
    def invalid(self,change):
        r=copy.deepcopy(self.record);change(r)
        with self.assertRaises((ValueError,TypeError,KeyError)): validate_record(r,self.cases)
    def test_retained_record_is_consistent(self): self.assertEqual(set(validate_record(self.record,self.cases)),{'1','2'})
    def test_exact_matrix_has_48_observations(self): self.assertEqual(len(self.record['rows']),48)
    def test_language_denominators_not_repeats(self):
        for p in self.record['summary'].values():
            self.assertEqual(p['slices']['en']['unique_cases'],4)
            self.assertEqual(p['slices']['ar']['unique_cases'],4)
    def test_missing_arabic_rejected(self): self.invalid(lambda r:r.update(rows=[x for x in r['rows'] if x['language']=='en']))
    def test_duplicate_rejected(self): self.invalid(lambda r:r['rows'].__setitem__(1,copy.deepcopy(r['rows'][0])))
    def test_nan_duration_rejected(self): self.invalid(lambda r:r['rows'][0].update(seconds=math.nan))
    def test_negative_duration_rejected(self): self.invalid(lambda r:r['rows'][0].update(seconds=-1))
    def test_zero_duration_rejected(self): self.invalid(lambda r:r['rows'][0].update(seconds=0))
    def test_boolean_duration_rejected(self): self.invalid(lambda r:r['rows'][0].update(seconds=True))
    def test_extra_tokens_rejected(self): self.invalid(lambda r:r['rows'][0].update(generated_tokens=25))
    def test_unknown_case_rejected(self): self.invalid(lambda r:r['rows'][0].update(id='invented'))
    def test_changed_prompt_rejected(self): self.invalid(lambda r:r['rows'][0].update(prompt='changed'))
    def test_changed_expected_rejected(self): self.invalid(lambda r:r['rows'][0].update(expected='changed'))
    def test_favourable_invented_summary_rejected(self): self.invalid(lambda r:r['summary']['1']['slices']['ar'].update(passed_measurements=12))
    def test_unrecorded_dtype_rejected(self): self.invalid(lambda r:r['settings'].update(dtype='int4'))
    def test_cpu_version_suffix_retained(self):
        r=copy.deepcopy(self.record);r['torch']='2.9.1+cpu'
        self.assertTrue(validate_record(r,self.cases))
    def test_wrong_base_cpu_version_rejected(self): self.invalid(lambda r:r.update(torch='2.10.0+cpu'))
    def test_nonfinite_load_rejected(self): self.invalid(lambda r:r['load_seconds'].update({'1':math.inf}))
    def test_missing_load_profile_rejected(self): self.invalid(lambda r:r['load_seconds'].pop('2'))
    def test_unrecorded_runtime_rejected(self): self.invalid(lambda r:r.update(torch='new'))
    def test_claimed_approval_rejected(self): self.invalid(lambda r:r.update(status='APPROVED'))
    def test_wrong_revision_rejected(self): self.invalid(lambda r:r.update(revision='main'))
    def test_wrong_hash_rejected(self): self.invalid(lambda r:r['artifact_hashes'].update({'config.json':'bad'}))
    def test_naive_timestamp_rejected(self): self.invalid(lambda r:r.update(started_utc='2026-11-28T10:00:00'))
    def test_os_isolation_overclaim_rejected(self): self.invalid(lambda r:r.update(network_guard='physical air gap'))
    def test_unknown_thread_rejected(self): self.invalid(lambda r:r['rows'][0].update(threads=8))
    def test_boolean_thread_rejected(self): self.invalid(lambda r:r['rows'][0].update(threads=True))
    def test_baseline_and_tuned_summary_are_raw_derived(self): self.assertEqual(summarize(self.record['rows']),self.record['summary'])
    def candidate(self):
        r=copy.deepcopy(self.record['rows'])
        for row in r:row['output']=row['expected']
        return dict(site='BANK-A',network=False,remote_operator=False,rights_review=True,dataset_review=True,quality_review=True,rollback_test=True,rows=r)
    def test_favourable_fixture_requires_review(self): self.assertEqual(decide(self.candidate())['status'],'REVIEW_REQUIRED')
    def test_site_conflict_dominates_missing_review(self):
        c=self.candidate();c.update(site='UAE-CLOUD',rights_review=None)
        d=decide(c);self.assertEqual(d['status'],'BLOCKED');self.assertTrue(d['gaps'])
    def test_external_fallback_blocked(self):
        c=self.candidate();c['network']=True;self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_missing_denominator_unverified(self):
        c=self.candidate();c['rows']=[x for x in c['rows'] if x['language']=='en'];self.assertEqual(decide(c)['status'],'UNVERIFIED')
    def test_one_failed_arabic_blocks(self):
        c=self.candidate();next(x for x in c['rows'] if x['language']=='ar')['output']='not label';self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_observed_results_not_declared_accepted(self):
        c=self.candidate();c['rows']=self.record['rows'];self.assertNotEqual(decide(c)['status'],'APPROVED')

class ArtifactTests(unittest.TestCase):
    def test_changed_artifact_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for n in FILES:(root/n).write_text('synthetic artifact')
            m=dict(model=MODEL,revision=REVISION,files={n:digest(root/n) for n in FILES})
            self.assertTrue(verify_manifest(root,m));(root/'config.json').write_text('modified')
            with self.assertRaises(ValueError):verify_manifest(root,m)
    def test_unknown_inventory_rejected(self):
        with self.assertRaises(ValueError):verify_manifest(HERE,dict(model=MODEL,revision=REVISION,files={'../x':'0'*64}))
    def test_moving_model_rejected(self):
        with self.assertRaises(ValueError):verify_manifest(HERE,dict(model=MODEL,revision='main',files={}))

if __name__=='__main__':unittest.main()
