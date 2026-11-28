"""Cross-module reader integrity and assessment separation, not deployment assurance."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,unittest
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
PACKAGES=[('12','12-sovereign-rag-systems','REQUIREMENTS',['RetrievalPolicy','RetrievedContext','GroundingCheck','RetrievalIndex']),('13','13-fine-tuning-optimization-evaluation','TRADEOFF_MEMO',['OptimizationExperiment','ExperimentVariant','MeasurementPopulation']),('14','14-agents-apis-enterprise-integrations','CONTROL_SPEC',['AgentIdentity','ToolAction','ApprovalGrant','InvocationRecord'])]
class ModelsAgentsPublication(unittest.TestCase):
    def test_syllabus_assessments_and_ontology(self):
        ontology=(ROOT/'taxonomy/ontology.yaml').read_text()
        explainer=(ROOT/'taxonomy/ONTOLOGY.md').read_text()
        for n,slug,pm,entities in PACKAGES:
            with self.subTest(module=n):
                text=(ROOT/'chapters'/f'{slug}.md').read_text()
                self.assertEqual(re.findall(r'^### '+n+r'\.([1-7]) ',text,re.M),list('1234567'))
                self.assertEqual(len(re.findall(r'^\*\*Q[1-5]\.\*\*',text,re.M)),5)
                self.assertIn('### Q6.',text)
                key=(ROOT/'assessments/solutions'/f'{slug}-solutions.md').read_text()
                for q in range(1,7):self.assertIn(f'## Q{q}.',key)
                self.assertIn('Total 40 points',key)
                for entity in entities:
                    self.assertIn('  - '+entity+'\n',ontology)
                    self.assertIn('| '+entity+' |',explainer)
    def test_reader_routes_diagrams_and_study_links(self):
        self.assertFalse((ROOT/'dist/assessments').exists())
        plan=BeautifulSoup((ROOT/'dist/learning/schedule.html').read_text(),'html.parser')
        self.assertEqual(len(plan.select('input[type="checkbox"]')),240)
        self.assertIn('Planned module',plan.select_one('[data-module="21"]').get_text())
        for n,slug,pm,_ in PACKAGES:
            routes=[f'modules/{slug}.html',f'labs/module-{n}/index.html',f'labs/module-{n}/{pm}.html',f'social/module-{n}/POST.html',f'social/module-{n}/CAROUSEL.html']
            for route in routes:
                p=ROOT/'dist'/route;soup=BeautifulSoup(p.read_text(),'html.parser')
                self.assertNotIn('Facilitator solutions and marking rubric',soup.get_text())
                for a in soup.select('a[href]'):
                    u=urlsplit(a['href'])
                    if u.scheme or u.netloc or not u.path or u.path.endswith('QUESTIONS.pdf'):continue
                    self.assertTrue((p.parent/unquote(u.path)).resolve().exists(),(route,a['href']))
            chapter=BeautifulSoup((ROOT/'dist'/routes[0]).read_text(),'html.parser')
            self.assertIsNotNone(chapter.select_one('figure.diagram-rendered img'))
            self.assertIn(f'{slug}.html',str(plan.select_one(f'[data-module="{n}"]')))
            self.assertIn('independent',chapter.get_text().lower())
    def test_ontology_relationships_have_declared_endpoints(self):
        text=(ROOT/'taxonomy/ontology.yaml').read_text()
        classes=set(re.findall(r'^  - (\w+)$',text.split('classes:',1)[1].split('data_lifecycle_properties:',1)[0],re.M))
        relationships=re.findall(r'^  - \[(\w+), (\w+), (\w+)\]$',text,re.M)
        self.assertTrue(relationships)
        for source,relation,target in relationships:
            self.assertIn(source,classes,(source,relation,target))
            self.assertIn(target,classes,(source,relation,target))

    def test_social_questions_and_style(self):
        for n,_,_,_ in PACKAGES:
            for name in ['CAROUSEL.html','POST.md','SLIDES.md']:
                self.assertNotIn('—',(ROOT/'social'/f'module-{n}'/name).read_text())
            soup=BeautifulSoup((ROOT/'social'/f'module-{n}/CAROUSEL.html').read_text(),'html.parser')
            heads=soup.select('section.slide h2')
            self.assertEqual(len(heads),8)
            self.assertTrue(all(h.get_text().strip().endswith('?') for h in heads))
if __name__=='__main__':unittest.main()
