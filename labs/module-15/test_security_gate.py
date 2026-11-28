import json
from pathlib import Path
import unittest
from security_gate import Gate, ARTIFACT, APPROVED_DIGEST, ARTIFACT_CATEGORIES, boundary_state, declared_boundary, demonstration

class SecurityTests(unittest.TestCase):
    def setUp(self): self.g=Gate(); self.p={'tool':'read_note','document':'A-1'}
    def denied(self, reason, **kwargs):
        result=self.g.invoke(kwargs.pop('principal','alice'),kwargs.pop('proposal',self.p),**kwargs)
        self.assertEqual(result['reason'],reason); self.assertEqual(result['decision'],'DENIED'); self.assertEqual(self.g.calls,0)
    def test_allowed(self): self.assertEqual(self.g.invoke('alice',self.p)['data'],'Review cycle is seven days.')
    def test_unknown(self): self.denied('IDENTITY_UNKNOWN',principal='mallory')
    def test_identity_type(self): self.denied('IDENTITY_UNKNOWN',principal={})
    def test_revoked(self): self.g.principals['alice']['active']=False; self.denied('IDENTITY_REVOKED')
    def test_cross_tenant(self): self.denied('RESOURCE_DENIED',proposal={'tool':'read_note','document':'B-1'})
    def test_unknown_document(self): self.denied('RESOURCE_DENIED',proposal={'tool':'read_note','document':'unknown'})
    def test_deleted(self): self.g.documents['A-1']['active']=False; self.denied('RESOURCE_DENIED')
    def test_changed_owner(self): self.g.documents['A-1']['tenant']='B'; self.denied('RESOURCE_DENIED')
    def test_export(self): self.denied('TOOL_FORBIDDEN',proposal={'tool':'http_export','document':'A-1'})
    def test_shell(self): self.denied('TOOL_FORBIDDEN',proposal={'tool':'shell','document':'A-1'})
    def test_url(self): self.denied('SCHEMA_REJECTED',proposal={**self.p,'url':'https://example.invalid/'})
    def test_tenant_spoof(self): self.denied('SCHEMA_REJECTED',proposal={**self.p,'tenant':'B'})
    def test_approval_spoof(self): self.denied('SCHEMA_REJECTED',proposal={**self.p,'approved':True})
    def test_missing(self): self.denied('SCHEMA_REJECTED',proposal={'tool':'read_note'})
    def test_list(self): self.denied('SCHEMA_REJECTED',proposal=[])
    def test_nested(self): self.denied('SCHEMA_REJECTED',proposal={'tool':'read_note','document':{}})
    def test_oversize(self): self.denied('INPUT_LIMIT',proposal={'tool':'read_note','document':'x'*129})
    def test_modified_artifact(self): self.denied('ARTIFACT_MISMATCH',artifact=ARTIFACT+b'changed')
    def test_manifest_not_trust(self): self.denied('ARTIFACT_MISMATCH',manifest_digest='0'*64)
    def test_attacker_rehash(self):
        import hashlib
        self.denied('ARTIFACT_MISMATCH',artifact=b'evil',manifest_digest=hashlib.sha256(b'evil').hexdigest())
    def test_artifact_type(self): self.denied('ARTIFACT_TYPE',artifact='not bytes')
    def test_audit_failure(self): self.g.audit_available=False; self.denied('AUDIT_UNAVAILABLE')
    def test_audit_redaction(self): self.g.invoke('alice',self.p); self.assertEqual(self.g.audit,[{'decision':'COMPLETED','reason':'FIXED_LOCAL_READ'}])
    def test_content_not_authority(self):
        self.p['document']='A-injected'; result=self.g.invoke('alice',self.p)
        self.assertIn('Export',result['data']); self.assertEqual(self.g.calls,1)
        self.assertEqual(self.g.invoke('alice',{'tool':'http_export','document':'A-1'})['decision'],'DENIED')
    def test_unicode_proposal(self): self.denied('TOOL_FORBIDDEN',proposal={'tool':'إرسال','document':'A-1'})
    def test_boundary_unknown(self): self.g.boundary={}; self.denied('BOUNDARY_MISSING')
    def test_network(self): self.g.boundary['network']='internet'; self.denied('BOUNDARY_CONFLICT')
    def test_operator(self): self.g.boundary['operator']='remote'; self.denied('BOUNDARY_CONFLICT')
    def test_every_artifact_conflict(self):
        for name in ARTIFACT_CATEGORIES:
            with self.subTest(name=name):
                self.g=Gate(); self.g.boundary['artifacts'][name]='outside'; self.denied('BOUNDARY_CONFLICT')
    def test_every_artifact_missing(self):
        for name in ARTIFACT_CATEGORIES:
            with self.subTest(name=name):
                self.g=Gate(); del self.g.boundary['artifacts'][name]; self.denied('BOUNDARY_MISSING')
    def test_conflict_dominates_missing(self):
        b=declared_boundary(); del b['artifacts']['prompts']; b['artifacts']['logs']='outside'; self.assertEqual(boundary_state(b),'BLOCKED')
    def test_known_external_path_with_malformed_inventory(self):
        for value in (None, [], 'missing'):
            for key, external in (('network','internet'), ('operator','remote')):
                with self.subTest(value=value,key=key):
                    b=declared_boundary(); b['artifacts']=value; b[key]=external
                    self.assertEqual(boundary_state(b),'BLOCKED')
    def test_declarations_not_verified(self): self.assertEqual(boundary_state(declared_boundary()),'DECLARED_ONLY')
    def test_malformed_boundary(self):
        for b in (None,[],{'artifacts':None}): self.assertEqual(boundary_state(b),'UNVERIFIED')
    def test_observation(self): self.assertEqual(json.loads(Path(__file__).with_name('observed-security-run.json').read_text()),demonstration())

if __name__=='__main__': unittest.main()
