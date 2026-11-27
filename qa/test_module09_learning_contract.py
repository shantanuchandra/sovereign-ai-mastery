"""Publication integrity, not infrastructure or legal assurance."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,unittest
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
class ComputePublication(unittest.TestCase):
    def test_topics_and_separate_key(self):
        c=(ROOT/'chapters/09-gpus-compute-networking-platform-engineering.md').read_text()
        self.assertEqual(re.findall(r'^### 9\.([1-7]) ',c,re.M),list('1234567'))
        self.assertEqual(len(re.findall(r'^\*\*Q[1-5]\.\*\*',c,re.M)),5)
        self.assertIn('### Q6.',c)
        self.assertEqual(len(re.findall(r'^\[\^\w+\]:',c,re.M)),5)
        k=(ROOT/'assessments/solutions/09-gpus-compute-networking-platform-engineering-solutions.md').read_text()
        for n in range(1,7):self.assertIn(f'## Q{n}.',k)
        self.assertIn('Total 40 points',k)
        ontology=(ROOT/'taxonomy/ontology.yaml').read_text()
        for entity in ['ComputeProfile','CapacityBudget','LoadObservation','ReplicaPlan']:
            self.assertIn('  - '+entity+'\n',ontology)
            self.assertIn('| '+entity+' |',(ROOT/'taxonomy/ONTOLOGY.md').read_text())
    def test_routes_and_key_exclusion(self):
        self.assertFalse((ROOT/'dist/assessments').exists())
        routes=['modules/09-gpus-compute-networking-platform-engineering.html','labs/module-09/index.html','labs/module-09/WORKSHEET.html','social/module-09/POST.html','social/module-09/CAROUSEL.html']
        for r in routes:
            p=ROOT/'dist'/r;s=BeautifulSoup(p.read_text(),'html.parser')
            for a in s.select('a[href]'):
                u=urlsplit(a['href'])
                if u.scheme or u.netloc or not u.path or u.path.endswith('QUESTIONS.pdf'):continue
                self.assertTrue((p.parent/unquote(u.path)).resolve().exists(),(r,a['href']))
        s=BeautifulSoup((ROOT/'dist'/routes[0]).read_text(),'html.parser')
        self.assertIsNotNone(s.select_one('figure.diagram-rendered img'))
        plan=BeautifulSoup((ROOT/'dist/learning/schedule.html').read_text(),'html.parser')
        self.assertIn('09-gpus-compute-networking-platform-engineering.html',str(plan.select_one('[data-module="09"]')))
        self.assertIn('Planned module',plan.select_one('[data-module="12"]').get_text())
        self.assertEqual(len(plan.select('input[type="checkbox"]')),240)
        self.assertIn('independent assessment and manual accessibility review pending',s.get_text())
    def test_social_questions_and_style(self):
        for name in ['CAROUSEL.html','POST.md','SLIDES.md']:
            text=(ROOT/'social/module-09'/name).read_text();self.assertNotIn('—',text)
        s=BeautifulSoup((ROOT/'social/module-09/CAROUSEL.html').read_text(),'html.parser')
        self.assertEqual(len(s.select('section.slide h2')),8)
        self.assertTrue(all(h.get_text().endswith('?') for h in s.select('section.slide h2')))
if __name__=='__main__':unittest.main()
