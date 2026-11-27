"""Inventory and output integrity checks, not legal/source authentication."""
from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote,urlsplit
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]

class Module05LearningContract(unittest.TestCase):
    def test_all_eight_topics_and_separate_six_question_key(self):
        chapter = (ROOT/'chapters/05-laws-regulation-jurisdiction.md').read_text()
        self.assertEqual(re.findall(r'^### 5\.([1-8]) ', chapter,re.M),list('12345678'))
        assessment = chapter.split('## Module 05 knowledge assessment')[1]
        self.assertEqual(len(re.findall(r'^\*\*Q[1-5]\.\*\* ',assessment,re.M)),5)
        self.assertEqual(assessment.count('### Q6.'),1)
        self.assertNotIn('../assessments/solutions/',chapter)
        key = (ROOT/'assessments/solutions/05-laws-regulation-jurisdiction-solutions.md').read_text()
        for i in range(1,7):
            self.assertIn(f'## Q{i}.',key)
        self.assertIn('Total 40 points',key)

    def test_hourly_plan_covers_curriculum_without_duplicate_hours(self):
        plan=json.loads((ROOT/'learning/study-plan.json').read_text())
        self.assertEqual([m['number'] for m in plan['modules']],list(range(1,25)))
        ids=[]
        titles=re.findall(r'^### Module \d{2} — (.+?) \(Week \d+\)',(ROOT/'TOC.md').read_text(),re.M)
        for m,title in zip(plan['modules'],titles,strict=True):
            self.assertEqual(m['title'],title)
            self.assertEqual([h['hour'] for h in m['hours']],list(range(1,11)))
            self.assertTrue(m['scenario'] and m['artifact'])
            for h in m['hours']:
                self.assertTrue(h['activity'] and h['output'])
                ids.append(h['id'])
        self.assertEqual(len(ids),240)
        self.assertEqual(len(set(ids)),240)
        self.assertEqual(len(set(m['artifact'] for m in plan['modules'])),24)

    def test_built_routes_and_solutions_exclusion(self):
        self.assertFalse((ROOT/'dist/assessments').exists())
        files=['modules/05-laws-regulation-jurisdiction.html','labs/module-05/index.html',
               'social/module-05/CAROUSEL.html','social/module-05/POST.html','learning/schedule.html']
        for route in files:
            path=ROOT/'dist'/route
            soup=BeautifulSoup(path.read_text(),'html.parser')
            self.assertNotIn('Facilitator solutions and marking rubric',soup.get_text())
            for link in soup.select('a[href]'):
                parts=urlsplit(link['href'])
                if parts.scheme or parts.netloc or not parts.path or parts.path.endswith('QUESTIONS.pdf'):
                    continue
                target=(path.parent/unquote(parts.path)).resolve()
                self.assertTrue(target.exists(),f'{route}: missing {link["href"]}')
        soup=BeautifulSoup((ROOT/'dist/learning/schedule.html').read_text(),'html.parser')
        self.assertEqual(len(soup.select('[data-module]')),24)
        self.assertEqual(len(soup.select('input[data-hour]')),240)
        self.assertIn('Planned module',soup.select_one('[data-module="12"]').get_text())
        self.assertIn('legal review pending',(ROOT/'dist/modules/05-laws-regulation-jurisdiction.html').read_text())

if __name__=='__main__':
    unittest.main()
