# ISO 27001:2022 Control Assessment

## Control Information

Control ID: A.8.15
Control Name: Logging
Organization: Northstar Digital Solutions
Evidence Type: SIMULATED

## Assessment Objective

Evaluate whether relevant security logs are
produced, stored, protected, and analyzed
to support security monitoring and investigations.

## Simulated Case Assumptions

- Windows security event logging is enabled.
- Cloud activity logging is partially implemented.
- Centralized SIEM collection is incomplete.
- Log retention requirements are not fully defined.
- Log integrity protection is inconsistent.
- Security log reviews are informal.

These are fictional case assumptions.

## Identified Gaps

GAP-028:
Incomplete centralized collection of
security-relevant logs.

GAP-029:
Insufficient log retention and integrity
protection requirements.

GAP-030:
No formalized security log review process.

## Assessment Result

Status: PARTIALLY_MET

Rationale:
Basic logging capabilities exist in the
fictional organization, but centralized
collection, protection, retention, and
review processes are incomplete.

## Recommended Remediation

1. Define security logging requirements.
2. Centralize relevant endpoint and cloud logs.
3. Establish log retention periods.
4. Protect logs from unauthorized modification.
5. Define log monitoring and review procedures.
6. Document alert escalation responsibilities.
7. Periodically validate logging coverage.

## Evidence Required for Closure

- Approved security logging standard
- SIEM log source inventory
- Endpoint logging configuration records
- Cloud logging configuration records
- Log retention configuration
- Log access and integrity controls
- Security monitoring and review records
