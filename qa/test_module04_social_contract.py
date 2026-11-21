"""Source contract for Module 04 public teaching assets; not a manual accessibility audit."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
class Module04PublishingContract(unittest.TestCase):
    def test_carousel_semantics_and_safe_boundaries(self):
        html = (ROOT / "social/module-04/CAROUSEL.html").read_text()
        self.assertEqual(len(re.findall(r'<section class="slide"', html)), 8)
        headings = re.findall(r'<h2 id="q\d+">([^<]+)</h2>', html)
        self.assertEqual(len(headings), 8)
        self.assertEqual(len(set(headings)), 8)
        self.assertTrue(all(h.endswith("?") for h in headings))
        self.assertIn("@media print", html)
        self.assertIn("focus-visible", html)
        self.assertIn("synthetic data", html)
        self.assertNotIn("Facilitator solutions and marking rubric", html)
    def test_post_and_exporter(self):
        post = (ROOT / "social/module-04/POST.md").read_text()
        self.assertTrue(len(post) > 200)
        self.assertNotIn("—", post)
        exporter = (ROOT / "social/module-04/export_pdf.py").read_text()
        self.assertIn("len(pdf.pages) == 8", exporter)
        self.assertIn("Not a tagged PDF", exporter)
    def test_site_wiring(self):
        site = (ROOT / "scripts/build_site.py").read_text()
        self.assertIn("social/module-04/POST.md", site)
        self.assertIn("module-04/CAROUSEL.html", site)
        self.assertIn("'03','04','05'", site)
if __name__ == "__main__":
    unittest.main()
