import copy
import json
import unittest
from pathlib import Path
from release_ops import ARTIFACTS, Controller, boundary, demo, manifest

class Controls(unittest.TestCase):
    def setUp(self):
        self.c=Controller(quota=2); self.value=manifest(); self.key=self.c.register(self.value)
    def ready(self): self.c.approve(self.key); self.c.deploy(self.key)
    def test_malformed_artifacts_never_mask_known_conflict(self):
        for assets in (None, [], 'invalid'):
            for field,value in [('operator','REMOTE'),('connectivity','INTERNET'),('media_review','FAIL')]:
                candidate=manifest(); candidate['artifacts']=assets; candidate[field]=value
                self.assertEqual(boundary(candidate),'BLOCKED')
    def test_unapproved_denied(self): self.assertFalse(self.c.deploy(self.key))
    def test_approved_deploys(self): self.ready(); self.assertEqual(self.c.active,self.key)
    def test_register_copies(self): self.value['version']='tamper'; self.assertEqual(self.c.registry[self.key]['version'],'v1')
    def test_runtime_change_requires_new_approval(self):
        self.ready(); value=manifest(); value['runtime_build']='python-fixture-v2'; key=self.c.register(value)
        self.assertNotEqual(key,self.key); self.assertFalse(self.c.deploy(key)); self.assertEqual(self.c.approve(key),'DECLARED_ONLY'); self.assertTrue(self.c.deploy(key))
    def test_runtime_mutation_rejected(self):
        self.ready(); self.c.registry[self.key]['runtime_build']='tampered'; self.assertEqual(self.c.approve(self.key),'UNVERIFIED'); self.assertFalse(self.c.deploy(self.key))
    def test_registry_tamper(self): self.ready(); self.c.registry[self.key]['version']='tamper'; self.assertFalse(self.c.deploy(self.key))
    def test_revocation(self): self.ready(); self.c.revoked.add(self.key); self.assertFalse(self.c.deploy(self.key))
    def test_unknown_release(self): self.assertFalse(self.c.deploy('unknown'))
    def test_missing_gate(self): self.value['gates'].pop('quality'); key=self.c.register(self.value); self.assertEqual(self.c.approve(key),'UNVERIFIED')
    def test_failed_gate(self):
        for gate in ('quality','security','identity','recovery'):
            v=manifest(); v['gates'][gate]='FAIL'; self.assertEqual(self.c.approve(self.c.register(v)),'UNVERIFIED')
    def test_extra_gate(self): self.value['gates']['other']='PASS'; self.assertEqual(self.c.approve(self.c.register(self.value)),'UNVERIFIED')
    def test_unknown_schema(self): self.value['telemetry_schema']='raw'; self.assertEqual(self.c.approve(self.c.register(self.value)),'UNVERIFIED')
    def test_external_each_artifact(self):
        for artifact in ARTIFACTS:
            v=manifest(); v['artifacts'][artifact]='EXTERNAL'; self.assertEqual(boundary(v),'BLOCKED',artifact)
    def test_missing_each_artifact(self):
        for artifact in ARTIFACTS:
            v=manifest(); del v['artifacts'][artifact]; self.assertEqual(boundary(v),'UNVERIFIED',artifact)
    def test_conflict_over_missing(self): self.value['artifacts'].pop('prompts'); self.value['artifacts']['backups']='EXTERNAL'; self.assertEqual(boundary(self.value),'BLOCKED')
    def test_external_operator(self): self.value['operator']='REMOTE'; self.assertEqual(boundary(self.value),'BLOCKED')
    def test_online(self): self.value['connectivity']='ONLINE'; self.assertEqual(boundary(self.value),'BLOCKED')
    def test_media_fail(self): self.value['media_review']='FAIL'; self.assertEqual(boundary(self.value),'BLOCKED')
    def test_missing_boundary(self): self.assertEqual(boundary({}),'UNVERIFIED')
    def test_valid_declaration_not_proof(self): self.assertEqual(boundary(self.value),'DECLARED_ONLY')
    def test_invalid_hash(self): self.value['model_sha256']='x'*64; self.assertRaises(ValueError,self.c.register,self.value)
    def test_unknown_field(self): self.value['extra']=1; self.assertRaises(ValueError,self.c.register,self.value)
    def test_no_release(self): self.assertEqual(self.c.request('tenant-a','1'),'NO_ELIGIBLE_RELEASE')
    def test_quota(self): self.ready(); self.c.request('tenant-a','1'); self.c.request('tenant-a','2'); self.assertEqual(self.c.request('tenant-a','3'),'QUOTA_DENIED'); self.assertEqual(self.c.metrics('tenant-a')['eligible_requests'],2)
    def test_tenant_independent_quota(self): self.ready(); self.c.request('tenant-a','1'); self.c.request('tenant-a','2'); self.assertEqual(self.c.request('tenant-b','1'),'RECORDED')
    def test_duplicate(self): self.ready(); self.c.request('tenant-a','1'); self.assertEqual(self.c.request('tenant-a','1'),'DUPLICATE'); self.assertEqual(len(self.c.requests),1)
    def test_unknown_tenant(self): self.ready(); self.assertRaises(ValueError,self.c.request,'bad','1')
    def test_minimized_event(self): self.ready(); self.c.request('tenant-a','private-id',prompt='PRIVATE BODY'); text=json.dumps(self.c.events); self.assertNotIn('PRIVATE BODY',text); self.assertNotIn('private-id',text)
    def test_bad_numeric_values(self):
        self.ready()
        for value in (True,-1,float('nan'),float('inf'),'5'):
            self.assertRaises(ValueError,self.c.request,'tenant-a','1',latency_ms=value)
    def test_invalid_tokens(self): self.ready(); self.assertRaises(ValueError,self.c.request,'tenant-a','1',tokens=True)
    def test_no_data(self): self.assertEqual(self.c.metrics('tenant-a')['decision'],'NO_DATA'); self.assertIsNone(self.c.metrics('tenant-a')['ratio'])
    def test_slo_latency(self): self.ready(); self.c.request('tenant-a','1',latency_ms=201); self.assertEqual(self.c.metrics('tenant-a')['good_requests'],0)
    def test_slo_exact_boundary(self): self.ready(); self.c.request('tenant-a','1',latency_ms=200); self.assertEqual(self.c.metrics('tenant-a')['good_requests'],1)
    def test_slo_failed_request(self): self.ready(); self.c.request('tenant-a','1',ok=False); self.assertEqual(self.c.metrics('tenant-a')['decision'],'FREEZE_AND_REVIEW')
    def test_bad_target(self):
        for value in (0,1,True,float('nan')): self.assertRaises(ValueError,self.c.metrics,'tenant-a',target=value)
    def test_rollback_none(self): self.assertFalse(self.c.rollback())
    def test_rollback(self): self.ready(); key=self.c.register(manifest('v2')); self.c.approve(key); self.c.deploy(key); self.assertTrue(self.c.rollback()); self.assertEqual(self.c.active,self.key)
    def test_rollback_revoked(self): self.ready(); key=self.c.register(manifest('v2')); self.c.approve(key); self.c.deploy(key); self.c.revoked.add(self.key); self.assertFalse(self.c.rollback())
    def test_mutation_stops_requests(self): self.ready(); self.c.registry[self.key]['prompt_version']='changed'; self.assertEqual(self.c.request('tenant-a','1'),'NO_ELIGIBLE_RELEASE')
    def test_demo(self):
        d=demo(); self.assertEqual(d['metrics']['good_requests'],9); self.assertEqual(d['metrics']['eligible_requests'],10); self.assertEqual(d['metrics']['ratio'],0.9); self.assertTrue(d['rollback_succeeded']); self.assertTrue(d['external_trace_deployment_denied'])
    def test_retained_record(self): self.assertEqual(json.loads(Path(__file__).with_name('observed-operations-run.json').read_text()),demo())

if __name__=='__main__': unittest.main()
