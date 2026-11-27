"""Publication integrity, not standard conformity or real facility assurance."""
import json,re,unittest
from pathlib import Path
from urllib.parse import unquote,urlsplit
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]

class Module06Publication(unittest.TestCase):
    def test_syllabus_assessment_source_scope_and_artifacts(self):
        chapter=(ROOT/'chapters/06-governance-responsible-ai-risk.md').read_text()
        self.assertEqual(re.findall(r'^### 6\.([1-7]) ',chapter,re.M),list('1234567'))
        self.assertEqual(len(re.findall(r'^\*\*Q[1-5]\.\*\*',chapter,re.M)),5)
        self.assertEqual(chapter.count('### Q6.'),1)
        self.assertIn('full paid ISO standards not inspected',chapter)
        self.assertIn('independent assessment and manual accessibility review pending',chapter)
        self.assertEqual(len(re.findall(r'^\[\^\w+\]:',chapter,re.M)),7)
        key=(ROOT/'assessments/solutions/06-governance-responsible-ai-risk-solutions.md').read_text()
        for n in range(1,7):self.assertIn(f'## Q{n}.',key)
        self.assertIn('Total 40 points',key)
        self.assertIn('PM deliverable rubric (20 points)',key)
    def test_social_questions_sources_and_no_em_dash(self):
        folder=ROOT/'social/module-06'
        for p in folder.glob('*'):
            if p.is_file():self.assertNotIn('—',p.read_text(),p.name)
        soup=BeautifulSoup((folder/'CAROUSEL.html').read_text(),'html.parser')
        self.assertEqual(len(soup.select('section.slide')),8)
        for section in soup.select('section.slide'):
            self.assertTrue(section.h2.get_text().endswith('?'))
            self.assertEqual(section['aria-labelledby'],section.h2['id'])
        self.assertIn('https://airc.nist.gov/airmf-resources/airmf/5-sec-core/',str(soup))
    def test_built_routes_diagram_and_key_exclusion(self):
        routes=['modules/06-governance-responsible-ai-risk.html','labs/module-06/index.html',
                'social/module-06/POST.html','social/module-06/SLIDES.html','social/module-06/CAROUSEL.html']
        for route in routes:
            p=ROOT/'dist'/route;soup=BeautifulSoup(p.read_text(),'html.parser')
            self.assertNotIn('facilitator solutions and scoring rubric',soup.get_text().lower())
            for a in soup.select('a[href]'):
                u=urlsplit(a['href'])
                if u.scheme or u.netloc or not u.path or u.path.endswith('QUESTIONS.pdf'):continue
                self.assertTrue((p.parent/unquote(u.path)).resolve().exists(),f'{route}: {a["href"]}')
        chapter=BeautifulSoup((ROOT/'dist'/routes[0]).read_text(),'html.parser')
        self.assertIsNotNone(chapter.select_one('figure.diagram-rendered img'))
        self.assertFalse((ROOT/'dist/assessments').exists())
        plan=BeautifulSoup((ROOT/'dist/learning/schedule.html').read_text(),'html.parser')
        self.assertIn('06-governance-responsible-ai-risk.html',str(plan.select_one('[data-module="06"]')))
        self.assertIn('Planned module',plan.select_one('[data-module="12"]').get_text())

if __name__=='__main__':unittest.main()
