# Bugfix Workflow

## Purpose

Define the end-to-end process for identifying, fixing, and validating bugs within AEOS Core.

## Entry Criteria

- Bug is identified and documented.
- Bug is classified by severity (CRITICAL / HIGH / MEDIUM / LOW).
- Human approval to proceed with fix (for CRITICAL/HIGH).

## Required Inputs

- Bug description with reproduction steps.
- Affected files and components.
- Severity classification.
- Assigned implementer-agent.
- Assigned reviewer-agent.

## Lifecycle Stages

1. **Bug Identification**: Document bug with reproduction steps.
2. **Severity Classification**: Classify bug severity.
3. **Task Definition**: Create TASK-XXX using task_template.md.
4. **Agent Assignment**: Assign implementer-agent and reviewer-agent.
5. **Root Cause Analysis**: implementer-agent identifies root cause.
6. **Implementation**: implementer-agent applies fix within scope.
7. **Review**: reviewer-agent validates fix correctness.
8. **Validation**: qa-agent validates tests pass and regression check.
9. **Human Approval**: Human approves (for CRITICAL/HIGH severity).
10. **Handoff**: implementer-agent produces HND-XXX.
11. **Memory Update**: documentation-agent updates memory artifacts.
12. **Close**: Task is marked complete.

## Validation Gates

- All tests must pass.
- Regression tests must pass.
- Fix must resolve the reported bug.
- Review must pass per REVIEW_PROTOCOL.

## Review Requirements

- Scope review by reviewer-agent.
- Implementation review by reviewer-agent.
- Validation review by qa-agent.
- Governance review by auditor-agent (if governance files affected).

## Artifacts Produced

- TASK-XXX (task definition)
- REV-XXX (review report)
- HND-XXX (handoff report)
- INC-XXX (if bug was a governance incident)

## Exit Criteria

- Bug is resolved and validated.
- All tests pass including regression tests.
- Review passes.
- Handoff report is complete.
- Human approval obtained (for CRITICAL/HIGH).

## Failure Modes

- Root cause cannot be identified → escalate to architect-agent.
- Fix introduces new bugs → return to implementation.
- Fix scope expands beyond bug → escalate to director-agent.
- Review fails → return to implementation.

## Handoff Requirements

- Handoff report must follow HANDOFF_PROTOCOL.
- Handoff must include root cause analysis.
- Handoff must include regression test results.
