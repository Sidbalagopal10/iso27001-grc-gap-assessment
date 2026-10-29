# ISO 27001:2022 Control Assessment

## Control Information

Control ID: A.5.9
Control Name: Inventory of information and other associated assets
Organization: Northstar Digital Solutions
Assessment Type: Simulated Educational Assessment

## Assessment Objective

Evaluate whether the organization maintains
an inventory of information and associated assets,
including documented ownership.

## Evidence Reviewed

Evidence Reference:
asset-inventory/asset-inventory.csv

Evidence Type: SIMULATED

The inventory contains 12 fictional assets
with unique identifiers, business owner roles,
information classifications, and criticality levels.

The CSV structure and required fields were
validated using a Python script.

## Positive Observations

- Asset inventory exists.
- All 12 assets have unique identifiers.
- Business owner roles are documented.
- Classification and criticality fields are populated.

## Identified Gaps

GAP-001:
No evidence that the inventory has been reconciled
against authoritative asset discovery sources.

GAP-002:
No documented inventory review schedule or
evidence of periodic inventory verification.

GAP-003:
No documented asset onboarding and retirement
procedure.

## Assessment Result

Status: PARTIALLY_MET

Rationale:
The simulated inventory demonstrates foundational
asset documentation practices. However, inventory
completeness, lifecycle maintenance, and periodic
review have not been demonstrated.

This status is an educational assessment judgment,
not a verified organizational compliance conclusion.

## Recommended Remediation

1. Establish an asset inventory management procedure.
2. Define review frequency and accountable owners.
3. Reconcile inventory records with authoritative
   asset discovery and cloud inventory sources.
4. Document onboarding, modification, and retirement.
5. Retain dated inventory review evidence.

## Evidence Required for Closure

- Approved asset inventory procedure
- Reconciliation results
- Dated inventory review records
- Asset lifecycle process documentation
