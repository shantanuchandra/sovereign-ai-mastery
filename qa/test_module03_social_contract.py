"""Module 03 social release contract: source-only checks, not visual or AT certification."""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "social/module-03/CAROUSEL.html"
SLIDES = ROOT / "social/module-03/SLIDES.md"
POST = ROOT / "social/module-03/POST.md"
CHAPTER = ROOT / "chapters/03-enterprise-sovereignty-requirements-strategy.md"

class SlideParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.headings = []
        self.ids = set()
        self.references = []
        self._heading = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            assert a["id"] not in self.ids, "duplicate ID: " + a["id"]
            self.ids.add(a["id"])
        if tag == "section" and "slide" in a.get("class", "").split():
            self.sections.append(a)
        if tag == "h2":
            self._heading = True
            self.headings.append("")
        if "aria-labelledby" in a:
            self.references.extend(a["aria-labelledby"].split())
    def handle_endtag(self, tag):
        if tag == "h2":
            self._heading = False
    def handle_data(self, data):
        if self._heading:
            self.headings[-1] += data

class Module03SocialContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = HTML.read_text(encoding="utf-8")
        cls.slides = SLIDES.read_text(encoding="utf-8")
        cls.post = POST.read_text(encoding="utf-8")
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.dom = SlideParser()
        cls.dom.feed(cls.html)

    def test_eight_question_led_accessibly_named_slides(self):
        self.assertEqual(len(self.dom.sections), 8)
        self.assertEqual(len(self.dom.headings), 8)
        self.assertTrue(all(h.strip().endswith("?") for h in self.dom.headings))
        self.assertTrue(all(ref in self.dom.ids for ref in self.dom.references))
        # Each slide must name its own question heading, not an unrelated ID.
        for index, section in enumerate(self.dom.sections, start=1):
            self.assertEqual(section.get("aria-labelledby"), f"q{index}")
            self.assertIn(f'<h2 id="q{index}">', self.html)
        self.assertEqual(len(self.dom.references), 8)
        self.assertEqual(len(set(self.dom.references)), 8)
        self.assertEqual([s.get("id") for s in self.dom.sections],
                         [f"slide-{i}" for i in range(1, 9)])

    def test_no_duplicate_dom_ids(self):
        ids = re.findall(r'\bid="([^"]+)"', self.html)
        self.assertEqual(len(ids), len(set(ids)), "duplicate DOM IDs")

    def test_language_mobile_and_print_basics(self):
        for token in ('lang="en"', 'name="viewport"', '@media print', '@page',
                      ':focus-visible', 'aria-label="Eight teaching slides"'):
            self.assertIn(token, self.html)

    def test_linked_chapter_and_synthetic_disclosure(self):
        self.assertIn('../../chapters/03-enterprise-sovereignty-requirements-strategy.md', self.html)
        self.assertIn('fictional', self.html.lower())
        self.assertIn('fictional', self.post.lower())
        self.assertIn('### 3.7 ', self.chapter)

    def test_no_social_answer_leak_or_em_dash(self):
        for text in (self.html, self.slides, self.post):
            self.assertNotIn('assessments/solutions/', text)
            self.assertNotIn('—', text)

    def test_hard_gate_content_not_diluted(self):
        for phrase in ('FACTORY-A', 'air-gapped', 'remote fallback',
                       'NOT FEASIBLE UNDER CURRENT CONSTRAINTS'):
            self.assertIn(phrase.lower(), self.html.lower())

if __name__ == "__main__":
    unittest.main()
