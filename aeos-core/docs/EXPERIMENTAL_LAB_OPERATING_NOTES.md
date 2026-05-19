# Experimental Lab Operating Notes

## Purpose

Operate `aeos-core` as a controlled governance experiment repository.

## What Belongs Here

- governance enforcement experiments
- traceability and lifecycle experiments
- validation experiments
- controlled portability evaluations

## What Does Not Belong Here

- canonical production governance changes
- autonomous workflow execution
- cross-repo synchronization tooling
- runtime orchestration infrastructure

## How Experiments Should Be Proposed

1. Define objective, scope, and non-goals.
2. Define risks and validation criteria.
3. Record explicit experiment and task artifacts.

## How Experiments Should Be Evaluated

1. Run deterministic lint/tests.
2. Perform review and audit checks.
3. Record decision with conditions or defer.

## How Porting Candidates Should Be Handled

- use `PORT-` review artifacts
- require compatibility and readability checks
- require explicit human approval before any canonical migration

## What Should Never Be Automated

- governance approval authority
- permission escalation decisions
- audit judgment
- escalation resolution
- risk acceptance decisions

## When to Stop and Request Human Review

- unclear scope or governance intent
- validation failures with ambiguous impact
- potential canonical impact
- requests that imply automatic porting or cross-repo automation
