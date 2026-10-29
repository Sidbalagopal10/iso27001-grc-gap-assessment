import csv
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(relative_path):
    with (ROOT / relative_path).open(newline="") as f:
        return list(csv.DictReader(f))


controls = load("control-assessment/control-matrix.csv")
risks = load("risk-register/risk-register.csv")
actions = load("remediation/remediation-plan.csv")

risk_counts = Counter(r["Risk_Level"] for r in risks)
control_counts = Counter(
    c["Assessment_Status"] for c in controls
)

risk_lookup = {r["Risk_ID"]: r for r in risks}
action_lookup = {a["Risk_ID"]: a for a in actions}

assert len(controls) == 10
assert len(risks) == 21
assert len(actions) == 21
assert len(risk_lookup) == len(risks)
assert len(action_lookup) == len(actions)

critical_risks = sorted(
    [r for r in risks if r["Risk_Level"] == "Critical"],
    key=lambda r: (-int(r["Risk_Score"]), r["Risk_ID"])
)

lines = [
    "# Executive Cybersecurity Risk Assessment Report",
    "",
    "**Organization:** Northstar Digital Solutions",
    "**Framework:** ISO/IEC 27001:2022 — Selected Annex A Controls",
    "**Assessment Type:** Simulated Educational Gap Assessment",
    f"**Report Generated:** {date.today().isoformat()}",
    "",
    "## 1. Executive Summary",
    "",
    (
        f"The simulated assessment evaluated {len(controls)} selected "
        "ISO 27001:2022 Annex A controls across a fictional hybrid "
        "IT environment."
    ),
    "",
    (
        f"The assessment documented {len(risks)} risk scenarios, "
        f"including {risk_counts['Critical']} Critical and "
        f"{risk_counts['High']} High risks."
    ),
    "",
    (
        f"A total of {len(actions)} remediation actions were "
        "planned to address the identified scenarios."
    ),
    "",
    "These results are hypothetical and do not establish "
    "the actual security posture of any organization.",
    "",
    "## 2. Control Assessment Summary",
    "",
    "| Assessment Status | Controls |",
    "|---|---:|",
]

for status in [
    "MET",
    "PARTIALLY_MET",
    "NOT_MET",
    "NOT_ASSESSED",
]:
    lines.append(
        f"| {status} | {control_counts[status]} |"
    )

lines += [
    "",
    "## 3. Risk Severity Distribution",
    "",
    "| Severity | Risk Count |",
    "|---|---:|",
]

for severity in ["Critical", "High", "Medium", "Low"]:
    lines.append(
        f"| {severity} | {risk_counts[severity]} |"
    )

lines += [
    "",
    "## 4. Critical Risk Register",
    "",
    "| Risk ID | Control | Risk Scenario | Score | Owner |",
    "|---|---|---|---:|---|",
]

for risk in critical_risks:
    description = risk["Risk_Description"].replace("|", "/")

    lines.append(
        f"| {risk['Risk_ID']} | {risk['Control_ID']} | "
        f"{description} | {risk['Risk_Score']} | "
        f"{risk['Risk_Owner']} |"
    )

lines += [
    "",
    "## 5. Remediation Priorities",
    "",
    "The following priorities are illustrative and subject "
    "to management approval:",
    "",
]

for risk in critical_risks:
    action = action_lookup[risk["Risk_ID"]]

    lines.append(
        f"- **{risk['Risk_ID']} — {risk['Control_ID']}:** "
        f"{action['Remediation_Action']} "
        f"(Owner: {action['Responsible_Owner']}; "
        f"Target: {action['Target_Days']} days)."
    )

lines += [
    "",
    "## 6. Proposed 30/60/90-Day Roadmap",
    "",
    "### Days 1–30",
    "",
    "- Review and approve the simulated risk register.",
    "- Prioritize Critical risks and assign accountable owners.",
    "- Establish security policy ownership and approval.",
    "- Address privileged access and authentication weaknesses.",
    "- Validate logging and backup protection requirements.",
    "",
    "### Days 31–60",
    "",
    "- Implement recurring identity and access reviews.",
    "- Formalize secure configuration baselines.",
    "- Conduct incident response tabletop exercises.",
    "- Establish documented backup restoration tests.",
    "- Review progress against remediation completion criteria.",
    "",
    "### Days 61–90",
    "",
    "- Validate completed remediation activities.",
    "- Collect implementation and effectiveness evidence.",
    "- Reassess residual risk where controls have changed.",
    "- Escalate unresolved risks for management decisions.",
    "- Prepare an updated risk treatment and governance report.",
    "",
    "## 7. Management Recommendations",
    "",
    "1. Review and approve a formal risk treatment approach.",
    "2. Prioritize risks with potentially severe business impact.",
    "3. Establish clear ownership and evidence requirements.",
    "4. Track remediation progress and overdue actions.",
    "5. Reassess risks after controls are implemented.",
    "",
    "## 8. Assessment Limitations",
    "",
    "- The organization and findings are fictional.",
    "- All evidence and risk ratings are simulated.",
    "- No production controls were independently verified.",
    "- Only 10 selected Annex A controls were assessed.",
    "- ISO 27001 clauses 4–10 were not comprehensively assessed.",
    "- No certification or compliance conclusion is provided.",
    "- All remediation actions remain planned, not completed.",
    "",
    "## 9. Supporting Artifacts",
    "",
    "- `control-assessment/control-matrix.csv`",
    "- `risk-register/risk-register.csv`",
    "- `risk-register/risk-justifications.csv`",
    "- `remediation/remediation-plan.csv`",
    "- `reports/control-risk-traceability.csv`",
    "- `docs/risk-assessment-methodology.md`",
    "",
]

output = ROOT / "reports/executive-risk-report.md"
output.write_text("\n".join(lines), encoding="utf-8")

print("Executive GRC report generated.")
print("Selected controls:", len(controls))
print("Documented risks:", len(risks))
print("Critical risks:", risk_counts["Critical"])
print("Remediation actions:", len(actions))
print("Output:", output.relative_to(ROOT))
