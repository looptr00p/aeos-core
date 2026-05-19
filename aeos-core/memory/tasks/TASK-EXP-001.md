# TASK-EXP-001

## Linked Objective

- OBJ-EXP-001

## Linked Experiment

- EXP-001

## Linked Porting Review

- PORT-001

## Task Context

Evaluate whether the experimental lab framing and porting governance are coherent, auditable, and safe for continued experimental use.

## Allowed Changes

- create experiment evaluation artifacts under `aeos-core/memory/`
- add concise operational notes under `aeos-core/docs/`
- add minimal validation support under `aeos-core/scripts/` and `aeos-core/tests/`

## Forbidden Changes

- modify `aeos-core-opencode`
- approve or execute any porting
- introduce cross-repo automation
- introduce orchestration, autonomous runtime, or hidden memory

## Implementation Steps

1. Create objective/task/review/audit/handoff artifacts for cycle 001.
2. Add portability risk assessment for controlled porting readiness.
3. Update `PORT-001` while preserving `DEFER`.
4. Add minimal lint/test coverage for new artifacts.
5. Validate using lint and pytest.

## Required Validation

- `python3 aeos-core/scripts/aeos_lint.py`
- `cd aeos-core && pytest`

## Acceptance Criteria

- required `EXP-001` cycle artifacts exist and are readable
- `PORT-001` explicitly remains deferred
- no canonical repo changes occur
- no scope expansion beyond evaluation artifacts and minimal validation support

## Reviewer Requirement

Reviewer role required prior to any future porting recommendation.

## Human Approval Requirement

Human approval required for any future canonical porting decision.

## Status

IN_PROGRESS
