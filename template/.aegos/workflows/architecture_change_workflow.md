# Architecture Change Workflow

> **State Graph Reference:** This workflow operates within the AEOS state graph defined in [state_graph.md](state_graph.md). All transitions and feedback loops follow the graph edges documented therein.

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

## State Graph Mapping

| Workflow Stage | State Graph Node | Responsible Agent | Output Artifact |
|----------------|------------------|-------------------|-----------------|
| Change Identification | `objective_defined` | director | OBJ-XXX |
| ADR Proposal + Review | `architecture_reviewed` | architect | ADR-XXX |
| Task Definition | `task_defined` | director | TASK-XXX |
| Implementation | `implementing` | implementer | Código + validación |
| Review | `reviewing` | reviewer | REV-XXX |
| Validation | `testing` | qa | Resultados de tests |
| Audit | `auditing` | auditor | AUD-XXX |
| Handoff | `handoff_complete` | director | HND-XXX |
| Close | `closed` | director | OBJ-XXX CLOSED |

## Feedback Loops

| Feedback Loop | Trigger | Condition | Action | Re-entry Path |
|---------------|---------|-----------|--------|---------------|
| `reviewing → implementing` | Reviewer finds issues in implementation | REV-XXX = REQUEST_CHANGES | Implementer addresses architecture gaps | implementing → reviewing |
| `testing → implementing` | Tests fail after architecture change | Test results = FAIL | Implementer fixes issues, updates tests | implementing → reviewing → testing |
| `auditing → reviewing` | Auditor finds gaps in architecture review | AUD-XXX = FAIL with review gaps | Reviewer re-reviews with focus on identified gaps | reviewing → testing |
| `auditing → objective_defined` | Auditor finds strategic inconsistency | Work doesn't align with OBJ-XXX or contradicts ADRs | Director re-aligns with human operator | objective_defined → ... |
| `implementing → architecture_reviewed` | Implementer discovers undocumented technical constraint | Current architecture insufficient or incorrect | Architect re-evaluates and creates/updates ADR | architecture_reviewed → task_defined → implementing |
| `implementing → task_defined` | Scope insufficient for architecture change | Cannot meet acceptance criteria with defined scope | Director expands TASK-XXX | task_defined → implementing |

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
- ST-NNN (state transition log for each state change)

## Exit Criteria

- ADR is accepted and implemented.
- All validation gates pass.
- All reviews pass.
- Architecture documentation is updated.
- Handoff report is complete.
- All state transitions logged in `memory/state-log/ST-NNN.md`.
- Final state transition recorded: `handoff_complete → closed`.

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
