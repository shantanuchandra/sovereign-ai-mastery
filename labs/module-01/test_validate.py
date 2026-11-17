import unittest
from validate import assess
class LabTests(unittest.TestCase):
    def setUp(self):
        self.claim=dict(id='X',workload='W',scope='enterprise',dimension='territorial',owner='P',criterion='C',control='K',test='T',evidence={'status':'missing'})
    def test_missing_evidence_is_unverified(self):
        self.assertEqual(assess(self.claim)['status'],'UNVERIFIED')
    def test_missing_owner_is_invalid(self):
        self.claim['owner']=''
        self.assertEqual(assess(self.claim)['status'],'INVALID')
    def test_bad_scope_is_invalid(self):
        self.claim['scope']='universal'
        self.assertEqual(assess(self.claim)['status'],'INVALID')
    def test_test_record_is_not_compliance(self):
        self.claim['evidence']={'status':'tested','source':'mock','observed_at':'2026-11-17'}
        self.assertEqual(assess(self.claim)['status'],'REVIEW_REQUIRED')
if __name__=='__main__':unittest.main()