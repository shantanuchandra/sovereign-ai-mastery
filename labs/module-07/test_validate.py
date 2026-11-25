import copy,json,unittest
from pathlib import Path
from validate import validate,mermaid,PATHS,PLANES

class GraphTests(unittest.TestCase):
    def setUp(self):self.graph=json.loads(Path(__file__).with_name('factory.json').read_text())
    def test_complete_declarations_require_review(self):self.assertEqual(validate(self.graph)['status'],'REVIEW_REQUIRED')
    def test_every_lifecycle_network_path_blocks_airgap(self):
        for kind in PATHS:
            g=copy.deepcopy(self.graph);next(e for e in g['edges'] if e['kind']==kind)['transport']='network'
            self.assertEqual(validate(g)['status'],'BLOCKED',kind)
    def test_every_component_plane_is_scoped(self):
        for plane in PLANES:
            g=copy.deepcopy(self.graph);next(n for n in g['nodes'] if n['plane']==plane)['site']='CAMPUS-B'
            self.assertEqual(validate(g)['status'],'BLOCKED',plane)
    def test_country_scope_differs_from_premises(self):
        self.graph['boundary']='country';self.graph['nodes'][0]['site']='CAMPUS-B'
        self.assertEqual(validate(self.graph)['status'],'REVIEW_REQUIRED')
        self.graph['nodes'][0]['country']='OTHER'
        self.assertEqual(validate(self.graph)['status'],'BLOCKED')
    def test_duplicate_node_cannot_hide_known_offsite_copy(self):
        duplicate=copy.deepcopy(self.graph['nodes'][0]);duplicate['site']='OFFSITE'
        self.graph['nodes'].append(duplicate)
        r=validate(self.graph);self.assertEqual(r['status'],'BLOCKED');self.assertTrue(any('duplicate_node' in g for g in r['gaps']))
    def test_missing_path_and_dangling_reference_are_gaps(self):
        self.graph['edges'].pop();self.graph['edges'][0]['to']='missing'
        self.assertEqual(validate(self.graph)['status'],'UNVERIFIED')
    def test_stale_build_and_failed_test_precedence(self):
        self.graph['edges'][0]['build_id']='old'
        self.assertEqual(validate(self.graph)['status'],'UNVERIFIED')
        self.graph['edges'][1]['outcome']='fail'
        self.assertEqual(validate(self.graph)['status'],'BLOCKED')
    def test_zone_crossing_requires_explicit_authorization(self):
        next(e for e in self.graph['edges'] if e['kind']=='diagnostics')['authorization']='implicit'
        self.assertEqual(validate(self.graph)['status'],'UNVERIFIED')
    def test_protected_derivative_cannot_drop_label(self):
        self.graph['edges'][0]['protected']=False
        self.assertTrue(any('protection_downgrade' in g for g in validate(self.graph)['gaps']))
    def test_malformed_records_do_not_become_review_ready(self):
        for obj in [None,[],42,{'nodes':[None,{'id':[],'plane':[]}],'edges':[None,{'from':[],'kind':[]}]}]:
            self.assertEqual(validate(obj)['status'],'UNVERIFIED')
    def test_unknown_path_retains_network_conflict(self):
        self.graph['edges'][0].update(kind='unknown',transport='network')
        self.assertEqual(validate(self.graph)['status'],'BLOCKED')
    def test_missing_plane_is_unverified(self):
        self.graph['nodes']=[n for n in self.graph['nodes'] if n['plane']!='management']
        self.assertIn('missing_plane:management',validate(self.graph)['gaps'])
    def test_export_is_deterministic_and_injection_resistant(self):
        self.graph['nodes'].append({'id':'x"]\nclick x "https://evil.invalid"'})
        output=mermaid(self.graph)
        self.assertNotIn('evil.invalid',output);self.assertEqual(output,mermaid(self.graph))
        self.assertIn('updates',output)
    def test_input_is_not_mutated_and_acceptance_does_not_override(self):
        original=copy.deepcopy(self.graph);validate(self.graph);self.assertEqual(original,self.graph)
        self.graph['edges'][0]['transport']='network';self.graph['acceptance']='CEO approved'
        self.assertEqual(validate(self.graph)['status'],'BLOCKED')

if __name__=='__main__':unittest.main()
