# Experimental Lab Charter

## Purpose

Define this repository's role as the AEOS Experimental Governance Lab.

## Scope

This lab supports controlled experiments in:
- governance enforcement
- linting behavior
- traceability continuity
- lifecycle semantics
- review/audit workflow behavior
- operational memory practices

## Non-Goals

- becoming the canonical operational repository
- autonomous runtime execution
- production orchestration
- cross-repository automation

## Governance Boundaries

- Governance-first rules remain mandatory.
- Experiments must be explicit, reviewable, and traceable.
- No experiment may bypass existing safety constraints.

## Human Approval Requirements

- Governance-impacting changes require human approval.
- Porting recommendations require explicit human decision.

## Relationship to aeos-core-opencode

- `aeos-core-opencode` remains canonical.
- This repository evaluates candidates for potential porting.
- No experiment is canonical without formal review and approval.

## Success Criteria

- Experiments are deterministic and reproducible.
- Validation evidence is explicit and auditable.
- Porting decisions are documented with rationale.

## Failure Criteria

- unreadable or corrupted artifacts
- invalid validation outputs
- hidden memory or autonomous behavior
- governance boundary violations

## Auditability Expectations

- Every experiment has explicit IDs and artifacts.
- Validation evidence is recorded and reviewable.
- Decisions are preserved in git history.

## Experiment Lifecycle Expectations

1. Define experiment objective.
2. Implement bounded changes.
3. Validate deterministically.
4. Record results and risks.
5. Review porting eligibility.
6. Require human approval before any canonical porting.
