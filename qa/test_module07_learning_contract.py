"""Publication integrity, not infrastructure or legal assurance."""
from pathlib import Path
from urllib.parse import urlsplit,unquote
import re,unittest
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
class ArchitecturePublication(unittest.TestCase):
    def test_topics_and_separate_key(self):
        c=(ROOT/'chapters/07-end-to-end-sovereign-ai-stack-reference-architecture.md').read_text()
        self.assertEqual(re.findall(r'^### 7\.([1-7]) ',c,re.M),list('1234567'))
        self.assertEqual(len(re.findall(r'^\*\*Q[1-5]\.\*\*',c,re.M)),5)
        self.assertIn('### Q6.',c)
        self.assertEqual(len(re.findall(r'^\[\^\w+\]:',c,re.M)),3)
        k=(ROOT/'assessments/solutions/07-end-to-end-sovereign-ai-stack-reference-architecture-solutions.md').read_text()
        for n in range(1,7):self.assertIn(f'## Q{n}.',k)
        self.assertIn('Total 40 points',k)
    def test_routes_and_key_exclusion(self):
        self.assertFalse((ROOT/'dist/assessments').exists())
        routes=['modules/07-end-to-end-sovereign-ai-stack-reference-architecture.html','labs/module-07/index.html','labs/module-07/ADR.html','social/module-07/POST.html','social/module-07/CAROUSEL.html']
        for r in routes:
            p=ROOT/'dist'/r;s=BeautifulSoup(p.read_text(),'html.parser')
            for a in s.select('a[href]'):
                u=urlsplit(a['href'])
                if u.scheme or u.netloc or not u.path or u.path.endswith('QUESTIONS.pdf'):continue
                self.assertTrue((p.parent/unquote(u.path)).resolve().exists(),(r,a['href']))
        s=BeautifulSoup((ROOT/'dist'/routes[0]).read_text(),'html.parser')
        self.assertIsNotNone(s.select_one('figure.diagram-rendered img'))
        self.assertIn('independent assessment and manual accessibility review pending',s.get_text())
    def test_social_questions_and_style(self):
        for name in ['CAROUSEL.html','POST.md','SLIDES.md']:
            text=(ROOT/'social/module-07'/name).read_text();self.assertNotIn('—',text)
        s=BeautifulSoup((ROOT/'social/module-07/CAROUSEL.html').read_text(),'html.parser')
        self.assertEqual(len(s.select('section.slide h2')),8)
        self.assertTrue(all(h.get_text().endswith('?') for h in s.select('section.slide h2')))
if __name__=='__main__':unittest.main()
