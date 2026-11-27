import copy
import json
from pathlib import Path
import unittest
from compare import assess, compare, simulate, ROUTES

FIXTURE=json.loads(Path(__file__).with_name('deployments.json').read_text())

class DeploymentTests(unittest.TestCase):
    def setUp(self):
        self.p=copy.deepcopy(FIXTURE['policy'])
        self.c=copy.deepcopy(FIXTURE['candidates'][0])
    def test_local_simulation_requires_review(self):
        r=assess(self.p,self.c)
        self.assertEqual(r['status'],'REVIEW_REQUIRED')
        self.assertEqual(r['recovery']['rto_minutes'],4)
        self.assertEqual(r['recovery']['rpo_minutes'],2)
    def test_comparison_excludes_high_scoring_blocked_designs(self):
        r=compare(self.p,FIXTURE['candidates'])
        self.assertEqual(r['ranked_candidates'],['local-private'])
        self.assertTrue(all(x['status']=='BLOCKED' for x in r['candidates'][1:]))
    def test_each_lifecycle_cannot_leave_premises(self):
        for purpose in ROUTES:
            with self.subTest(purpose=purpose):
                c=copy.deepcopy(self.c)
                next(x for x in c['routes'] if x['purpose']==purpose)['site']='OTHER'
                self.assertEqual(assess(self.p,c)['status'],'BLOCKED')
    def test_unknown_route_keeps_known_conflict(self):
        self.c['routes'].append(dict(purpose='unknown',site='OTHER',country='AE',network=False,operator='enterprise'))
        r=assess(self.p,self.c)
        self.assertEqual(r['status'],'BLOCKED');self.assertTrue(r['gaps'])
    def test_duplicate_route_keeps_known_conflict(self):
        item=copy.deepcopy(self.c['routes'][0]);item['site']='OTHER'
        self.c['routes'].append(item)
        r=assess(self.p,self.c)
        self.assertEqual(r['status'],'BLOCKED');self.assertTrue(r['gaps'])
    def test_missing_route_is_unverified(self):
        self.c['routes'].pop()
        self.assertEqual(assess(self.p,self.c)['status'],'UNVERIFIED')
    def test_country_scope_does_not_enforce_site(self):
        self.p['scope']='country'
        for x in self.c['routes']:x['site']='OTHER'
        for event in self.c['recovery']['events']:event['site']='OTHER'
        self.assertEqual(assess(self.p,self.c)['status'],'REVIEW_REQUIRED')
    def test_country_scope_rejects_foreign_derivative(self):
        self.p['scope']='country';self.c['routes'][-1]['country']='XX'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
    def test_airgap_rejects_every_network_path(self):
        self.p['airgap']=True
        for purpose in ROUTES:
            c=copy.deepcopy(self.c)
            next(x for x in c['routes'] if x['purpose']==purpose)['network']=True
            self.assertEqual(assess(self.p,c)['status'],'BLOCKED',purpose)
    def test_remote_operator_not_silently_permitted(self):
        self.c['routes'][0]['operator']='provider_remote'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
    def test_unknown_operator_is_gap(self):
        self.c['routes'][0]['operator']='unspecified'
        self.assertEqual(assess(self.p,self.c)['status'],'UNVERIFIED')
    def test_unknown_dependency_inventory_is_gap(self):
        self.c['dependency_inventory_complete']=False
        self.assertEqual(assess(self.p,self.c)['status'],'UNVERIFIED')
    def test_stale_or_assumed_profile_not_ranked(self):
        for key,value in [('evidence_kind','assumed'),('observed_build','old')]:
            c=copy.deepcopy(self.c);c[key]=value
            self.assertEqual(assess(self.p,c)['status'],'UNVERIFIED')
            self.assertEqual(compare(self.p,[c])['ranked_candidates'],[])
    def test_no_label_certifies_deployment(self):
        self.c['evidence_kind']='deployment_test'
        self.assertEqual(assess(self.p,self.c)['status'],'REVIEW_REQUIRED')
    def test_recovery_outside_boundary_blocks(self):
        self.c['recovery']['events'][-1]['site']='OFFSITE'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
    def test_rto_and_rpo_are_separate_gates(self):
        for key,value in [('rto_minutes',3),('rpo_minutes',1)]:
            p=copy.deepcopy(self.p);p[key]=value
            self.assertEqual(assess(p,self.c)['status'],'BLOCKED')
    def test_same_failure_domain_blocks(self):
        self.c['recovery']['target_domain']=self.c['recovery']['failed_domain']
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
    def test_site_loss_single_site_is_infeasible(self):
        self.p['failure_scope']='site'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
        self.c['recovery']['events'][-1]['site']='OTHER'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
    def test_country_authorized_site_recovery_possible_in_simulation(self):
        self.p.update(scope='country',failure_scope='site')
        self.c['recovery']['events'][-1]['site']='OTHER'
        next(x for x in self.c['routes'] if x['purpose']=='failover')['site']='OTHER'
        self.assertEqual(assess(self.p,self.c)['status'],'REVIEW_REQUIRED')
    def test_invalid_numbers_and_booleans_rejected(self):
        for value in [True,-1,float('nan'),float('inf'),10**1000,'5',None]:
            c=copy.deepcopy(self.c);c['monthly_cost_aed']=value
            with self.assertRaises(ValueError):assess(self.p,c)
    def test_invalid_enums_and_network_boolean_rejected(self):
        self.p['scope']='region'
        with self.assertRaises(ValueError):assess(self.p,self.c)
        self.p['scope']='premises';self.c['routes'][0]['network']='false'
        with self.assertRaises(ValueError):assess(self.p,self.c)
    def test_timeline_order_kind_and_cardinality_rejected(self):
        events=self.c['recovery']['events']
        for bad in [events[::-1],events[:2],events+[events[-1]],
                    [dict(events[0],kind='invented'),*events[1:]],
                    [events[0],dict(events[1],at=-1),events[2]]]:
            with self.assertRaises(ValueError):simulate(bad)
    def test_duplicate_candidates_rejected(self):
        with self.assertRaises(ValueError):compare(self.p,[self.c,self.c])
    def test_zero_duration_and_loss_are_valid(self):
        events=[dict(x,at=10) for x in self.c['recovery']['events']]
        self.assertEqual(simulate(events)['rto_minutes'],0)
        self.assertEqual(simulate(events)['rpo_minutes'],0)
    def test_unknown_failure_domain_is_not_ranked(self):
        self.c['recovery']['target_domain']='UNKNOWN'
        self.assertEqual(assess(self.p,self.c)['status'],'UNVERIFIED')
    def test_unknown_location_retains_known_country_conflict(self):
        self.c['routes'][0].update(site='UNKNOWN',country='XX')
        r=assess(self.p,self.c)
        self.assertEqual(r['status'],'BLOCKED');self.assertTrue(r['gaps'])
    def test_unknown_policy_is_rejected(self):
        self.p['site']='UNKNOWN'
        with self.assertRaises(ValueError):assess(self.p,self.c)
    def test_event_and_route_disagreement_is_gap(self):
        self.p['scope']='country'
        for event in self.c['recovery']['events']:
            c=copy.deepcopy(self.c)
            next(x for x in c['recovery']['events'] if x['kind']==event['kind'])['site']='OTHER'
            self.assertEqual(assess(self.p,c)['status'],'UNVERIFIED')
    def test_airgap_cannot_allow_remote_administration(self):
        self.p.update(scope='country',airgap=True,allowed_operators=['enterprise','provider_remote'])
        self.c['routes'][0]['operator']='provider_remote'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')
    def test_premises_policy_cannot_allow_remote_administration(self):
        self.p['allowed_operators'].append('provider_remote')
        self.c['routes'][0]['operator']='provider_remote'
        self.assertEqual(assess(self.p,self.c)['status'],'BLOCKED')

if __name__=='__main__':unittest.main()
