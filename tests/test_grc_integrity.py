import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_csv(relative_path):
    with (ROOT / relative_path).open(newline="") as f:
        return list(csv.DictReader(f))


class TestGRCIntegrity(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.controls = load_csv(
            "control-assessment/control-matrix.csv"
        )
        cls.risks = load_csv(
            "risk-register/risk-register.csv"
        )
        cls.actions = load_csv(
            "remediation/remediation-plan.csv"
        )
        cls.justifications = load_csv(
            "risk-register/risk-justifications.csv"
        )
        cls.trace = load_csv(
            "reports/control-risk-traceability.csv"
        )

    def test_01_expected_record_counts(self):
        self.assertEqual(len(self.controls), 10)
        self.assertEqual(len(self.risks), 21)
        self.assertEqual(len(self.actions), 21)
        self.assertEqual(len(self.justifications), 21)
        self.assertEqual(len(self.trace), 21)

    def test_02_unique_identifiers(self):
        for rows, key in [
            (self.controls, "Control_ID"),
            (self.risks, "Risk_ID"),
            (self.actions, "Action_ID"),
            (self.justifications, "Risk_ID"),
            (self.trace, "Action_ID"),
        ]:
            ids = [row[key] for row in rows]
            self.assertEqual(len(ids), len(set(ids)))

    def test_03_risk_scores(self):
        for risk in self.risks:
            likelihood = int(risk["Likelihood"])
            impact = int(risk["Impact"])
            score = likelihood * impact

            self.assertTrue(1 <= likelihood <= 5)
            self.assertTrue(1 <= impact <= 5)
            self.assertEqual(int(risk["Risk_Score"]), score)

            expected = (
                "Critical" if score >= 20 else
                "High" if score >= 12 else
                "Medium" if score >= 6 else
                "Low"
            )

            self.assertEqual(risk["Risk_Level"], expected)

    def test_04_control_risk_coverage(self):
        control_ids = {
            c["Control_ID"] for c in self.controls
        }
        mapped_ids = {
            r["Control_ID"] for r in self.risks
        }

        self.assertEqual(control_ids, mapped_ids)

    def test_05_remediation_relationships(self):
        risk_lookup = {
            r["Risk_ID"]: r for r in self.risks
        }

        self.assertEqual(
            {a["Risk_ID"] for a in self.actions},
            set(risk_lookup)
        )

        for action in self.actions:
            risk = risk_lookup[action["Risk_ID"]]

            self.assertEqual(
                action["Control_ID"],
                risk["Control_ID"]
            )
            self.assertEqual(
                action["Responsible_Owner"],
                risk["Risk_Owner"]
            )
            self.assertEqual(
                action["Priority"],
                risk["Risk_Level"]
            )
            self.assertEqual(action["Status"], "PLANNED")
            self.assertGreater(int(action["Target_Days"]), 0)
            self.assertTrue(
                action["Completion_Criteria"].strip()
            )

    def test_06_evidence_references(self):
        for control in self.controls:
            evidence = ROOT / control["Evidence_Reference"]
            self.assertTrue(
                evidence.is_file(),
                f"Missing evidence document: {evidence}"
            )

    def test_07_simulated_classification(self):
        for risk in self.risks:
            self.assertEqual(
                risk["Evidence_Type"], "SIMULATED"
            )

        for item in self.justifications:
            self.assertEqual(
                item["Assessment_Basis"],
                "SIMULATED_QUALITATIVE_JUDGMENT"
            )

    def test_08_justification_coverage(self):
        risk_lookup = {
            r["Risk_ID"]: r for r in self.risks
        }

        self.assertEqual(
            {j["Risk_ID"] for j in self.justifications},
            set(risk_lookup)
        )

        for item in self.justifications:
            risk = risk_lookup[item["Risk_ID"]]

            for field in [
                "Control_ID", "Likelihood", "Impact",
                "Risk_Score", "Risk_Level"
            ]:
                self.assertEqual(item[field], risk[field])

            self.assertTrue(
                item["Likelihood_Justification"].strip()
            )
            self.assertTrue(
                item["Impact_Justification"].strip()
            )

    def test_09_traceability_relationships(self):
        controls = {
            c["Control_ID"]: c for c in self.controls
        }
        risks = {
            r["Risk_ID"]: r for r in self.risks
        }
        actions = {
            a["Action_ID"]: a for a in self.actions
        }
        justifications = {
            j["Risk_ID"]: j for j in self.justifications
        }

        self.assertEqual(
            {t["Action_ID"] for t in self.trace},
            set(actions)
        )

        for row in self.trace:
            control = controls[row["Control_ID"]]
            risk = risks[row["Risk_ID"]]
            action = actions[row["Action_ID"]]
            justification = justifications[row["Risk_ID"]]

            self.assertEqual(
                risk["Control_ID"], control["Control_ID"]
            )
            self.assertEqual(
                action["Risk_ID"], risk["Risk_ID"]
            )
            self.assertEqual(
                action["Control_ID"], control["Control_ID"]
            )

            comparisons = [
                (row["Control_Name"], control["Control_Name"]),
                (row["Gap_Description"], control["Gap_Description"]),
                (row["Risk_Description"], risk["Risk_Description"]),
                (row["Risk_Score"], risk["Risk_Score"]),
                (row["Risk_Level"], risk["Risk_Level"]),
                (row["Remediation_Action"], action["Remediation_Action"]),
                (row["Responsible_Owner"], action["Responsible_Owner"]),
                (row["Remediation_Status"], action["Status"]),
                (
                    row["Likelihood_Justification"],
                    justification["Likelihood_Justification"]
                ),
                (
                    row["Impact_Justification"],
                    justification["Impact_Justification"]
                ),
            ]

            for actual, expected in comparisons:
                self.assertEqual(actual, expected)

    def test_10_no_missing_required_fields(self):
        datasets = [
            self.controls,
            self.risks,
            self.actions,
            self.justifications,
            self.trace,
        ]

        for dataset in datasets:
            for row in dataset:
                for field, value in row.items():
                    self.assertIsNotNone(value, field)
                    self.assertTrue(str(value).strip(), field)

    def test_11_methodology_document(self):
        path = ROOT / "docs/risk-assessment-methodology.md"
        self.assertTrue(path.is_file())

        content = path.read_text()

        for section in [
            "## Likelihood Scale",
            "## Impact Scale",
            "## Risk Scoring",
            "## Risk Severity Thresholds",
            "## Limitations",
        ]:
            self.assertIn(section, content)

    def test_12_critical_risk_count(self):
        critical = sum(
            r["Risk_Level"] == "Critical"
            for r in self.risks
        )
        self.assertEqual(critical, 8)


if __name__ == "__main__":
    unittest.main()
