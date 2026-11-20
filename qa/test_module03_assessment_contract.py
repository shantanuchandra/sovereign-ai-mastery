"""Source-only contract for Module 03 assessment and separate facilitator key.

Does not authenticate claims, test live infrastructure or certify a deployment.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters/03-enterprise-sovereignty-requirements-strategy.md"
KEY = ROOT / "assessments/solutions/03-enterprise-sovereignty-requirements-strategy-solutions.md"
BUILDER = ROOT / "scripts/build_site.py"


class Module03AssessmentContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.key = KEY.read_text(encoding="utf-8")
        cls.builder = BUILDER.read_text(encoding="utf-8")

    def test_all_seven_toc_headers_are_present_exactly_once(self):
        heads = re.findall(r"^### 3\.([1-7]) ", self.chapter, re.M)
        self.assertEqual(heads, list("1234567"))

    def test_five_learner_questions_and_separate_sixth_case(self):
        assessment = self.chapter.split("## Module 03 knowledge assessment", 1)[1]
        self.assertEqual(len(re.findall(r"^\*\*Q[1-5]\. ", assessment, re.M)), 5)
        self.assertEqual(assessment.count("### Q6."), 1)

    def test_scenario_preserves_immutable_site_and_no_network(self):
        assessment = self.chapter.split("### Q6.", 1)[1]
        for phrase in ("FACTORY-A physical premises",
                       "no inbound or outbound network connectivity",
                       "NOT FEASIBLE UNDER CURRENT CONSTRAINTS"):
            self.assertIn(phrase, assessment)

    def test_rca_requires_evidence_and_distinguishes_attempted_from_real(self):
        assessment = self.chapter.split("### Q6.", 1)[1]
        for phrase in ("Technical cause versus process root cause",
                       "Reproducible test and evidence packet",
                       "no verified evidence that real customer data were exported"):
            self.assertIn(phrase.lower(), assessment.lower())

    def test_separate_key_covers_all_questions_and_pm_deliverable(self):
        for number in range(1, 7):
            self.assertIn(f"## Q{number}.", self.key)
        self.assertIn("Total 40 points", self.key)
        self.assertIn("PM deliverable rubric (20 points", self.key)

    def test_facilitator_key_is_not_linked_from_learner_chapter(self):
        self.assertNotIn("../assessments/solutions/", self.chapter)
        self.assertIn("Solutions are deliberately not copied to dist/", self.builder)

    def test_fictional_and_no_certificate_claims(self):
        self.assertIn("fictional", self.chapter.lower())
        self.assertIn("fictional", self.key.lower())
        self.assertIn("not an actual supplier", self.key.lower())
        self.assertIn("REVIEW_REQUIRED", self.key)


if __name__ == "__main__":
    unittest.main()
