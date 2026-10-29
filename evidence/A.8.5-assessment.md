# ISO 27001:2022 Control Assessment

## Control Information

Control ID: A.8.5
Control Name: Secure authentication
Organization: Northstar Digital Solutions
Evidence Type: SIMULATED

## Assessment Objective

Evaluate whether secure authentication
technologies and procedures are implemented
according to access restrictions and security
requirements.

## Simulated Case Assumptions

- Employee password authentication exists.
- MFA is partially deployed for standard users.
- MFA is not consistently enforced for
  privileged accounts.
- Authentication configurations are incomplete.
- Authentication monitoring is partially
  implemented.

These are fictional case assumptions.

## Identified Gaps

GAP-019:
MFA is not consistently enforced for
privileged accounts.

GAP-020:
MFA coverage for standard users is incomplete.

GAP-021:
Authentication configuration and monitoring
requirements are not fully implemented.

## Assessment Result

Status: PARTIALLY_MET

Rationale:
Basic authentication controls exist in the
fictional organization, but MFA enforcement
and authentication monitoring are incomplete.

## Recommended Remediation

1. Enforce phishing-resistant MFA where feasible,
   prioritizing privileged accounts.
2. Expand MFA coverage to relevant users.
3. Document secure authentication standards.
4. Review authentication configurations.
5. Monitor authentication failures and anomalies.

## Evidence Required for Closure

- MFA enforcement configuration exports
- Privileged account authentication settings
- Authentication policy documentation
- MFA coverage report
- Authentication monitoring records
