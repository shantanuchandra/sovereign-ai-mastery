"""Preview-only Module 05 reader integration checks; run after scripts/build_site.py.

No deployment or publication. These tests prove local generated files, routes and
basic static semantics, not legal correctness, accessible reading order or actual
browser/screen-reader behaviour.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
PAGE = DIST / "modules/05-laws-regulation-jurisdiction.html"

EXPECTED = (
    "5.1 UAE federal personal data protection framework",
    "5.2 DIFC and ADGM data protection regimes",
    "5.3 Sector, government and critical infrastructure considerations",
    "5.4 Saudi PDPL and data transfer considerations",
    "5.5 GDPR, EU AI Act and global comparisons",
    "5.6 Residency, transfers, contracts, subprocessors and lawful access",
    "5.7 How legal jurisdiction differs from operational or technical control",
    "5.8 Converting legal questions into reviewable requirements and evidence",
)


class DraftReaderContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not PAGE.is_file():
            raise RuntimeError("Run python scripts/build_site.py before reader checks")
        cls.html = PAGE.read_text(encoding="utf-8")
        cls.soup = BeautifulSoup(cls.html, "html.parser")
        cls.article = cls.soup.select_one("main .prose")

    def test_not_the_old_web_first_exemplar(self):
        self.assertIsNotNone(self.article)
        headings = [h.get_text(" ", strip=True) for h in self.article.select("h3")]
        for section in EXPECTED:
            self.assertIn(section, headings, f"Missing TOC teaching section: {section}")
        self.assertIn("MODULE 04 IS STILL HOLD", self.article.get_text(" ", strip=True).upper())
        self.assertIn("NEEDS_COUNSEL", self.article.get_text(" ", strip=True))

    def test_reader_renders_static_svg_not_raw_mermaid_only(self):
        diagram = self.article.select_one("figure.diagram-rendered")
        self.assertIsNotNone(diagram, "Website-only Mermaid fence is insufficient")
        svg = diagram.select_one('img[src$="module-05-control-graph.svg"]')
        self.assertIsNotNone(svg, "Missing linked static SVG")
        self.assertTrue(svg.get("alt"), "Diagram image lacks alt text")
        self.assertIsNotNone(diagram.select_one("figcaption"))
        self.assertIsNotNone(diagram.select_one("details.diagram-source code.language-mermaid"))
        self.assertTrue((DIST / "diagrams/module-05-control-graph.svg").is_file())

    def test_eight_sections_accessible_from_page_headings(self):
        headings = self.article.select("h1,h2,h3")
        self.assertTrue(headings)
        identifiers = [tag.get("id") for tag in headings]
        self.assertTrue(all(identifiers), "Heading lacks an in-page anchor")
        self.assertEqual(len(identifiers), len(set(identifiers)))
        for label in EXPECTED:
            h = next(h for h in headings if h.get_text(" ", strip=True) == label)
            self.assertEqual(h.name, "h3")

    def test_local_learner_resources_exist(self):
        # Validate links visible inside the Module 05 learner content and
        # chapter-next affordances, not the entire legacy repository.
        containers = [self.article, self.soup.select_one("section.chapter-next")]
        broken = []
        for parent in containers:
            if parent is None:
                continue
            for node in parent.select("[href],[src]"):
                for attr in ("href", "src"):
                    link = node.get(attr)
                    if not link:
                        continue
                    parts = urlsplit(link)
                    if parts.scheme or parts.netloc or link.startswith(("mailto:", "tel:", "data:")):
                        continue
                    if not parts.path:
                        if parts.fragment and not self.soup.find(id=unquote(parts.fragment)):
                            broken.append(f"Fragment #{parts.fragment}")
                        continue
                    dest = (PAGE.parent / unquote(parts.path)).resolve()
                    if not dest.is_relative_to(DIST.resolve()) or not dest.is_file():
                        broken.append(f"{attr}: {link}")
                    elif parts.fragment:
                        target_soup = self.soup if dest == PAGE.resolve() else None
                        # Inspect same-page named anchors only. Other routes are
                        # checked for existence, not their dynamic anchors.
                        if target_soup is not None and not target_soup.find(id=unquote(parts.fragment)):
                            broken.append(f"Missing anchor {parts.fragment}")
        self.assertEqual(broken, [], "Broken draft reader links/resources: " + "; ".join(broken))

    def test_labs_ship_as_real_working_files_not_prose_only(self):
        for route in ("labs/module-05/index.html",
                      "labs/module-05/control_map.json",
                      "labs/module-05/validate.py",
                      "labs/module-05/test_validate.py",
                      "labs/module-05/README.md",
                      "social/module-05/CAROUSEL.html",
                      "social/module-05/POST.html"):
            with self.subTest(route=route):
                self.assertTrue((DIST / route).is_file(), f"Missing promised lab/social route: {route}")
        self.assertIn("python3 labs/module-05/validate.py",
                      (DIST / "labs/module-05/index.html").read_text(encoding="utf-8"))

    def test_facilitator_key_does_not_leak_into_reader(self):
        self.assertFalse((DIST / "assessments/solutions/05-laws-regulation-jurisdiction-solutions.md").exists())
        self.assertNotIn("Facilitator solutions and scoring rubric", self.html)
        self.assertNotIn("**Worked answer:**", self.html)
        self.assertNotIn("Q6 | Physical-site and air-gap RCA (18 points)", self.html)
        for a in self.article.select("a[href]"):
            self.assertNotIn("/assessments/solutions/", a["href"])
        self.assertIn("facilitator-only key", self.article.get_text(" ", strip=True))

    def test_no_unqualified_approved_claim(self):
        text = self.article.get_text(" ", strip=True)
        self.assertIn("independent", text.lower())
        self.assertIn("not a legal", text.lower())
        self.assertRegex(text, r"(?i)(draft|unpublished)")
        self.assertIn("physically", text.lower())
        self.assertIn("blocked", text.lower())


if __name__ == "__main__":
    unittest.main()
