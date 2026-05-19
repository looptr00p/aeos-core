# Porting Policy

## Purpose

Define deterministic governance for proposing experiment outputs for migration into `aeos-core-opencode`.

## Porting Rule

No experiment may be ported automatically.
No Codex-generated change is canonical without review.

## Eligibility Criteria

A candidate is eligible only if it is:
- readable
- deterministic
- governance-compliant
- validated with passing checks
- operationally compatible with canonical constraints

## Required Evidence

- experiment objective
- implementation summary
- validation results
- operational risk assessment
- governance impact assessment
- compatibility assessment
- rollback plan
- human approval record

## Review Requirements

- reviewer assessment required
- governance impact review required
- formatting/readability review required

## Audit Requirements

- auditability evidence must be explicit
- traceability IDs must be intact
- validation evidence must be reproducible

## Acceptance Criteria

Porting can be approved only when:
- tests and lint pass
- artifacts are readable and non-corrupted
- governance constraints remain enforced
- rollback path is documented
- human approval is present

## Rejection Criteria

Reject immediately when any of the following occurs:
- corrupted formatting
- unreadable artifacts
- invalid tests
- missing validation evidence
- governance boundary violations

## Rollback Expectations

Every proposal must include a rollback plan with:
- files affected
- revert approach
- risk statement

## Formatting and Readability Requirements

- markdown artifacts must be human-readable
- YAML and Python must be syntax-valid
- collapsed or malformed files must never be ported

## Operational Compatibility Expectations

- compatibility with canonical governance model required
- no autonomous runtime behavior
- no hidden memory behavior
- no unrestricted permissions

## Human Approval Requirements

Final porting decision requires explicit human approval.
