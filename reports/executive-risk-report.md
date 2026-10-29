# Executive Cybersecurity Risk Assessment Report

**Organization:** Northstar Digital Solutions
**Framework:** ISO/IEC 27001:2022 — Selected Annex A Controls
**Assessment Type:** Simulated Educational Gap Assessment
**Report Generated:** 2026-10-29

## 1. Executive Summary

The simulated assessment evaluated 10 selected ISO 27001:2022 Annex A controls across a fictional hybrid IT environment.

The assessment documented 21 risk scenarios, including 8 Critical and 13 High risks.

A total of 21 remediation actions were planned to address the identified scenarios.

These results are hypothetical and do not establish the actual security posture of any organization.

## 2. Control Assessment Summary

| Assessment Status | Controls |
|---|---:|
| MET | 0 |
| PARTIALLY_MET | 9 |
| NOT_MET | 1 |
| NOT_ASSESSED | 0 |

## 3. Risk Severity Distribution

| Severity | Risk Count |
|---|---:|
| Critical | 8 |
| High | 13 |
| Medium | 0 |
| Low | 0 |

## 4. Critical Risk Register

| Risk ID | Control | Risk Scenario | Score | Owner |
|---|---|---|---:|---|
| RISK-006 | A.5.15 | Excessive access permissions may enable unauthorized access to sensitive resources | 20 | IT Manager |
| RISK-008 | A.5.16 | Former employee accounts may remain active and enable unauthorized access | 20 | IT Manager |
| RISK-011 | A.5.17 | Compromised credentials may remain valid and enable continued unauthorized access | 20 | Security Lead |
| RISK-012 | A.5.24 | Unclear incident response responsibilities may delay threat containment | 20 | Security Lead |
| RISK-014 | A.8.5 | Privileged accounts without MFA may be compromised through stolen passwords | 20 | Security Lead |
| RISK-016 | A.8.9 | Insecure system configurations may expose sensitive cloud resources | 20 | IT Manager |
| RISK-018 | A.8.13 | Inadequately protected backups may be compromised or destroyed during a security incident | 20 | IT Manager |
| RISK-020 | A.8.15 | Incomplete centralized logging may delay detection and investigation of security incidents | 20 | Security Lead |

## 5. Remediation Priorities

The following priorities are illustrative and subject to management approval:

- **RISK-006 — A.5.15:** Review privileged permissions and remove unnecessary access (Owner: IT Manager; Target: 15 days).
- **RISK-008 — A.5.16:** Implement HR-triggered employee offboarding and account deactivation (Owner: IT Manager; Target: 15 days).
- **RISK-011 — A.5.17:** Implement compromised credential revocation and replacement workflow (Owner: Security Lead; Target: 15 days).
- **RISK-012 — A.5.24:** Develop approved incident response plan and define escalation responsibilities (Owner: Security Lead; Target: 15 days).
- **RISK-014 — A.8.5:** Enforce phishing-resistant MFA across privileged AWS and Microsoft Entra accounts (Owner: Security Lead; Target: 15 days).
- **RISK-016 — A.8.9:** Develop and enforce secure configuration baselines for cloud and endpoint systems (Owner: IT Manager; Target: 15 days).
- **RISK-018 — A.8.13:** Implement immutable backup storage with restricted access and encryption (Owner: IT Manager; Target: 15 days).
- **RISK-020 — A.8.15:** Centralize endpoint and cloud security logs and establish monitoring procedures (Owner: Security Lead; Target: 15 days).

## 6. Proposed 30/60/90-Day Roadmap

### Days 1–30

- Review and approve the simulated risk register.
- Prioritize Critical risks and assign accountable owners.
- Establish security policy ownership and approval.
- Address privileged access and authentication weaknesses.
- Validate logging and backup protection requirements.

### Days 31–60

- Implement recurring identity and access reviews.
- Formalize secure configuration baselines.
- Conduct incident response tabletop exercises.
- Establish documented backup restoration tests.
- Review progress against remediation completion criteria.

### Days 61–90

- Validate completed remediation activities.
- Collect implementation and effectiveness evidence.
- Reassess residual risk where controls have changed.
- Escalate unresolved risks for management decisions.
- Prepare an updated risk treatment and governance report.

## 7. Management Recommendations

1. Review and approve a formal risk treatment approach.
2. Prioritize risks with potentially severe business impact.
3. Establish clear ownership and evidence requirements.
4. Track remediation progress and overdue actions.
5. Reassess risks after controls are implemented.

## 8. Assessment Limitations

- The organization and findings are fictional.
- All evidence and risk ratings are simulated.
- No production controls were independently verified.
- Only 10 selected Annex A controls were assessed.
- ISO 27001 clauses 4–10 were not comprehensively assessed.
- No certification or compliance conclusion is provided.
- All remediation actions remain planned, not completed.

## 9. Supporting Artifacts

- `control-assessment/control-matrix.csv`
- `risk-register/risk-register.csv`
- `risk-register/risk-justifications.csv`
- `remediation/remediation-plan.csv`
- `reports/control-risk-traceability.csv`
- `docs/risk-assessment-methodology.md`
