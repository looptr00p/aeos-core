# Architecture Change Workflow

## Purpose

Define the end-to-end process for proposing, reviewing, and implementing architecture changes within AEOS Core.

## Entry Criteria

- Architecture change is identified as necessary.
- Current architecture documentation is referenced.
- Human approval to proceed with architecture review.

## Required Inputs

- Description of proposed architecture change.
- Current architecture documentation.
- Affected components and files.
- Assigned architect-agent.
- Assigned reviewer-agent.

## Lifecycle Stages

1. **Change Identification**: Document the need for architecture change.
2. **ADR Proposal**: architect-agent creates ADR-XXX using adr_template.md.
3. **ADR Review**: reviewer-agent and auditor-agent review ADR.
4. **Human Approval**: Human approves or rejects ADR.
5. **Task Definition**: If ADR accepted, create TASK-XXX for implementation.
6. **Agent Assignment**: Assign implementer-agent and reviewer-agent.
7. **Implementation**: implementer-agent executes within defined scope.
8. **Review**: reviewer-agent conducts architecture and implementation review.
9. **Validation**: qa-agent validates tests pass.
10. **Audit**: auditor-agent validates governance compliance.
11. **Handoff**: implementer-agent produces HND-XXX.
12. **Memory Update**: documentation-agent updates architecture documentation.
13. **Close**: Task is marked complete, ADR status updated.

## Validation Gates

- ADR must follow ADR_PROTOCOL.
- ADR must include alternatives considered.
- All tests must pass after implementation.
- Architecture review must pass.
- Governance review must pass.
- Human approval for ADR is required.

## Review Requirements

- Architecture review by architect-agent and auditor-agent.
- Implementation review by reviewer-agent.
- Governance review by auditor-agent.
- Validation review by qa-agent.
- ADR review by director-agent.

## Artifacts Produced

- ADR-XXX (architecture decision record)
- TASK-XXX (task definition)
- REV-XXX (review report)
- AUD-XXX (audit report)
- HND-XXX (handoff report)
- Updated architecture documentation

## Exit Criteria

- ADR is accepted and implemented.
- All validation gates pass.
- All reviews pass.
- Architecture documentation is updated.
- Handoff report is complete.

## Failure Modes

- ADR rejected by human → close or revise.
- ADR lacks alternatives → return to architect-agent.
- Implementation deviates from ADR → escalate.
- Architecture review fails → return to implementation.
- Governance violation detected → escalate to director-agent.

## Handoff Requirements

- Handoff report must follow HANDOFF_PROTOCOL.
- Handoff must reference the ADR.
- Handoff must include updated architecture documentation locations.
