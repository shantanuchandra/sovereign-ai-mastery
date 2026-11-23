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
from xml.etree import ElementTree as ET

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

    def test_module05_is_not_marked_ready_in_unpublished_reader(self):
        """A built draft may be navigable without claiming release approval."""
        current = self.soup.select_one('a.toc-chapter.is-active[href$="05-laws-regulation-jurisdiction.html"]')
        self.assertIsNotNone(current)
        self.assertIsNone(current.select_one('.read-dot[title="Chapter ready"]'))
        self.assertIn("DRAFT", self.article.get_text(" ", strip=True).upper())
        self.assertIn("MODULE 04", self.article.get_text(" ", strip=True).upper())

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

    def test_svg_teaches_vendor_data_and_fail_closed_release_decision(self):
        tree = ET.parse(DIST / "diagrams/module-05-control-graph.svg")
        svg = tree.getroot()
        ns = "{http://www.w3.org/2000/svg}"
        self.assertEqual(svg.tag, ns + "svg")
        self.assertEqual(svg.get("role"), "img")
        title = svg.find(ns + "title")
        desc = svg.find(ns + "desc")
        self.assertIsNotNone(title)
        self.assertIsNotNone(desc)
        self.assertIn("hard gate", (desc.text or "").lower())
        self.assertIn("no numeric score override", (desc.text or "").lower())
        labels = " ".join(x.strip() for x in svg.itertext() if x)
        for term in ("Legal entity", "Counsel", "Data + derivatives",
                     "Vendor / control paths", "Observed evidence",
                     "Hard release gate", "HOLD / BLOCKED",
                     "Candidate for release review", "physical air gap"):
            self.assertIn(term, labels)

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


    def test_release_candidate_lab_command_manifest(self):
        """Check learner-shown commands against actual shipped files, not prose promises.

        This validates the draft bundle only. It does not attest to deployed Pages.
        """
        import shlex

        readme = (ROOT / "labs/module-05/README.md").read_text(encoding="utf-8")
        lab_page = (DIST / "labs/module-05/index.html")
        self.assertTrue(lab_page.is_file(), "Lab landing page not shipped")
        rendered = BeautifulSoup(lab_page.read_text(encoding="utf-8"), "html.parser")
        main = rendered.select_one("main")
        self.assertIsNotNone(main, "Lab landing page has no learner main landmark")
        commands = []
        for block in re.findall(r"~~~bash\s*\n(.*?)\n~~~", readme, re.S):
            for line in block.splitlines():
                line = line.strip()
                if line.startswith(("python3 ", "python ")):
                    commands.append(line)
        self.assertGreaterEqual(len(commands), 2, "Missing runnable lab command examples")
        rendered_text = main.get_text(" ", strip=True)
        for command in commands:
            with self.subTest(command=command):
                self.assertIn(command, rendered_text, "README command absent from built lab page")
                args = shlex.split(command)
                for token in args[1:]:
                    if token.startswith("labs/module-05/"):
                        target = (DIST / token).resolve()
                        self.assertTrue(target.is_relative_to(DIST.resolve()))
                        self.assertTrue(target.is_file(), f"Command target not shipped: {token}")
                        self.assertTrue((ROOT / token).is_file(), f"Command target missing in source: {token}")
                if "-s" in args:
                    folder = args[args.index("-s") + 1]
                    self.assertTrue((DIST / folder).is_dir(), f"Test discovery directory not shipped: {folder}")

        # Fail if the learner lab page links to a missing asset or any facilitator key.
        for node in main.select("a[href]"):
            href = node["href"]
            self.assertNotIn("assessments/solutions/", href)
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (lab_page.parent / unquote(parts.path)).resolve()
            self.assertTrue(target.is_relative_to(DIST.resolve()), f"Escaping lab route: {href}")
            self.assertTrue(target.is_file(), f"Broken learner lab link: {href}")
        for page in (PAGE, lab_page):
            markup = page.read_text(encoding="utf-8")
            self.assertNotIn("assessments/solutions/05-laws-regulation-jurisdiction-solutions", markup)
        self.assertFalse((DIST / "assessments/solutions/05-laws-regulation-jurisdiction-solutions.md").exists())

    def test_generated_site_has_no_facilitator_solution_payload_or_links(self):
        """The draft website must not expose any module's facilitator answers.

        Check the entire built artifact, not only the Module 05 reader. A
        navigation change or a copy rule can leak keys on unrelated routes.
        This is a static bundle check, not a deployed-site security audit.
        """
        solution_dir = DIST / "assessments" / "solutions"
        self.assertFalse(solution_dir.exists(),
                         "Facilitator solution directory shipped in learner bundle")
        leaked = []
        for file in DIST.rglob("*"):
            if not file.is_file():
                continue
            relative = file.relative_to(DIST).as_posix()
            if re.search(r"(?:^|/)(?:solutions|answer[-_]?keys?)(?:/|$)|(?:^|/)[^/]+[-_](?:solutions?|answer[-_]?keys?)(?:\.[^/]+)?$", relative, re.I):
                leaked.append(f"Facilitator-looking file: {relative}")
            if file.suffix.lower() != ".html":
                continue
            soup = BeautifulSoup(file.read_text(encoding="utf-8"), "html.parser")
            for a in soup.select("a[href]"):
                target = unquote(urlsplit(a["href"]).path).lower()
                if re.search(r"(?:^|/)(?:assessments/solutions|answer[-_]?keys?)(?:/|$)|(?:^|/)[^/]+[-_](?:solutions?|answer[-_]?keys?)(?:\.[^/]+)?$", target):
                    leaked.append(f"Facilitator link in {relative}: {a['href']}")
        self.assertEqual(leaked, [], "Learner bundle exposed facilitator resources")

    def test_facilitator_key_does_not_leak_into_reader(self):
        self.assertFalse((DIST / "assessments/solutions/05-laws-regulation-jurisdiction-solutions.md").exists())
        self.assertNotIn("Facilitator solutions and scoring rubric", self.html)
        self.assertNotIn("**Worked answer:**", self.html)
        self.assertNotIn("Q6 | Physical-site and air-gap RCA (18 points)", self.html)
        for a in self.article.select("a[href]"):
            self.assertNotIn("/assessments/solutions/", a["href"])
        self.assertIn("facilitator-only key", self.article.get_text(" ", strip=True))

    def test_withdrawn_legal_pinpoints_do_not_reappear_in_teaching_assets(self):
        """Guard withdrawn legal citations in learner and facilitator teaching.

        This checks known-invalid unqualified references, not legal validity.
        Historical source-comparison reviews intentionally remain outside scope.
        """
        teaching = (
            ROOT / "chapters/05-laws-regulation-jurisdiction.md",
            ROOT / "assessments/solutions/05-laws-regulation-jurisdiction-solutions.md",
            ROOT / "labs/module-05/README.md",
            ROOT / "labs/module-05/control_map.json",
            ROOT / "social/module-05/CAROUSEL.html",
            ROOT / "social/module-05/POST.md",
        )
        withdrawn = (
            re.compile(r"(?i)ADGM[^\n]{0,110}\bPart\s+6\b"),
            re.compile(r"(?i)ADGM[^\n]{0,110}\bArticle\s+42\s*\(2\)"),
            re.compile(r"(?i)transfer.regulation[^\n]{0,100}\bArticles?\s+6\s*[-–]\s*7\b"),
        )
        # Mutation probes make sure the guard actually rejects known unsafe
        # assertions. They also catch accidental regex over-escaping.
        known_bad = (
            "ADGM international transfers are governed by Part 6",
            "ADGM law Article 42(2) automatically permits transfers",
            "Saudi transfer regulation Articles 6-7 always apply",
        )
        for sample in known_bad:
            self.assertTrue(any(pattern.search(sample) for pattern in withdrawn),
                            f"Withdrawn-citation guard failed its mutation probe: {sample}")
        known_safe = (
            "ADGM Part V and Article 42(3)(c) appear in guidance, pending consolidation",
            "Saudi transfer regulation article numbering conflicts across English editions",
        )
        for sample in known_safe:
            self.assertFalse(any(pattern.search(sample) for pattern in withdrawn),
                             f"Withdrawn-citation guard rejected qualified text: {sample}")
        violations = []
        for file in teaching:
            self.assertTrue(file.is_file(), f"Missing teaching asset: {file}")
            for number, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
                for pattern in withdrawn:
                    if pattern.search(line):
                        violations.append(f"{file.relative_to(ROOT)}:{number}: {line[:150]}")
        self.assertEqual(violations, [], "Withdrawn legal pinpoint resurfaced")

    def test_no_unqualified_approved_claim(self):
        text = self.article.get_text(" ", strip=True)
        self.assertIn("independent", text.lower())
        self.assertIn("not a legal", text.lower())
        self.assertRegex(text, r"(?i)(draft|unpublished)")
        self.assertIn("physically", text.lower())
        self.assertIn("blocked", text.lower())


if __name__ == "__main__":
    unittest.main()
