"""Unit tests for fictional, fail-closed Module 02 scenario evaluation."""
import copy
import json
import unittest
from pathlib import Path
from evaluate import evaluate_case, evaluate_portfolio

SAMPLE = json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))
CASES = {item["id"]: item for item in SAMPLE["workloads"]}


class ScoringLabTests(unittest.TestCase):
    def case(self, name):
        return copy.deepcopy(CASES[name])

    def test_baseline_expected_dispositions(self):
        report = evaluate_portfolio(SAMPLE)
        actual = {row["id"]: row["disposition"] for row in report["results"]}
        self.assertEqual(actual, {
            "CORP-02": "UNVERIFIED",
            "PLANT-02": "BLOCKED",
            "OT-02": "BLOCKED",
            "LIC-02": "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS"
        })

    def test_site_rule_denies_approved_country_but_wrong_premises(self):
        item = self.case("LIC-02")
        item["candidate"]["compute_site"] = "DOMESTIC-DC-B"
        item["candidate"]["offline_licence_available"] = True
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "BLOCKED")
        self.assertIn("compute_outside_named_physical_premises", result["hard_gate_failures"])

    def test_air_gap_denies_any_network_path_even_with_disconnected_label(self):
        item = self.case("OT-02")
        item["candidate"]["network"] = "disconnected"
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "BLOCKED")
        self.assertIn("air_gap_has_external_network_path", result["hard_gate_failures"])

    def test_offline_requirement_never_uses_remote_fallback(self):
        result = evaluate_case(self.case("LIC-02"))
        self.assertEqual(result["disposition"], "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS")
        self.assertFalse(result["hard_gate_failures"])

    def test_no_evidence_is_unverified_not_pass(self):
        item = self.case("CORP-02")
        for rec in item["dimensions"].values():
            rec["stage"] = "M3"
            rec["evidence"] = "asserted"
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "UNVERIFIED")
        self.assertEqual(result["scenario_reported_coverage"], "0/4")

    def test_simulated_all_reviewed_still_not_certified(self):
        item = self.case("CORP-02")
        for index, rec in enumerate(item["dimensions"].values()):
            rec.update({"stage": "M4", "evidence": "reviewed", "test_id": f"SYNTH-TEST-{index}"})
        result = evaluate_case(item)
        self.assertEqual(result["scenario_reported_coverage"], "4/4")
        self.assertEqual(result["disposition"], "REVIEW_REQUIRED")
        self.assertNotIn("COMPLIANT", result["disposition"])

    def test_known_adverse_control_blocks_even_with_other_reviewed_results(self):
        item = self.case("CORP-02")
        item["dimensions"]["technological"]["evidence"] = "adverse"
        self.assertEqual(evaluate_case(item)["disposition"], "BLOCKED")

    def test_current_boundary_does_not_weaken_after_egress_flag_edit(self):
        item = self.case("PLANT-02")
        item["candidate"]["restricted_offsite_flow"] = False
        item["dimensions"]["territorial"]["evidence"] = "configured"
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "UNVERIFIED")
        self.assertNotEqual(result["disposition"], "REVIEW_REQUIRED")

    def test_missing_dimension_is_invalid(self):
        item = self.case("CORP-02")
        del item["dimensions"]["legal_contractual"]
        self.assertEqual(evaluate_case(item)["disposition"], "INVALID")

    def test_malformed_boolean_is_invalid(self):
        item = self.case("CORP-02")
        item["candidate"]["restricted_offsite_flow"] = "false"
        self.assertEqual(evaluate_case(item)["disposition"], "INVALID")

    def test_duplicate_ids_rejected(self):
        items = [self.case("CORP-02"), self.case("CORP-02")]
        with self.assertRaises(ValueError):
            evaluate_portfolio({"workloads": items})


    def test_expired_evidence_is_unverified(self):
        item = self.case("CORP-02")
        item["dimensions"]["territorial"]["evidence"] = "expired"
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "UNVERIFIED")
        self.assertTrue(any("expired" in gap for gap in result["unverified_claims"]))

    def test_local_capacity_shortfall_is_not_feasible(self):
        item = self.case("LIC-02")
        item["candidate"]["offline_licence_available"] = True
        item["candidate"]["capacity_feasible"] = False
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS")
        self.assertIn("local_or_approved_compute_capacity_unavailable", result["feasibility_gaps"])

    def test_named_location_outside_approved_list_is_blocked(self):
        item = self.case("CORP-02")
        item["candidate"]["compute_site"] = "UNAPPROVED-SITE-Z"
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "BLOCKED")
        self.assertIn("compute_site_not_in_approved_locations", result["hard_gate_failures"])

    def test_disconnected_candidate_still_needs_real_evidence(self):
        item = self.case("OT-02")
        item["candidate"]["network"] = "disconnected"
        item["candidate"]["external_network_path"] = False
        result = evaluate_case(item)
        self.assertEqual(result["disposition"], "UNVERIFIED")
        self.assertNotEqual(result["disposition"], "REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
