import json,unittest
from copy import deepcopy
from pathlib import Path
from check_run import check_run
class RunRecordTests(unittest.TestCase):
    def setUp(self):self.run=json.loads(Path(__file__).with_name('observed-local-run.json').read_text())
    def test_observed_record(self):self.assertTrue(check_run(self.run))
    def test_changed_runtime(self):
        self.run['transformers']='other';self.assertRaises(ValueError,check_run,self.run)
    def test_missing_arabic(self):
        self.run['rows']=self.run['rows'][:4];self.assertRaises(ValueError,check_run,self.run)
    def test_invented_favorable_score(self):
        self.run['exact_match']['en']['passed']=4;self.assertRaises(ValueError,check_run,self.run)
    def test_wrong_revision(self):
        self.run['revision']='main';self.assertRaises(ValueError,check_run,self.run)
    def test_changed_prompt(self):
        self.run['rows'][0]['prompt']='other';self.assertRaises(ValueError,check_run,self.run)
    def test_nan_time(self):
        self.run['rows'][0]['seconds']=float('nan');self.assertRaises(ValueError,check_run,self.run)
    def test_false_acceptance(self):
        self.run['status']='ACCEPTED';self.assertRaises(ValueError,check_run,self.run)
    def test_missing_tokenizer(self):
        del self.run['artifact_hashes']['tokenizer.json'];self.assertRaises(ValueError,check_run,self.run)
if __name__=='__main__':unittest.main()
