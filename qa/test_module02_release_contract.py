"""Source-only regression checks. They do NOT replace independent source or browser review."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters/02-classifications-components-maturity-models.md"
SOLUTION = ROOT / "assessments/solutions/02-classifications-components-maturity-models-solutions.md"
DECK = ROOT / "social/module-02/CAROUSEL.html"
POST = ROOT / "social/module-02/POST.md"
LEDGER = ROOT / "qa/module-02-source-audit-ledger.md"
ENGINE = ROOT / "learning/studio-engine.mjs"


class Module02ReleaseContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.solution = SOLUTION.read_text(encoding="utf-8")
        cls.deck = DECK.read_text(encoding="utf-8")
        cls.post = POST.read_text(encoding="utf-8")
        cls.ledger = LEDGER.read_text(encoding="utf-8")
        cls.engine = ENGINE.read_text(encoding="utf-8")

    def test_exactly_seven_ordered_toc_sections(self):
        heads = [int(x) for x in re.findall(r"^### 2\.([1-7]) ", self.chapter, re.M)]
        self.assertEqual(heads, list(range(1, 8)))

    def test_five_knowledge_questions_and_sixth_rca(self):
        assessment = self.chapter.split("## 2A. Knowledge assessment", 1)[1]
        self.assertEqual(len(re.findall(r"^\*\*[1-5]\. ", assessment, re.M)), 5)
        for item in ["Question 6:", "Direct cause", "Contributing", "Retest",
                     "BLOCKED", "physically air-gapped"]:
            self.assertIn(item.lower(), assessment.lower())

    def test_actual_provider_source_is_not_equated_with_certification(self):
        q5 = self.chapter.split("**5. Real product", 1)[1].split("### Question 6", 1)[0]
        self.assertIn("Standard and Regional Provisioned", q5)
        self.assertIn("region-specific deployment", q5)
        self.assertIn("Global types: May be processed in any Azure region", q5)
        self.assertIn("single physical factory premises", q5)
        self.assertNotIn("Azure-geography-based deployment", q5)
        self.assertIn("Data Zone", self.solution)
        self.assertIn("deployment region", self.solution)

    def test_independent_references_are_course_context_not_sovereignty_standards(self):
        for link in ["airc.nist.gov/airmf-resources/airmf/5-sec-core/",
                     "csrc.nist.gov/pubs/sp/800/207/final",
                     "csrc.nist.gov/pubs/sp/800/161/r1/upd1/final",
                     "opensource.org/ai/open-source-ai-definition"]:
            self.assertIn(link, self.chapter)
        self.assertIn("course-authored", self.chapter.lower())

    def test_audit_inventory_covers_every_toc_section_and_vendor_example(self):
        for x in ["2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "A01-Q5"]:
            self.assertIn(x, self.ledger)
        self.assertIn("primary", self.ledger.lower())

    def test_site_and_air_gap_hard_gates_are_preserved(self):
        section = self.chapter.split("### 2.7 ", 1)[1]
        self.assertIn("specific", section)
        self.assertIn("no inbound or outbound network connectivity", section)
        self.assertIn("NOT FEASIBLE UNDER CURRENT CONSTRAINTS", section)
        self.assertIn("BLOCKED", section)

    def test_studio_dropdown_labels_match_exercise(self):
        labels = ["Strict on-premises IP research assistant",
                  "Single premises only; no data or derivatives may leave",
                  "Air-gapped factory operations",
                  "General internet access including external service endpoints"]
        for label in labels:
            self.assertIn(label, self.chapter)
            self.assertIn(label, self.engine)

    def test_carousel_does_not_leak_answers_or_use_banned_punctuation(self):
        self.assertNotIn("Facilitator solutions and marking rubric", self.deck)
        self.assertNotIn("Facilitator solutions and marking rubric", self.post)
        self.assertNotIn("\u2014", self.post)
        self.assertNotIn("\u2014", self.deck)
        self.assertIn("DECISION TEST", self.deck)
        self.assertIn("Microsoft Learn", self.deck)

    def test_solution_key_includes_lab_rubric_and_routing_fallback_rca(self):
        for label in ["CORP-02", "PLANT-02", "OT-02", "LIC-02",
                      "PM deliverable rubric", "Direct cause", "retest"]:
            self.assertIn(label.lower(), self.solution.lower())


if __name__ == "__main__":
    unittest.main()
