# Bugfix Workflow

> **State Graph Reference:** This workflow operates within the AEOS state graph defined in [state_graph.md](state_graph.md). All transitions and feedback loops follow the graph edges documented therein.

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

## State Graph Mapping

| Workflow Stage | State Graph Node | Responsible Agent | Output Artifact |
|----------------|------------------|-------------------|-----------------|
| Bug Identification | `objective_defined` | director | OBJ-XXX |
| Task Definition | `task_defined` | director | TASK-XXX |
| Root Cause Analysis + Implementation | `implementing` | implementer | Código + validación |
| Review | `reviewing` | reviewer | REV-XXX |
| Validation | `testing` | qa | Resultados de tests |
| Handoff | `handoff_complete` | director | HND-XXX |
| Close | `closed` | director | OBJ-XXX CLOSED |

## Feedback Loops

| Feedback Loop | Trigger | Condition | Action | Re-entry Path |
|---------------|---------|-----------|--------|---------------|
| `reviewing → implementing` | Reviewer finds issues in fix | REV-XXX = REQUEST_CHANGES | Implementer addresses specific issues from REV-XXX | implementing → reviewing |
| `testing → implementing` | Tests fail or regression detected | Test results = FAIL | Implementer fixes bugs, updates tests | implementing → reviewing → testing |
| `testing → task_defined` | Acceptance criteria unclear for testing | Cannot define clear tests against criteria | Director redefines TASK-XXX with clearer criteria | task_defined → implementing → testing |
| `implementing → task_defined` | Scope insufficient for fix | Cannot meet acceptance criteria with defined scope | Director expands TASK-XXX with new scope | task_defined → implementing |

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
- ST-NNN (state transition log for each state change)

## Exit Criteria

- Bug is resolved and validated.
- All tests pass including regression tests.
- Review passes.
- Handoff report is complete.
- Human approval obtained (for CRITICAL/HIGH).
- All state transitions logged in `memory/state-log/ST-NNN.md`.
- Final state transition recorded: `handoff_complete → closed`.

## Failure Modes

- Root cause cannot be identified → escalate to architect-agent.
- Fix introduces new bugs → return to implementation.
- Fix scope expands beyond bug → escalate to director-agent.
- Review fails → return to implementation.

## Handoff Requirements

- Handoff report must follow HANDOFF_PROTOCOL.
- Handoff must include root cause analysis.
- Handoff must include regression test results.
