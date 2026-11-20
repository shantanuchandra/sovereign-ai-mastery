#!/usr/bin/env python3
"""Static Module 02 carousel print/accessibility contract (no browser or PDF engine).

Run: python -m unittest discover -s social/module-02 -p 'test_*.py' -v
These tests cannot prove visual fit, accessible reading order, or PDF export success.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

SOURCE = Path(__file__).with_name("CAROUSEL.html")


class DeckParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.sections = []
        self.headings = []
        self.ids = set()
        self.duplicate_ids = []
        self.links = []
        self.buttons = []
        self.current_section = None
        self.current_heading = False
        self.heading_text = []
        self.lang = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html":
            self.lang = a.get("lang")
        if "id" in a:
            if a["id"] in self.ids:
                self.duplicate_ids.append(a["id"])
            self.ids.add(a["id"])
        if tag == "section" and "slide" in a.get("class", "").split():
            self.current_section = a
            self.sections.append(a)
        if tag == "h2":
            self.current_heading = True
            self.heading_text = []
        if tag == "a":
            self.links.append(a)
        if tag == "button":
            self.buttons.append(a)

    def handle_data(self, data):
        if self.current_heading:
            self.heading_text.append(data)

    def handle_endtag(self, tag):
        if tag == "h2":
            self.headings.append("".join(self.heading_text).strip())
            self.current_heading = False
        if tag == "section":
            self.current_section = None


class CarouselContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = SOURCE.read_text(encoding="utf-8")
        cls.deck = DeckParser()
        cls.deck.feed(cls.source)

    def test_eight_question_slides_and_unique_heading_targets(self):
        self.assertEqual(8, len(self.deck.sections))
        self.assertEqual(8, len(self.deck.headings))
        self.assertTrue(all(h.endswith("?") for h in self.deck.headings))
        self.assertFalse(self.deck.duplicate_ids)
        for i, section in enumerate(self.deck.sections, 1):
            self.assertEqual(f"q{i}", section.get("aria-labelledby"))
            self.assertIn(f"q{i}", self.deck.ids)

    def test_language_and_action_accessibility(self):
        self.assertEqual("en", self.deck.lang)
        self.assertEqual(1, len(self.deck.buttons))
        self.assertIn("PDF", self.deck.buttons[0].get("aria-label", ""))
        self.assertIn("button:focus-visible", self.source)
        self.assertIn("a:focus-visible", self.source)
        self.assertTrue(any(x.get("href", "").startswith("https://") for x in self.deck.links))

    def test_print_pages_and_no_page_nine(self):
        self.assertRegex(self.source, r"@page\s*\{[^}]*size:\s*8in\s+10in")
        self.assertRegex(self.source, r"@media print\s*\{")
        self.assertRegex(self.source, r"\.slide\s*\{[^}]*width:\s*8in;[^}]*height:\s*10in")
        self.assertIn(".slide:last-child{break-after:auto", self.source)
        self.assertIn(".toolbar,.sources{display:none!important}", self.source)
        self.assertIn("window.print()", self.source)

    def test_explicit_boundaries_and_source(self):
        for phrase in ("FACTORY-A", "air-gap", "Microsoft Learn", "Fictional", "BLOCKED"):
            self.assertIn(phrase.lower(), self.source.lower())
        self.assertIn("https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types", self.source)
        self.assertIn("PDF export, visual clipping and assistive-technology QA must be independently checked", self.source)

    def test_no_external_active_assets_or_user_data(self):
        self.assertNotRegex(self.source, r"<script\b")
        self.assertNotRegex(self.source, r"<iframe\b")
        self.assertNotRegex(self.source, r"<form\b")
        self.assertNotRegex(self.source, r"(?i)(?:api[_-]?key|bearer\s+[a-z0-9])")

    def test_mobile_readability_reflow_contract(self):
        # Source-level guard only; rendered 200% zoom and keyboard QA still required.
        mobile = self.source.split("@media(max-width:620px)", 1)[1].split("@media(max-width:400px)", 1)[0]
        self.assertIn("aspect-ratio:auto", mobile)
        self.assertIn("height:auto", mobile)
        self.assertIn("overflow:visible", mobile)
        self.assertIn("font-size:12px", mobile)
        self.assertIn("clamp(14px,3.6vw,17px)", mobile)

    def test_overflow_is_documented_as_unverified(self):
        # An overflow-hidden slide can clip text; static tests do not establish fit.
        self.assertIn("overflow:hidden", self.source)
        self.assertIn("visual clipping", self.source)


if __name__ == "__main__":
    unittest.main()
