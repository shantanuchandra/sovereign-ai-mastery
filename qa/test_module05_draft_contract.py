"""Module 05 draft contracts. Structural QA, not legal or accessibility sign-off."""
from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters/05-laws-regulation-jurisdiction.md"
KEY = ROOT / "assessments/solutions/05-laws-regulation-jurisdiction-solutions.md"
CAROUSEL = ROOT / "social/module-05/CAROUSEL.html"
POST = ROOT / "social/module-05/POST.md"


class Module05DraftContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.solutions = KEY.read_text(encoding="utf-8")
        cls.carousel = CAROUSEL.read_text(encoding="utf-8")
        cls.post = POST.read_text(encoding="utf-8")

    def test_all_eight_curriculum_legal_headers(self):
        for label in ("5.1 UAE federal", "5.2 DIFC and ADGM",
                      "5.3 Sector", "5.4 Saudi PDPL", "5.5 GDPR",
                      "5.6 Residency", "5.7 How legal jurisdiction",
                      "5.8 Converting legal questions"):
            self.assertIn(label, self.chapter)
        self.assertEqual(len(re.findall(r"^### 5\.\d ", self.chapter, re.M)), 8)

    def test_separate_assessment_and_rubric(self):
        questions = re.findall(r"^\d\. \*\*Q[1-6]", self.chapter, re.M)
        self.assertEqual(len(questions), 6)
        self.assertIn("Total **40 points**", self.solutions)
        self.assertIn("18-point rubric", self.solutions)
        self.assertNotIn("**Worked answer:**", self.chapter)
        self.assertIn("Safety override", self.solutions)

    def test_all_cited_chapter_footnotes_defined(self):
        citations = set(re.findall(r"\[\^([^\]]+)\]", self.chapter))
        definitions = re.findall(r"^\[\^([^\]]+)\]:", self.chapter, re.M)
        self.assertEqual(len(definitions), len(set(definitions)))
        self.assertEqual(citations, set(definitions))

    def test_unverified_legal_scope_remains_open(self):
        for term in ("NEEDS_COUNSEL", "legal opinion",
                     "Module 04 is still HOLD", "separate branch",
                     "NOT COMPLETED", "named physical"):
            self.assertIn(term.lower(), self.chapter.lower())
        self.assertIn("no inbound or outbound", self.chapter.lower())
        self.assertIn("firewall", self.chapter.lower())

    def test_evidence_stays_source_bounded(self):
        for domain in ("uaelegislation.gov.ae", "difc.com", "adgm.com",
                       "dgp.sdaia.gov.sa", "eur-lex.europa.eu",
                       "ai-act-service-desk.ec.europa.eu"):
            self.assertIn(domain, self.chapter)
        self.assertIn("full consolidated text/version not independently reviewed", self.chapter)

    def test_eight_question_slides_with_print_and_focus(self):
        html = self.carousel
        slides = re.findall(r'<section class="slide', html)
        self.assertEqual(len(slides), 8)
        titles = re.findall(r'<h2 class="question">([\s\S]*?)</h2>', html)
        self.assertEqual(len(titles), 8)
        normalized = [re.sub(r"<[^>]+>", " ", x).replace("?", "?").strip() for x in titles]
        self.assertEqual(len(set(normalized)), 8)
        self.assertTrue(all(x.endswith("?") for x in normalized), normalized)
        self.assertIn("@page{size:8in 10in", html)
        self.assertIn("@media print", html)
        self.assertNotIn("—", html)

    def test_post_has_provenance_and_no_social_dashes(self):
        self.assertIn("DRAFT", self.post)
        self.assertIn("fictional", self.post)
        self.assertIn("difc.com", self.post)
        self.assertIn("adgm.com", self.post)
        self.assertNotIn("—", self.post)

    def test_lab_and_exporter_are_kept_separate(self):
        self.assertTrue((ROOT / "labs/module-05/validate.py").exists())
        self.assertTrue((ROOT / "labs/module-05/test_validate.py").exists())
        exporter = (ROOT / "social/module-05/export_pdf.py").read_text(encoding="utf-8")
        self.assertIn("PdfReader", exporter)
        self.assertIn("len(pdf.pages) == 8", exporter)
        self.assertIn("NOT a tagged PDF", exporter)


if __name__ == "__main__":
    unittest.main()
