"""Fail-closed tests for the fictional Module 03 release decision simulator."""
import copy
import json
import unittest
from pathlib import Path

from evaluate import evaluate_case, evaluate_portfolio

CASES = {x["id"]: x for x in json.loads(Path(__file__).with_name("cases.json").read_text(encoding="utf-8"))["workloads"]}


class RequirementGateTests(unittest.TestCase):
    def row(self, ident):
        return copy.deepcopy(CASES[ident])

    def test_baseline_dispositions(self):
        result = evaluate_portfolio({"workloads": list(CASES.values())})
        self.assertEqual({x["id"]: x["disposition"] for x in result["results"]}, {
            "POLICY-03": "UNVERIFIED", "DESIGN-03": "BLOCKED",
            "OT-03": "BLOCKED", "LICENCE-03": "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS"})

    def test_domestic_but_not_named_factory_is_blocked(self):
        row = self.row("LICENCE-03")
        row["candidate"]["offline_licence_available"] = True
        row["candidate"]["compute_site"] = "UAE-DC-2"
        result = evaluate_case(row)
        self.assertEqual(result["disposition"], "BLOCKED")
        self.assertIn("compute_outside_named_premises", result["hard_failures"])

    def test_air_gap_has_no_hidden_management_exception(self):
        row = self.row("OT-03")
        row["candidate"]["network_mode"] = "disconnected"
        result = evaluate_case(row)
        self.assertEqual(result["disposition"], "BLOCKED")
        self.assertIn("external_management_path_in_air_gap", result["hard_failures"])

    def test_air_gap_without_path_still_not_verified(self):
        row = self.row("OT-03")
        row["candidate"].update(network_mode="disconnected", external_management_path=False)
        self.assertEqual(evaluate_case(row)["disposition"], "UNVERIFIED")

    def test_local_route_change_does_not_create_verification(self):
        row = self.row("DESIGN-03")
        row["candidate"]["offsite_derivative_attempt"] = False
        row["claims"][0]["evidence"] = "configured"
        self.assertEqual(evaluate_case(row)["disposition"], "UNVERIFIED")

    def test_offline_licence_unavailable_is_infeasible(self):
        self.assertEqual(evaluate_case(self.row("LICENCE-03"))["disposition"],
                         "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS")

    def test_capacity_shortfall_is_infeasible(self):
        row = self.row("POLICY-03")
        row["candidate"]["capacity_feasible"] = False
        self.assertEqual(evaluate_case(row)["disposition"], "NOT_FEASIBLE_UNDER_CURRENT_CONSTRAINTS")

    def test_adverse_evidence_blocks_a_workload(self):
        row = self.row("POLICY-03")
        row["claims"][0]["evidence"] = "adverse"
        self.assertEqual(evaluate_case(row)["disposition"], "BLOCKED")

    def test_all_declared_reviewed_is_not_certification(self):
        row = self.row("POLICY-03")
        for i, claim in enumerate(row["claims"]):
            claim["evidence"] = "reviewed"
            claim["test_id"] = f"SYNTH-TEST-{i}"
        result = evaluate_case(row)
        self.assertEqual(result["disposition"], "REVIEW_REQUIRED")
        self.assertEqual(result["scenario_reported_coverage"], "3/3")

    def test_missing_issuer_is_invalid(self):
        row = self.row("POLICY-03")
        row.pop("authority")
        self.assertEqual(evaluate_case(row)["disposition"], "INVALID")

    def test_missing_test_control_chain_is_invalid(self):
        row = self.row("POLICY-03")
        row["claims"][0].pop("test")
        self.assertEqual(evaluate_case(row)["disposition"], "INVALID")

    def test_string_boolean_does_not_bypass_gate(self):
        row = self.row("DESIGN-03")
        row["candidate"]["offsite_derivative_attempt"] = "false"
        self.assertEqual(evaluate_case(row)["disposition"], "INVALID")

    def test_duplicate_claim_ids_are_invalid(self):
        row = self.row("DESIGN-03")
        row["claims"][1]["id"] = row["claims"][0]["id"]
        self.assertEqual(evaluate_case(row)["disposition"], "INVALID")

    def test_duplicate_workloads_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_portfolio({"workloads": [self.row("OT-03"), self.row("OT-03")]})


if __name__ == "__main__":
    unittest.main()
