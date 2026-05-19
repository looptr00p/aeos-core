# Format Remediation Audit

## Affected Files

- README.md
- aeos-core/scripts/aeos_lint.py
- aeos-core/tests/enforcement/test_experimental_lab_role.py
- aeos-core/docs/EXPERIMENTAL_LAB_CHARTER.md
- aeos-core/governance/PORTING_POLICY.md
- aeos-core/templates/experiment_template.md
- aeos-core/templates/porting_review_template.md
- aeos-core/memory/experiments/EXP-001.md
- aeos-core/memory/experiments/PORT-001.md

## Corruption Type

- Readability degradation from duplicated markdown section in `README.md`.
- Experimental lab role artifacts missing from tracked remediated set before this pass.
- No collapsed single-line Python artifacts detected in `aeos-core/scripts/` and `aeos-core/tests/` during this remediation pass.

## Operational Impact

- Duplicated markdown reduced operational clarity during review.
- Missing/partial experimental governance artifacts reduced deterministic review readiness.

## Governance Impact

- Potential ambiguity about repository role and controlled porting discipline.
- Reduced audit clarity for experimental governance decisions.

## Remediation Scope

- Localized markdown readability restoration in `README.md`.
- Additive creation/verification of experimental governance artifacts under `aeos-core/`.
- Lightweight lint/test verification for deterministic reviewability.

## Remediation Boundaries

- No architecture redesign.
- No governance semantic redesign.
- No workflow engine/runtime behavior changes.
- No dependency changes.
- No cross-repository automation.

## Rollback Considerations

- Revert the remediation commit to restore prior state.
- If partial rollback is needed, revert only `README.md` and/or specific experimental artifacts.
- Re-run lint and tests after rollback to confirm deterministic integrity.
