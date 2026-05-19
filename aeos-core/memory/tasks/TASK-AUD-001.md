# TASK-AUD-001

## Linked Objective

- OBJ-AUD-001

## Allowed Changes

- create audit artifacts under `aeos-core/memory/`
- create concise supporting audit documentation
- add minimal deterministic lint/test checks if safe

## Forbidden Changes

- modify `aeos-core-opencode`
- approve or perform porting
- add cross-repo automation
- add orchestration or autonomous runtime behavior

## Audit Steps

1. Review experimental-role, porting, and operating-note artifacts.
2. Evaluate canonical protection and porting-control enforceability.
3. Evaluate readability and format integrity of experimental artifacts.
4. Evaluate lint/test trustworthiness.
5. Record findings, conditions, and recommendations.

## Validation Requirements

- `python3 aeos-core/scripts/aeos_lint.py`
- `cd aeos-core && pytest`

## Acceptance Criteria

- `AUD-EXP-002` exists with findings and conditions
- `PORT-001` remains `DEFER`
- audit and handoff artifacts are traceable and readable
- no scope expansion beyond audit cycle artifacts and minimal validation checks

## Reviewer Requirement

Manual reviewer confirmation required before reconsidering any future porting candidate.

## Human Approval Requirement

Human approval remains mandatory for canonical porting decisions.

## Status

CLOSED
