import copy,json,unittest
from pathlib import Path
from run_local_model import build_prompt,check_record
class ModelRecordTests(unittest.TestCase):
    def setUp(self): self.record=json.loads(Path(__file__).with_name('observed-model-run.json').read_text())
    def test_observed_record(self): self.assertTrue(check_record(self.record))
    def test_context_only_authorized(self):
        prompt,chunks=build_prompt();self.assertEqual([c['id'] for c in chunks],['a-travel:0'])
        self.assertNotIn('B-ONLY',prompt);self.assertNotIn('410',prompt)
    def test_invented_score(self):
        self.record['exact_answer_pass']=not self.record['exact_answer_pass']
        with self.assertRaises(ValueError): check_record(self.record)
    def test_changed_prompt(self):
        self.record['prompt_sha256']='0'*64
        with self.assertRaises(ValueError): check_record(self.record)
    def test_changed_fixture(self):
        self.record['fixture_sha256']='0'*64
        with self.assertRaises(ValueError): check_record(self.record)
    def test_false_release(self):
        self.record['release']='APPROVED'
        with self.assertRaises(ValueError): check_record(self.record)
    def test_missing_hashes(self):
        self.record['artifact_hashes']={}
        with self.assertRaises(ValueError): check_record(self.record)
    def test_nonfinite_timing(self):
        self.record['generation_seconds']=float('nan')
        with self.assertRaises(ValueError): check_record(self.record)
    def test_changed_model(self):
        self.record['revision']='different'
        with self.assertRaises(ValueError): check_record(self.record)
    def test_changed_context(self):
        self.record['context_chunk_ids']=['b-travel:0']
        with self.assertRaises(ValueError): check_record(self.record)
    def test_token_bound(self):
        self.record['generated_tokens']=25
        with self.assertRaises(ValueError): check_record(self.record)
    def test_wrong_artifact_names(self):
        value=self.record['artifact_hashes'].pop('tokenizer.json');self.record['artifact_hashes']['invented.json']=value
        with self.assertRaises(ValueError): check_record(self.record)
    def test_runtime_pins(self):
        for key,value in [('torch','2.10.0'),('transformers','4.58.0')]:
            changed=copy.deepcopy(self.record);changed[key]=value
            with self.assertRaises(ValueError): check_record(changed)
    def test_cpu_build_allowed(self):
        self.record['torch']='2.9.1+cpu';self.assertTrue(check_record(self.record))
    def test_network_scope(self):
        self.record['network_guard']='physical air gap proven'
        with self.assertRaises(ValueError): check_record(self.record)
    def test_naive_time(self):
        self.record['started_utc']='2026-11-28T00:00:00'
        with self.assertRaises(ValueError): check_record(self.record)
    def test_non_utc_time(self):
        self.record['started_utc']='2026-11-28T00:00:00+05:30'
        with self.assertRaises(ValueError): check_record(self.record)
if __name__=='__main__': unittest.main()
