import copy
import unittest
from concurrent.futures import ThreadPoolExecutor
from custody import ARTIFACTS, CustodyGate, Denied, boundary_state, demo, local_declaration

class PolicyTests(unittest.TestCase):
    def setUp(self): self.g = CustodyGate()
    def grants(self): return [self.g.approve_rotation(s,'A-key',1) for s in ('s-c1','s-c2')]
    def rotate(self, grants=None, now=100): return self.g.rotate('s-admin','A-key',1,grants or self.grants(),now)
    def test_reader(self): self.assertEqual(self.g.access('s-reader','A-doc')['result'],'METADATA_ONLY')
    def test_admin_not_reader(self): self.assertRaises(Denied,self.g.access,'s-admin','A-doc')
    def test_reader_not_admin(self): self.assertRaises(Denied,self.g.rotate,'s-reader','A-key',1,[])
    def test_support_not_reader(self): self.assertRaises(Denied,self.g.access,'s-support','A-doc')
    def test_support_not_approver(self): self.assertRaises(Denied,self.g.approve_rotation,'s-support','A-key',1)
    def test_cross_tenant_read(self): self.assertRaises(Denied,self.g.access,'s-other','A-doc')
    def test_cross_tenant_resource(self): self.assertRaises(Denied,self.g.access,'s-reader','B-doc')
    def test_cross_tenant_approval(self): self.assertRaises(Denied,self.g.approve_rotation,'s-other','A-key',1)
    def test_unknown_session(self): self.assertRaises(Denied,self.g.access,'forged','A-doc')
    def test_expired_session(self): self.assertRaises(Denied,self.g.access,'s-reader','A-doc',200)
    def test_revoked_session(self):
        self.g.users['reader']['active']=False
        self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
    def test_clearance(self):
        self.g.users['reader']['clearance']=1
        self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
    def test_removed_role(self):
        self.g.users['reader']['roles']=set()
        self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
    def test_rotation(self):
        out=self.rotate(); self.assertEqual(out['current'],2); self.assertEqual(out['versions'][1],'retired')
    def test_old_reference_retained(self):
        self.rotate(); self.assertEqual(self.g.access('s-reader','A-doc')['key_version'],1)
    def test_no_migration(self):
        self.rotate(); self.assertEqual(self.g.resources['A-doc']['version'],1)
    def test_return_copy(self):
        out=self.rotate(); out['versions'][1]='deleted'; self.assertEqual(self.g.keys['A-key']['versions'][1],'retired')
    def test_retired_disabled(self):
        self.rotate(); self.g.keys['A-key']['versions'][1]='disabled'; self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
    def test_missing_key(self):
        del self.g.keys['A-key']; self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
    def test_no_approvals(self): self.assertRaises(Denied,self.g.rotate,'s-admin','A-key',1,[])
    def test_duplicate_grant(self):
        g=self.grants()[0]; self.assertRaises(Denied,self.g.rotate,'s-admin','A-key',1,[g,g])
    def test_same_custodian_twice(self):
        gs=[self.g.approve_rotation('s-c1','A-key',1) for _ in range(2)]; self.assertRaises(Denied,self.rotate,gs)
    def test_initiator_cannot_approve(self):
        self.g.users['admin']['roles'].add('custodian'); gs=[self.g.approve_rotation(s,'A-key',1) for s in ('s-admin','s-c1')]; self.assertRaises(Denied,self.rotate,gs)
    def test_expiry_exact(self): self.assertRaises(Denied,self.rotate,self.grants(),110)
    def test_revoke_approver(self):
        gs=self.grants(); self.g.users['custodian1']['active']=False; self.assertRaises(Denied,self.rotate,gs)
    def test_remove_approver_role(self):
        gs=self.grants(); self.g.users['custodian1']['roles']=set(); self.assertRaises(Denied,self.rotate,gs)
    def test_change_approver_tenant(self):
        gs=self.grants(); self.g.users['custodian1']['tenant']='B'; self.assertRaises(Denied,self.rotate,gs)
    def test_expire_approver(self):
        gs=self.grants(); self.g.users['custodian1']['expires']=100; self.assertRaises(Denied,self.rotate,gs)
    def test_policy_stale(self):
        gs=self.grants(); self.g.policy_revision+=1; self.assertRaises(Denied,self.rotate,gs)
    def test_key_stale(self):
        gs=self.grants(); self.g.keys['A-key']['revision']+=1; self.assertRaises(Denied,self.rotate,gs)
    def test_wrong_key(self):
        gs=self.grants(); self.g.keys['A-other']=copy.deepcopy(self.g.keys['A-key']); self.assertRaises(Denied,self.g.rotate,'s-admin','A-other',1,gs)
    def test_unknown_grant(self): self.assertRaises(Denied,self.rotate,['forged','other'])
    def test_replay(self):
        gs=self.grants(); self.rotate(gs); self.assertRaises(Denied,self.g.rotate,'s-admin','A-key',2,gs)
    def test_bad_ttl(self):
        for value in (0,-1,11,True,'10'):
            with self.subTest(value=value): self.assertRaises(Denied,self.g.approve_rotation,'s-c1','A-key',1,100,value)
    def test_stale_approval(self): self.assertRaises(Denied,self.g.approve_rotation,'s-c1','A-key',0)
    def test_audit_failure_no_change(self):
        gs=self.grants(); old=copy.deepcopy(self.g.keys); self.g.audit_available=False; self.assertRaises(Denied,self.rotate,gs); self.assertEqual(old,self.g.keys); self.assertFalse(self.g.grants[gs[0]]['used'])
    def test_audit_no_secret(self):
        self.g.access('s-reader','A-doc'); self.assertEqual(set(self.g.audit[0]),{'actor','operation','target','outcome','policy_revision'})
    def test_concurrent_rotation(self):
        gs=self.grants()
        def run(_):
            try: self.rotate(gs); return 'ALLOWED'
            except Denied: return 'DENIED'
        with ThreadPoolExecutor(max_workers=2) as p: self.assertEqual(sorted(p.map(run,range(2))),['ALLOWED','DENIED'])
        self.assertEqual(self.g.keys['A-key']['current'],2)
    def test_demo_actual(self):
        out=demo(); self.assertEqual([x['decision'] for x in out['attempts']],['DENIED','DENIED','ALLOWED','ALLOWED','ALLOWED','DENIED','DENIED'])
    def test_every_external_artifact(self):
        for artifact in ARTIFACTS:
            with self.subTest(artifact=artifact):
                d=local_declaration(); d[artifact]='external'; self.assertEqual(boundary_state(d),'BLOCKED')
    def test_missing_is_unverified(self):
        d=local_declaration(); del d['logs']; self.assertEqual(boundary_state(d),'UNVERIFIED')
    def test_conflict_dominates_missing(self): self.assertEqual(boundary_state({'logs':'external'}),'BLOCKED')
    def test_declarations_not_verification(self): self.assertEqual(boundary_state(local_declaration()),'DECLARED_ONLY')
    def test_remote_operator(self):
        d=local_declaration(); d['operators']='remote'; self.assertEqual(boundary_state(d),'BLOCKED')
    def test_online(self):
        d=local_declaration(); d['network']='online'; self.assertEqual(boundary_state(d),'BLOCKED')
    def test_unreviewed_media(self):
        d=local_declaration(); d['media_reviewed']=False; self.assertEqual(boundary_state(d),'BLOCKED')
    def test_block_access(self):
        self.g.declaration['diagnostics']='external'; self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
    def test_unverified_access(self):
        del self.g.declaration['backups']; self.assertRaises(Denied,self.g.access,'s-reader','A-doc')
if __name__ == '__main__': unittest.main()
