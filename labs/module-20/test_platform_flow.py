import copy
import json
from pathlib import Path
import unittest
from platform_flow import Platform, FlowError, TRACE, ARTIFACTS, boundary, local_plan, demo

class FlowTests(unittest.TestCase):
    def setUp(self): self.p = Platform()
    def create(self): return self.p.call('fixture-a','tenant-a','create',{'name':'Synthetic'},'create')
    def configured(self):
        self.create(); self.p.call('fixture-a','tenant-a','configure',{'plan':local_plan()},'configure')
    def validated(self):
        self.configured(); self.p.call('fixture-a','tenant-a','validate',{'acceptance':dict.fromkeys(TRACE,True)},'validate')
    def test_cross_tenant(self):
        self.create()
        for op in ('read','activate'):
            with self.assertRaisesRegex(FlowError,'DENIED_SCOPE'): self.p.call('fixture-b','tenant-a',op,{},'x')
    def test_unknown_principal(self):
        with self.assertRaisesRegex(FlowError,'DENIED_SCOPE'): self.p.call('tenant-a','tenant-a','create',{},'x')
    def test_reader(self):
        self.create()
        self.assertEqual(self.p.call('fixture-reader','tenant-a','read')['stage'],'REQUESTED')
        with self.assertRaisesRegex(FlowError,'DENIED_ROLE'): self.p.call('fixture-reader','tenant-a','activate',{},'x')
    def test_idempotent_retry(self):
        first=self.create(); self.assertEqual(first,self.create()); self.assertEqual(len(self.p.events),1)
    def test_idempotency_conflict(self):
        self.create()
        with self.assertRaisesRegex(FlowError,'IDEMPOTENCY_CONFLICT'): self.p.call('fixture-a','tenant-a','create',{'name':'Other'},'create')
    def test_cross_tenant_key(self):
        self.create(); self.p.call('fixture-b','tenant-b','create',{'name':'B'},'create'); self.assertEqual(len(self.p.events),2)
    def test_stage_skip(self):
        self.create()
        with self.assertRaisesRegex(FlowError,'INVALID_TRANSITION'): self.p.call('fixture-a','tenant-a','activate',{},'x')
    def test_boundary_conflict(self):
        for artifact in ARTIFACTS:
            with self.subTest(artifact=artifact):
                plan=local_plan(); plan['paths'][artifact]='external'; self.assertEqual(boundary(plan)['status'],'BLOCKED')
    def test_airgap(self):
        for field,value in [('network','connected'),('media_review',False),('operator','remote')]:
            plan=local_plan(); plan[field]=value; self.assertEqual(boundary(plan)['status'],'BLOCKED')
    def test_missing_evidence(self):
        self.assertEqual(boundary({})['status'],'UNVERIFIED')
        self.configured()
        with self.assertRaisesRegex(FlowError,'UNVERIFIED_ACCEPTANCE'): self.p.call('fixture-a','tenant-a','validate',{'acceptance':{}},'v')
    def test_conflict_dominates_missing(self):
        plan=local_plan(); plan['paths']={}; plan['operator']='remote'; self.assertEqual(boundary(plan)['status'],'BLOCKED')
    def test_extra_conflicting_route(self):
        plan=local_plan(); plan["paths"]={"diagnostics":"external"}
        self.assertEqual(boundary(plan)["status"],"BLOCKED")
    def test_nonlocal_synonyms(self):
        for value in ("cloud","remote","off-site","domestic-cloud","vendor"):
            plan=local_plan(); plan["paths"]["support"]=value
            self.assertEqual(boundary(plan)["status"],"BLOCKED")
    def test_operator_nonlocal_and_missing(self):
        plan={"operator":"cloud", "paths":{}}
        self.assertEqual(boundary(plan)["status"],"BLOCKED")
    def test_connected_synonyms_and_missing(self):
        for value in ("internet","online","internet-enabled","remote"):
            plan={"airgap":True,"network":value}
            self.assertEqual(boundary(plan)["status"],"BLOCKED")
    def test_invalid_route_unverified(self):
        plan=local_plan(); plan["paths"]["diagnostics"]=[]
        self.assertEqual(boundary(plan)["status"],"UNVERIFIED")
    def test_malformed_inventory(self):
        plan=local_plan(); plan['paths']=[]; plan['network']='connected'; self.assertEqual(boundary(plan)['status'],'BLOCKED')
    def test_validation_boundary_dominates_missing_acceptance(self):
        self.configured()
        self.p.records['tenant-a']['plan']['paths']['traces']='external'
        for acceptance in ({}, None, {'R1': False}):
            with self.subTest(acceptance=acceptance):
                with self.assertRaisesRegex(FlowError,'BOUNDARY_CHANGED'):
                    self.p.call('fixture-a','tenant-a','validate',{'acceptance':acceptance},'v')
        self.assertEqual(self.p.records['tenant-a']['stage'],'CONFIGURED')
        self.assertEqual(len(self.p.events),2)
    def test_strict_acceptance(self):
        self.configured()
        for value in (1,'PASS',False,None):
            with self.subTest(value=value):
                data=dict.fromkeys(TRACE,True); data['R1']=value
                with self.assertRaisesRegex(FlowError,'UNVERIFIED_ACCEPTANCE'): self.p.call('fixture-a','tenant-a','validate',{'acceptance':data},'v')
    def test_unknown_property(self):
        with self.assertRaisesRegex(FlowError,'INVALID_PROPERTIES'): self.p.call('fixture-a','tenant-a','create',{'name':'A','tenant':'tenant-b'},'x')
    def test_invalid_key(self):
        for key in (None,'',4,'x'*81):
            with self.assertRaisesRegex(FlowError,'INVALID_REQUEST'): self.p.call('fixture-a','tenant-a','create',{'name':'A'},key)
    def test_configure_denies(self):
        self.create(); plan=local_plan(); plan['paths']['logs']='external'
        with self.assertRaisesRegex(FlowError,'BLOCKED'): self.p.call('fixture-a','tenant-a','configure',{'plan':plan},'c')
        self.assertEqual(self.p.records['tenant-a']['stage'],'REQUESTED')
    def test_activate_rechecks(self):
        self.validated(); self.p.records['tenant-a']['plan']['operator']='remote'
        with self.assertRaisesRegex(FlowError,'BOUNDARY_CHANGED'): self.p.call('fixture-a','tenant-a','activate',{},'a')
    def test_evidence_rechecks(self):
        self.validated(); self.p.records['tenant-a']['acceptance']['R1']=False
        with self.assertRaisesRegex(FlowError,'UNVERIFIED_ACCEPTANCE'): self.p.call('fixture-a','tenant-a','activate',{},'a')
    def test_defensive_copies(self):
        self.configured(); record=self.p.call('fixture-a','tenant-a','read'); record['plan']['operator']='remote'; self.assertEqual(self.p.records['tenant-a']['plan']['operator'],'on-site')
    def test_demo(self): self.assertEqual(demo()['event_count'],4)
    def test_retained_record(self): self.assertEqual(json.loads(Path(__file__).with_name('observed-platform-run.json').read_text()),demo())
    def test_traceability(self):
        for name in TRACE.values(): self.assertTrue(callable(getattr(self,name)))

if __name__=='__main__': unittest.main()
