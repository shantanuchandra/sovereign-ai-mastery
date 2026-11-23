"""Fail-closed checks for synthetic Module 05 legal-control map."""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from validate import ValidationError, validate_document

ROOT = Path(__file__).resolve().parent


def fixture():
    return json.loads((ROOT / "control_map.json").read_text(encoding="utf-8"))


def record(document, record_id):
    return next(row for row in document["activities"]
                if row["activity_id"] == record_id)


class LegalControlGraphContract(unittest.TestCase):
    def assert_rejected(self, doc, phrase):
        with self.assertRaises(ValidationError) as failure:
            validate_document(doc)
        self.assertIn(phrase, str(failure.exception))

    def test_valid_synthetic_baseline_is_never_certified(self):
        result = validate_document(fixture())
        self.assertEqual(result["status"], "SYNTHETIC_SCHEMA_VALIDATED_ONLY")
        self.assertEqual(result["activities_checked"], 6)
        self.assertEqual(result["legal_review_needed"], 4)
        self.assertEqual(result["decision_counts"]["HOLD"], 5)
        self.assertEqual(result["decision_counts"]["PILOT_SYNTHETIC_ONLY"], 1)
        self.assertNotIn("COMPLIANT", str(result))

    def test_reject_missing_primary_source_pinpoint(self):
        doc = fixture()
        record(doc, "GC-02")["legal_candidate"]["source_section"] = ""
        self.assert_rejected(doc, "legal_candidate.source_section is missing")

    def test_reject_unverified_law_promoted_to_approval(self):
        doc = fixture()
        record(doc, "GC-02")["decision"] = "APPROVED"
        self.assert_rejected(doc, "approval forbidden before counsel review")

    def test_reject_fake_counsel_approval_id(self):
        doc = fixture()
        record(doc, "GC-02")["legal_candidate"]["review_status"] = "APPROVED"
        self.assert_rejected(doc, "APPROVED legal review lacks counsel_approval_id")

    def test_reject_pending_counsel_with_conflicting_approval(self):
        doc = fixture()
        record(doc, "GC-03")["legal_candidate"]["counsel_approval_id"] = "MADE-UP"
        self.assert_rejected(doc, "pending counsel entry must not carry approval")

    def test_reject_real_or_restricted_data_in_synthetic_pilot(self):
        doc = fixture()
        record(doc, "GC-01")["data_class"] = "restricted_synthetic"
        self.assert_rejected(doc, "synthetic pilot cannot include restricted")

    def test_reject_outside_processing_from_named_factory(self):
        doc = fixture()
        record(doc, "PLANT-05")["processing_destinations"].append("UAE-CLOUD")
        self.assert_rejected(doc, "processing_destinations violates named physical")

    def test_reject_unverified_remote_support_from_named_factory(self):
        for route in ("REMOTE-SUPPORT", "VENDOR-TELEMETRY", "PRIVATE-LINK",
                      "FACTORY-A-LAN-UNVERIFIED"):
            doc = fixture()
            record(doc, "PLANT-05")["network_paths"] = [route]
            with self.subTest(route=route):
                self.assert_rejected(doc, "named premises network paths need verified on-site routing")

    def test_reject_offsite_backup_from_named_factory(self):
        doc = fixture()
        record(doc, "PLANT-05")["backup_destinations"] = ["NEARBY-UAE-REGION"]
        self.assert_rejected(doc, "backup_destinations violates named physical")

    def test_reject_any_network_path_from_physical_airgap(self):
        for network in ("REMOTE-SUPPORT", "PRIVATE-LINK", "TELEMETRY",
                        "DISASTER-RECOVERY", "LICENCE-CHECK"):
            doc = fixture()
            record(doc, "OT-05")["network_paths"] = [network]
            with self.subTest(network=network):
                self.assert_rejected(doc, "physical air gap prohibits ALL network")

    def test_blocked_egress_attempt_is_not_airgap_success(self):
        """A firewall deny log proves an attempted path, not physical isolation."""
        for attempted_route in ("BLOCKED-REMOTE-SUPPORT-ATTEMPT",
                                "BLOCKED-DNS-QUERY-ATTEMPT",
                                "BLOCKED-LICENCE-CHECK-ATTEMPT"):
            doc = fixture()
            row = record(doc, "OT-05")
            row["network_paths"] = [attempted_route]
            row["hard_gate_state"] = "FAILED"
            row["decision"] = "BLOCKED"
            with self.subTest(route=attempted_route):
                self.assert_rejected(doc, "physical air gap prohibits ALL network")

    def test_blocked_egress_attempt_is_not_named_premises_proof(self):
        """Even denied offsite support is an unverified named-site route."""
        doc = fixture()
        row = record(doc, "PLANT-05")
        row["network_paths"] = ["BLOCKED-OFFSITE-SUPPORT-ATTEMPT"]
        row["hard_gate_state"] = "FAILED"
        row["decision"] = "BLOCKED"
        self.assert_rejected(doc, "named premises network paths need verified on-site routing")

    def test_reject_online_activation_dependency(self):
        doc = fixture()
        record(doc, "OT-05")["licence_mode"] = "ONLINE_REQUIRED"
        self.assert_rejected(doc, "physical hard gate forbids required online licence")

    def test_reject_disguised_online_activation_mode(self):
        doc = fixture()
        record(doc, "OT-05")["licence_mode"] = "ONLINE_REQUIRED_WITH_FALLBACK"
        self.assert_rejected(doc, "unrecognized licence_mode")

    def test_reject_unknown_offline_entitlement_even_with_claimed_gate(self):
        doc = fixture()
        row = record(doc, "PLANT-05")
        row["licence_mode"] = "UNKNOWN"
        row["hard_gate_state"] = "VERIFIED"
        row["decision"] = "PILOT_SYNTHETIC_ONLY"
        row["data_class"] = "synthetic_only"
        self.assert_rejected(doc, "physical release requires separately evidenced offline licence")

    def test_reject_unverified_offline_entitlement_even_with_claimed_gate(self):
        doc = fixture()
        row = record(doc, "OT-05")
        row["licence_mode"] = "OFFLINE_UNVERIFIED"
        row["hard_gate_state"] = "VERIFIED"
        row["decision"] = "PILOT_SYNTHETIC_ONLY"
        row["data_class"] = "synthetic_only"
        self.assert_rejected(doc, "physical release requires separately evidenced offline licence")

    def test_reject_unverified_physical_release_even_if_counsel_approved(self):
        doc = fixture()
        row = record(doc, "PLANT-05")
        row["legal_candidate"]["review_status"] = "APPROVED"
        row["legal_candidate"]["counsel_approval_id"] = "FICTIONAL-COUNSEL-TEST"
        row["decision"] = "APPROVED"
        self.assert_rejected(doc, "no release without separately verified physical evidence")

    def test_failed_hard_gate_has_blocked_disposition(self):
        doc = fixture()
        record(doc, "PLANT-05")["hard_gate_state"] = "FAILED"
        self.assert_rejected(doc, "FAILED hard gate requires BLOCKED")

    def test_reject_duplicate_identifiers(self):
        doc = fixture()
        doc["activities"].append(copy.deepcopy(doc["activities"][0]))
        self.assert_rejected(doc, "duplicate activity_id")

    def test_reject_missing_control_owner(self):
        doc = fixture()
        record(doc, "GC-04")["control_owner"] = ""
        self.assert_rejected(doc, "control_owner must be nonempty")

    def test_reject_missing_test_id(self):
        doc = fixture()
        record(doc, "GC-04").pop("test_id")
        self.assert_rejected(doc, "missing fields: test_id")

    def test_reject_missing_destination_list(self):
        doc = fixture()
        record(doc, "OT-05")["backup_destinations"] = []
        self.assert_rejected(doc, "backup_destinations needs a named physical destination")

    def test_nonphysical_case_cannot_claim_physical_gate_verification(self):
        doc = fixture()
        record(doc, "GC-01")["hard_gate_state"] = "VERIFIED"
        self.assert_rejected(doc, "nonphysical workflow must use NOT_APPLICABLE gate")


if __name__ == "__main__":
    unittest.main()
