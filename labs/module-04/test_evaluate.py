"""Deterministic fail-closed tests for Module 04 fictional source/workload lab."""
import copy
import json
import unittest
from pathlib import Path
from evaluate import evaluate_case, evaluate_portfolio

BASE = json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))
CASES = {row["id"]: row for row in BASE["workloads"]}
IDS = {row["id"] for row in BASE["source_claims"]}


class EvidenceMapTests(unittest.TestCase):
    def case(self, ident):
        return copy.deepcopy(CASES[ident])

    def test_baseline_four_dispositions(self):
        report = evaluate_portfolio(BASE)
        self.assertEqual({x["id"]: x["disposition"] for x in report["results"]},
                         {"GCC-DESK-04": "UNVERIFIED",
                          "GCC-PLANT-04": "BLOCKED",
                          "GCC-OT-04": "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS",
                          "GCC-QA-04": "UNVERIFIED"})
        self.assertEqual(report["source_count"], 5)

    def test_wrong_named_factory_even_domestic_is_blocked(self):
        row = self.case("GCC-PLANT-04")
        row["candidate"]["compute_site"] = "DOMESTIC-DC"
        row["candidate"]["restricted_offsite_derivative"] = False
        row["claims"][0]["evidence"] = "configured"
        r = evaluate_case(row, IDS)
        self.assertIn("compute_outside_named_premises", r["hard_failures"])

    def test_synthetic_asr_export_blocks_local_gpu(self):
        row = self.case("GCC-PLANT-04")
        self.assertIn("restricted_derivative_attempt_outside_premises",
                      evaluate_case(row, IDS)["hard_failures"])

    def test_air_gap_disallows_connected_private_links(self):
        row = self.case("GCC-OT-04")
        row["candidate"]["offline_licence_available"] = True
        row["candidate"]["network_mode"] = "private_links"
        r = evaluate_case(row, IDS)
        self.assertEqual(r["disposition"], "BLOCKED")
        self.assertIn("air_gap_has_network_connectivity", r["hard_failures"])

    def test_air_gap_disallows_hidden_management_even_if_disconnected(self):
        row = self.case("GCC-OT-04")
        row["candidate"]["offline_licence_available"] = True
        row["candidate"]["external_management_path"] = True
        self.assertIn("air_gap_has_external_management_path",
                      evaluate_case(row, IDS)["hard_failures"])

    def test_offline_licence_unavailable_is_not_feasible(self):
        row = self.case("GCC-OT-04")
        r = evaluate_case(row, IDS)
        self.assertEqual(r["disposition"], "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS")
        self.assertIn("offline_model_licence_unavailable", r["infeasibility"])

    def test_offline_licence_edit_is_not_acceptance_evidence(self):
        row = self.case("GCC-OT-04")
        row["candidate"]["offline_licence_available"] = True
        self.assertEqual(evaluate_case(row, IDS)["disposition"], "UNVERIFIED")

    def test_adverse_routing_edit_still_unverified(self):
        row = self.case("GCC-PLANT-04")
        row["candidate"]["restricted_offsite_derivative"] = False
        row["claims"][0]["evidence"] = "configured"
        self.assertEqual(evaluate_case(row, IDS)["disposition"], "UNVERIFIED")

    def test_all_fictional_reviews_never_certify(self):
        row = self.case("GCC-DESK-04")
        for index, claim in enumerate(row["claims"]):
            claim["evidence"] = "reviewed"
            claim["test_id"] = "SYNTH-REVIEW-" + str(index)
        r = evaluate_case(row, IDS)
        self.assertEqual(r["disposition"], "REVIEW_REQUIRED")
        self.assertEqual(r["scenario_reported_coverage"], "2/2")

    def test_public_strategy_never_automatically_approves(self):
        row = self.case("GCC-DESK-04")
        self.assertEqual(evaluate_case(row, IDS)["disposition"], "UNVERIFIED")

    def test_unknown_source_ref_is_invalid(self):
        row = self.case("GCC-QA-04")
        row["claims"][0]["source_id"] = "FAKE-GOVERNMENT-LAW"
        self.assertEqual(evaluate_case(row, IDS)["disposition"], "INVALID")

    def test_missing_claim_owner_invalid(self):
        row = self.case("GCC-QA-04")
        row["claims"][0]["owner"] = ""
        self.assertEqual(evaluate_case(row, IDS)["disposition"], "INVALID")

    def test_false_string_is_invalid_not_false(self):
        row = self.case("GCC-QA-04")
        row["candidate"]["restricted_offsite_derivative"] = "false"
        self.assertEqual(evaluate_case(row, IDS)["disposition"], "INVALID")

    def test_duplicate_source_rejected(self):
        data = copy.deepcopy(BASE)
        data["source_claims"].append(copy.deepcopy(data["source_claims"][0]))
        with self.assertRaises(ValueError):
            evaluate_portfolio(data)

    def test_duplicate_workload_rejected(self):
        data = copy.deepcopy(BASE)
        data["workloads"].append(copy.deepcopy(data["workloads"][0]))
        with self.assertRaises(ValueError):
            evaluate_portfolio(data)

    def test_source_requires_https(self):
        data = copy.deepcopy(BASE)
        data["source_claims"][0]["source_url"] = "http://unsupported"
        with self.assertRaises(ValueError):
            evaluate_portfolio(data)

    def test_capacity_failure_is_not_feasible(self):
        row = self.case("GCC-QA-04")
        row["candidate"]["capacity_feasible"] = False
        self.assertEqual(evaluate_case(row, IDS)["disposition"],
                         "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS")


if __name__ == "__main__":
    unittest.main()
