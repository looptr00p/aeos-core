# Feature Workflow

## Purpose

Define the end-to-end process for implementing new features within AEOS Core.

## Entry Criteria

- Objective is defined and approved (OBJ-XXX).
- ADR is created if architecture changes are needed (ADR-XXX).
- Human approval to proceed with feature implementation.

## Required Inputs

- Active objective (OBJ-XXX).
- ADR if architecture is affected (ADR-XXX).
- Defined acceptance criteria.
- Assigned implementer-agent.
- Assigned reviewer-agent.

## Lifecycle Stages

1. **Objective Definition**: Create OBJ-XXX using objective_template.md.
2. **Architecture Review**: If architecture is affected, create ADR-XXX.
3. **Task Definition**: Create TASK-XXX using task_template.md.
4. **Agent Assignment**: Assign implementer-agent and reviewer-agent.
5. **Implementation**: implementer-agent executes within defined scope.
6. **Review**: reviewer-agent conducts review per REVIEW_PROTOCOL.
7. **Validation**: qa-agent validates tests and acceptance criteria.
8. **Audit**: auditor-agent validates governance compliance.
9. **Human Approval**: Human reviews and approves (if required).
10. **Handoff**: implementer-agent produces HND-XXX.
11. **Memory Update**: documentation-agent updates memory artifacts.
12. **Close**: Task is marked complete.

## Validation Gates

- All tests must pass.
- All review types must pass per REVIEW_PROTOCOL.
- All acceptance criteria must be met.
- Audit must pass governance compliance.
- Human approval obtained (if required).

## Review Requirements

- Scope review by reviewer-agent.
- Implementation review by reviewer-agent.
- Governance review by auditor-agent.
- Validation review by qa-agent.
- Handoff review by reviewer-agent and director-agent.

## Artifacts Produced

- OBJ-XXX (objective)
- ADR-XXX (if applicable)
- TASK-XXX (task definition)
- REV-XXX (review report)
- AUD-XXX (audit report)
- HND-XXX (handoff report)

## Exit Criteria

- All validation gates pass.
- All reviews pass.
- Handoff report is complete.
- Memory is updated.
- Human approval obtained (if required).

## Failure Modes

- Objective lacks clear acceptance criteria → escalate.
- Architecture ADR not accepted → halt implementation.
- Review fails → return to implementation.
- Audit fails → escalate to director-agent.
- Human approval denied → close or revise task.

## Handoff Requirements

- Handoff report must follow HANDOFF_PROTOCOL.
- Handoff must be saved to memory/handoffs/.
- Handoff must include all artifacts produced.
