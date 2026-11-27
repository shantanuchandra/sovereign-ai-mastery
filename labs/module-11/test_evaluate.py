import unittest
from evaluate import score_rows, decide, verify_manifest
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib

class EvaluationTests(unittest.TestCase):
    def rows(self):
        return [dict(id='en1',language='en',expected='LOCAL',output='local'),dict(id='ar1',language='ar',expected='محلي',output='محلي')]
    def candidate(self):
        return dict(site='BANK-A',network=False,remote_operator=False,license_review=True,provenance=True,build='abc',evaluated_build='abc',rows=self.rows())
    def test_network_guard(self):
        from run_local import deny_network
        self.assertRaises(RuntimeError,deny_network,('example.invalid',443))
    def test_score(self):self.assertEqual(score_rows(self.rows())['ar'],dict(passed=1,total=1,rate=1))
    def test_normalization(self):
        r=self.rows();r[0]['output']='  ＬＯＣＡＬ\n';self.assertEqual(score_rows(r)['en']['passed'],1)
    def test_no_substring_credit(self):
        r=self.rows();r[0]['output']='not local';self.assertEqual(score_rows(r)['en']['passed'],0)
    def test_favorable_only_review(self):self.assertEqual(decide(self.candidate())['status'],'REVIEW_REQUIRED')
    def test_arabic_failure(self):
        c=self.candidate();c['rows'][1]['output']='wrong';self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_missing_arabic_unknown(self):
        c=self.candidate();c['rows']=c['rows'][:1];self.assertEqual(decide(c)['status'],'UNVERIFIED')
    def test_license_false(self):
        c=self.candidate();c['license_review']=False;self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_license_missing(self):
        c=self.candidate();del c['license_review'];self.assertEqual(decide(c)['status'],'UNVERIFIED')
    def test_conflict_survives_missing(self):
        c=self.candidate();c['site']='DC-B';del c['license_review'];self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_network_block(self):
        c=self.candidate();c['network']=True;self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_remote_operator_block(self):
        c=self.candidate();c['remote_operator']=True;self.assertEqual(decide(c)['status'],'BLOCKED')
    def test_unknown_site(self):
        c=self.candidate();c['site']=None;self.assertEqual(decide(c)['status'],'UNVERIFIED')
    def test_build_mismatch(self):
        c=self.candidate();c['evaluated_build']='old';self.assertEqual(decide(c)['status'],'UNVERIFIED')
    def test_string_bool_rejected(self):
        c=self.candidate();c['network']='false';self.assertEqual(decide(c)['status'],'UNVERIFIED')
    def test_duplicate_id(self):
        r=self.rows();r.append(r[0]);self.assertRaises(ValueError,score_rows,r)
    def test_unknown_language(self):
        r=self.rows();r[0]['language']='xx';self.assertRaises(ValueError,score_rows,r)
    def test_empty_expected(self):
        r=self.rows();r[0]['expected']=' ';self.assertRaises(ValueError,score_rows,r)
    def test_missing_output(self):
        r=self.rows();del r[0]['output'];self.assertRaises(ValueError,score_rows,r)
    def test_empty_rows_not_success(self):self.assertEqual(score_rows([]),{})
    def test_manifest_mutation(self):
        with TemporaryDirectory() as d:
            p=Path(d);(p/'a').write_text('safe');m={'files':{'a':hashlib.sha256(b'safe').hexdigest()}}
            verify_manifest(p,m);(p/'a').write_text('changed');self.assertRaises(ValueError,verify_manifest,p,m)
    def test_manifest_escape(self):
        with TemporaryDirectory() as d:self.assertRaises(ValueError,verify_manifest,Path(d),{'files':{'../x':'a'*64}})
    def test_empty_manifest(self):
        with TemporaryDirectory() as d:self.assertRaises(ValueError,verify_manifest,Path(d),{'files':{}})
if __name__=='__main__':unittest.main()
