"""Source-footnote inventory contract for Module 04.
This is NOT an online publisher audit or independent source certification.
"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "chapters/04-uae-gcc-global-sovereign-ai-ecosystems.md"
LEDGER = ROOT / "reviews/module-04/source-accuracy-ledger-2026-11-22.md"

class Module04SourceLedgerContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chapter = CHAPTER.read_text(encoding="utf-8")
        cls.ledger = LEDGER.read_text(encoding="utf-8")

    def test_all_primary_source_footnotes_inventoried_once(self):
        chapter_ids = re.findall(r"^\[\^([^\]]+)\]:", self.chapter, re.M)
        ledger_ids = re.findall(r"^\| `([^`]+)` \| \*\*(VERIFIED_DIRECT|PENDING_DIRECT|RETRIEVAL_BLOCKED)\*\*", self.ledger, re.M)
        self.assertEqual(len(chapter_ids), 30)
        self.assertEqual(len(chapter_ids), len(set(chapter_ids)))
        self.assertEqual(set(chapter_ids), {row[0] for row in ledger_ids})
        self.assertEqual(len(ledger_ids), len(set(row[0] for row in ledger_ids)))

    def test_every_cited_footnote_has_exactly_one_definition(self):
        cited = set(re.findall(r"\[\^([^\]]+)\]", self.chapter))
        definitions = re.findall(r"^\[\^([^\]]+)\]:", self.chapter, re.M)
        self.assertEqual(cited, set(definitions),
                         f"Undefined: {sorted(cited - set(definitions))}; unused: {sorted(set(definitions) - cited)}")
        self.assertEqual(len(definitions), len(set(definitions)))

    def test_partial_audit_not_mislabelled_complete(self):
        self.assertIn("T04-03 PARTIALLY VERIFIED, STILL OPEN/BLOCKING", self.ledger)
        self.assertIn("Both Module 04 reviews remain HOLD", self.ledger)
        self.assertIn("not a human/different-model challenge", self.ledger)
        self.assertIn("RETRIEVAL_BLOCKED", self.ledger)
        self.assertIn("PENDING_DIRECT", self.ledger)

    def test_no_source_claim_is_customer_specific_certification(self):
        for claim in ("never a site test", "in-country off-site endpoint does not pass",
                      "all inbound/outbound networks", "offline licence"):
            self.assertIn(claim.lower(), self.ledger.lower())

    def test_known_primary_publisher_rows_have_bounded_status(self):
        for x in ("eu-timeline-45", "china-cac-45", "india-pib-45",
                  "iea-energy-46", "nist-scrm-46", "ibm-allam-47"):
            self.assertRegex(self.ledger, rf"(?m)^\| `{re.escape(x)}` \| \*\*VERIFIED_DIRECT\*\*")
        for x in ("gcc-bahrain-44", "gcc-qatar-44", "tii-emirati-47"):
            self.assertIn(x, self.ledger)

if __name__ == "__main__":
    unittest.main()
