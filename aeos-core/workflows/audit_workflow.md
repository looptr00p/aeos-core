# Audit Workflow

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

## Exit Criteria

- All audit categories are completed.
- All findings are documented.
- All escalations are routed.
- Audit report is reviewed.

## Failure Modes

- Audit scope is too broad → narrow scope and re-plan.
- Audit scope is too narrow → expand scope with approval.
- Findings are disputed → escalate to director-agent.
- Audit trail is incomplete → document as finding.

## Handoff Requirements

- Audit report must follow AUDIT_TEMPLATE.
- Audit report must be saved to memory/audits/.
- All escalations must be documented.
