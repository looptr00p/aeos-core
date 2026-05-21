# Audit Workflow

> **State Graph Reference:** This workflow operates within the AEOS state graph defined in [state_graph.md](state_graph.md). All transitions and feedback loops follow the graph edges documented therein.

## Purpose

Define the process for conducting governance, traceability, and reproducibility audits within AEOS Core.

## Entry Criteria

- Scheduled audit cycle or triggered audit request.
- Audit scope is defined.
- Assigned auditor-agent.

## Required Inputs

- Audit scope definition.
- Access to all memory artifacts.
- Access to governance documents.
- Access to completed tasks and handoffs.

## Lifecycle Stages

1. **Audit Planning**: Define audit scope and criteria.
2. **Artifact Collection**: Gather all artifacts within scope.
3. **Governance Audit**: Validate compliance with governance documents.
4. **Traceability Audit**: Validate all artifacts are traceable.
5. **Reproducibility Audit**: Validate outputs are reproducible.
6. **Permission Audit**: Validate permission model compliance.
7. **Workflow Audit**: Validate workflow compliance.
8. **Findings Documentation**: Document all findings in AUD-XXX.
9. **Escalation**: Escalate CRITICAL/HIGH findings to director-agent.
10. **Recommendations**: Document recommendations for remediation.
11. **Close**: Audit is marked complete.

## State Graph Mapping

| Workflow Stage | State Graph Node | Responsible Agent | Output Artifact |
|----------------|------------------|-------------------|-----------------|
| Audit Planning | `objective_defined` | director | OBJ-XXX |
| Artifact Collection + Audit Execution | `auditing` | auditor | AUD-XXX |
| Findings Documentation | `auditing` | auditor | AUD-XXX + INC-XXX (si aplica) |
| Escalation | `objective_defined` (feedback) | director | Re-alignment |
| Close | `closed` | director | OBJ-XXX CLOSED |

## Feedback Loops

| Feedback Loop | Trigger | Condition | Action | Re-entry Path |
|---------------|---------|-----------|--------|---------------|
| `auditing → reviewing` | Auditor finds gaps in prior review | AUD-XXX = FAIL with review gaps | Reviewer re-reviews with focus on identified gaps | reviewing → testing |
| `auditing → objective_defined` | Auditor finds strategic inconsistency | Work doesn't align with OBJ-XXX or contradicts ADRs | Director re-aligns with human operator | objective_defined → ... |
| `auditing → auditing` | Audit scope insufficient | Findings incomplete for scope | Expand audit scope with approval | Re-execute audit categories |

## Validation Gates

- All audit categories must be covered.
- All findings must reference specific artifacts.
- All severity classifications must be justified.
- All recommendations must be actionable.

## Review Requirements

- Audit report reviewed by director-agent.
- CRITICAL/HIGH findings require human review.
- Audit methodology reviewed for completeness.

## Artifacts Produced

- AUD-XXX (audit report)
- INC-XXX (for CRITICAL/HIGH findings)
- Recommendations document
- ST-NNN (state transition log for each state change)

## Exit Criteria

- All audit categories are completed.
- All findings are documented.
- All escalations are routed.
- Audit report is reviewed.
- All state transitions logged in `memory/state-log/ST-NNN.md`.
- Final state transition recorded: `auditing → closed`.

## Failure Modes

- Audit scope is too broad → narrow scope and re-plan.
- Audit scope is too narrow → expand scope with approval.
- Findings are disputed → escalate to director-agent.
- Audit trail is incomplete → document as finding.

## Handoff Requirements

- Audit report must follow AUDIT_TEMPLATE.
- Audit report must be saved to memory/audits/.
- All escalations must be documented.
