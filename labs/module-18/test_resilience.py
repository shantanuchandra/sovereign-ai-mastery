import copy
import json
import tempfile
import unittest
from pathlib import Path
from resilience import ARTIFACTS, Exercise, boundary, declaration, demo, encode, fixture, digest

class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(prefix='module18-test-'); self.addCleanup(self.temp.cleanup)
        self.e=Exercise(self.temp.name); self.e.capture(fixture())
    def test_real_file_restore(self):
        expected=self.e.live.read_bytes(); self.e.live.unlink()
        self.assertEqual(self.e.recover(declaration())['decision'],'RESTORED_SYNTHETIC')
        self.assertEqual(self.e.live.read_bytes(),expected)
    def test_retirement_survives_old_backup(self):
        self.e.retired.add('d2'); self.e.recover(declaration())
        self.assertEqual(self.e.substitute('a')['ids'],['d1'])
        self.assertNotIn('d2',self.e.live.read_text())
    def test_all_external_paths_blocked(self):
        for artifact in ARTIFACTS:
            with self.subTest(artifact=artifact):
                d=declaration(); d['artifacts'][artifact]='EXTERNAL'
                self.assertEqual(self.e.recover(d)['decision'],'BLOCKED')
    def test_missing_path_unverified(self):
        d=declaration(); del d['artifacts']['ocr']; self.assertEqual(boundary(d),'UNVERIFIED')
    def test_conflict_dominates_missing(self):
        d=declaration(); d['artifacts']={}; d['connectivity']='CONNECTED'; self.assertEqual(boundary(d),'BLOCKED')
    def test_airgap_operator_and_media(self):
        for key,value in [('operator','REMOTE'),('connectivity','CONNECTED'),('media_review','FAIL')]:
            d=declaration(); d[key]=value; self.assertEqual(boundary(d),'BLOCKED')
    def test_unknown_not_verified(self):
        for value in (None,{}, {'artifacts':None}): self.assertEqual(boundary(value),'UNVERIFIED')
        self.assertEqual(boundary(declaration()),'DECLARED_ONLY')
    def test_tampered_backup_does_not_replace_live(self):
        expected=self.e.live.read_bytes(); self.e.backup.write_bytes(b'corrupt')
        self.assertEqual(self.e.recover(declaration())['reason'],'INTEGRITY_MISMATCH')
        self.assertEqual(self.e.live.read_bytes(),expected)
    def test_missing_backup(self):
        self.e.backup.unlink(); self.assertEqual(self.e.recover(declaration())['decision'],'UNVERIFIED')
    def test_schema_rejected_even_with_matching_checksum(self):
        data=encode({'schema':2,'records':[]}); self.e.backup.write_bytes(data); self.e.expected=digest(data)
        self.assertEqual(self.e.recover(declaration())['reason'],'SCHEMA')
    def test_duplicate_id_rejected(self):
        f=fixture(); f['records'].append(copy.deepcopy(f['records'][0]))
        with self.assertRaises(ValueError): self.e.capture(f)
    def test_revoked_model(self):
        self.e.revoked_models.add('old'); self.assertEqual(self.e.recover(declaration(),'old')['decision'],'BLOCKED')
        self.assertEqual(self.e.substitute('a','old')['decision'],'BLOCKED')
    def test_revocation_dominates_missing_boundary(self):
        self.e.revoked_models.add('old')
        before=self.e.live.read_bytes()
        self.assertEqual(self.e.recover({},'old'),{'decision':'BLOCKED','reason':'MODEL_REVOKED'})
        self.assertEqual(self.e.live.read_bytes(),before)
    def test_malformed_model_graceful(self):
        before=self.e.live.read_bytes()
        for model in ([],{},None,True,1,''):
            with self.subTest(model=model):
                self.assertEqual(self.e.recover(declaration(),model)['decision'],'UNVERIFIED')
                self.assertEqual(self.e.substitute('a',model)['decision'],'UNVERIFIED')
        self.assertEqual(self.e.live.read_bytes(),before)
    def test_boundary_conflict_dominates_malformed_model(self):
        d=declaration(); d['artifacts']['failover']='EXTERNAL'
        self.assertEqual(self.e.recover(d,[])['decision'],'BLOCKED')
    def test_schema_requires_exact_integer_one(self):
        before=self.e.live.read_bytes()
        for schema in (True,1.0):
            with self.subTest(schema=schema):
                f=fixture(); f['schema']=schema
                with self.assertRaises(ValueError): self.e.capture(f)
                data=encode(f); self.e.backup.write_bytes(data); self.e.expected=digest(data)
                self.assertEqual(self.e.recover(declaration())['reason'],'SCHEMA')
                self.assertEqual(self.e.live.read_bytes(),before)
    def test_migration_exact_equality(self):
        self.e.retired.add('d2'); self.e.recover(declaration()); result=self.e.migrate()
        self.assertEqual(result,{'decision':'MIGRATED_SYNTHETIC','rows':2,'equal_records':True})
    def test_retirement_rechecked_at_migration(self):
        self.e.recover(declaration()); self.e.retired.add('d2')
        self.assertEqual(self.e.migrate()['rows'],2)
    def test_cross_tenant_substitute(self):
        self.assertEqual(self.e.substitute('b')['ids'],['d3']); self.assertEqual(self.e.substitute('unknown')['ids'],[])
    def test_observation(self):
        o=demo(); self.assertEqual(o['substitution']['ids'],['d1']); self.assertEqual(o['external_failover']['decision'],'BLOCKED')
        self.assertTrue(o['live_file_deleted_before_restore']); self.assertTrue(o['migration']['equal_records'])

if __name__=='__main__': unittest.main()
