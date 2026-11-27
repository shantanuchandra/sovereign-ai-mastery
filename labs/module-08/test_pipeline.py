import copy,json,sqlite3,unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from pipeline import Pipeline,vector,similarity
class DataPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp=TemporaryDirectory();self.root=Path(self.temp.name)/'lab';self.p=Pipeline(self.root)
        self.records=json.loads(Path(__file__).with_name('records.json').read_text())
    def tearDown(self):self.p.close();self.temp.cleanup()
    def ingest_all(self):
        for r in self.records:self.p.ingest(r)
    def test_tenant_filter_before_excerpt(self):
        self.ingest_all();rows=self.p.query('plant_a','pump pressure','2026-11-26')
        self.assertEqual([r['document'] for r in rows],['manual_a'])
        self.assertNotIn('tenant B',str(rows))
    def test_sql_injection_tenant_is_rejected(self):
        self.ingest_all()
        with self.assertRaises(ValueError):self.p.query("plant_a' OR 1=1--",'pump','2026-11-26')
    def test_lineage_and_classification_survive_chunking(self):
        self.ingest_all();r=self.p.query('plant_a','pump','2026-11-26')[0]
        self.assertEqual(r['classification'],'restricted');self.assertEqual(len(r['source_hash']),64)
        self.assertTrue(r['chunk'].startswith(r['document']))
    def test_expiry_excludes_before_purge_and_cascades(self):
        self.ingest_all();self.assertEqual(self.p.query('plant_a','pump','2026-12-01'),[])
        self.assertEqual(self.p.expire('2026-12-01'),4)
        self.assertEqual(self.p.db.execute('SELECT count(*) FROM chunks').fetchone()[0],0)
    def test_restore_cannot_resurrect_retired_record(self):
        self.ingest_all();self.p.snapshot('snapshot_a')
        self.assertEqual(self.p.retire('plant_a','manual_a')['state'],'UNVERIFIED')
        self.p.restore('snapshot_a');self.assertEqual(self.p.query('plant_a','pump','2026-11-26'),[])
        self.assertTrue(self.p.query('plant_b','pump','2026-11-26'))
    def test_reopen_preserves_tombstone(self):
        self.ingest_all();self.p.retire('plant_a','manual_a');self.p.close();self.p=Pipeline(self.root)
        with self.assertRaises(ValueError):self.p.ingest(self.records[0])
    def test_missing_ledger_fails_closed(self):
        self.p.close();(self.root/'ledger.sqlite').unlink()
        with self.assertRaises(ValueError):Pipeline(self.root)
    def test_snapshot_path_traversal_and_unknown_deletion(self):
        for name in ['../outside','/tmp/x','store.sqlite','UPPER']:
            with self.assertRaises(ValueError):self.p.snapshot(name)
        with self.assertRaises(ValueError):self.p.remove_snapshot('unknown')
    def test_registered_snapshot_removal_is_bounded(self):
        self.ingest_all();path=self.p.snapshot('owned_copy');self.p.remove_snapshot('owned_copy');self.assertFalse(path.exists())
        self.assertEqual(self.p.retire('plant_a','manual_a')['state'],'REVIEW_REQUIRED')
    def test_known_boundary_conflicts_do_not_ingest(self):
        for key,value in [('site','OFFSITE'),('country','OTHER'),('preprocess_site','CLOUD'),('transport','network')]:
            r=copy.deepcopy(self.records[0]);r[key]=value
            with self.assertRaisesRegex(ValueError,'BLOCKED'):self.p.ingest(r)
        self.assertEqual(self.p.db.execute('SELECT count(*) FROM docs').fetchone()[0],0)
    def test_duplicate_ingestion_is_atomic(self):
        self.p.ingest(self.records[0]);count=self.p.db.execute('SELECT count(*) FROM chunks').fetchone()[0]
        with self.assertRaises(sqlite3.IntegrityError):self.p.ingest(self.records[0])
        self.assertEqual(self.p.db.execute('SELECT count(*) FROM chunks').fetchone()[0],count)
    def test_synthetic_modalities_and_arabic_retrieval(self):
        self.ingest_all();self.assertTrue(self.p.query('plant_a','الصمام','2026-11-26'))
        self.assertTrue(self.p.query('plant_a','valve','2026-11-26'))
    def test_query_body_is_not_logged(self):
        self.ingest_all();self.p.query('plant_a','PRIVATE_QUERY_SENTINEL','2026-11-26')
        self.assertNotIn('PRIVATE_QUERY_SENTINEL',str(self.p.ledger.execute('SELECT * FROM events').fetchall()))
    def test_unowned_directory_is_rejected(self):
        other=Path(self.temp.name)/'unowned';other.mkdir();(other/'keep.txt').write_text('keep')
        with self.assertRaises(ValueError):Pipeline(other)
        self.assertEqual((other/'keep.txt').read_text(),'keep')
    def test_symlink_snapshot_is_rejected(self):
        outside=Path(self.temp.name)/'outside';outside.write_text('keep');(self.root/'linked.sqlite').symlink_to(outside)
        with self.assertRaises(ValueError):self.p.snapshot('linked')
        self.assertEqual(outside.read_text(),'keep')
    def test_invalid_expiry_fails_without_partial_ingestion(self):
        for expiry in [None,True,'invalid','2026-02-30']:
            r=copy.deepcopy(self.records[0]);r['expires']=expiry
            with self.assertRaises(ValueError):self.p.ingest(r)
        self.assertEqual(self.p.db.execute('SELECT count(*) FROM docs').fetchone()[0],0)
    def test_invalid_policy_does_not_create_storage(self):
        for kwargs in [{'site':''},{'country':None},{'airgap':'false'}]:
            root=Path(self.temp.name)/'invalid'
            with self.assertRaises(ValueError):Pipeline(root,**kwargs)
            self.assertFalse(root.exists())
    def test_network_permission_does_not_relax_site_rule(self):
        other=Pipeline(Path(self.temp.name)/'connected',airgap=False)
        try:
            r=copy.deepcopy(self.records[0]);r['transport']='network';other.ingest(r)
            r.update(id='remote',preprocess_site='CLOUD')
            with self.assertRaisesRegex(ValueError,'BLOCKED'):other.ingest(r)
        finally:other.close()
    def test_toy_similarity_is_bounded_and_not_semantic(self):
        self.assertAlmostEqual(similarity(vector('pump pump'),vector('pump')),1)
        self.assertEqual(similarity(vector('pump'),vector('motor')),0)

if __name__=='__main__':unittest.main()
