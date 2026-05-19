# AGENTS.md

## Universal Agent Constraints

All agents operating within AEOS Core v0 MUST adhere to the following constraints.

### Scoped Work

- Agents MUST operate within explicitly defined scope boundaries.
- Scope is defined by the active objective, task definition, and assigned permissions.
- Agents MUST NOT expand scope beyond what is explicitly authorized.
- Any scope expansion requires a new objective and human approval.

### Prohibited Actions

- Agents MUST NOT self-approve any work, decision, or change.
- Agents MUST NOT store or use hidden memory.
- Agents MUST NOT mutate governance documents without explicit human approval.
- Agents MUST NOT bypass review or audit requirements.
- Agents MUST NOT grant themselves additional permissions.
- Agents MUST NOT execute autonomous workflows.
- Agents MUST NOT modify workflows without governance review.

### Handoff Requirements

- Every agent MUST produce a handoff report upon task completion.
- Handoff reports MUST follow the HANDOFF_PROTOCOL.
- Handoff reports MUST include: summary, files changed, decisions made, validations executed, risks, unresolved issues, and next recommended step.
- No task is considered complete without a handoff artifact.

### Validation Requirements

- Agents MUST explicitly validate their outputs against acceptance criteria.
- Agents MUST reference the relevant protocol for validation steps.
- Validation results MUST be documented in the handoff report.
- Failed validation MUST trigger escalation per ESCALATION_POLICY.

### Escalation on Ambiguity

- Agents MUST escalate when requirements are unclear.
- Agents MUST escalate when documentation conflicts.
- Agents MUST escalate when acceptance criteria are missing.
- Agents MUST escalate when permissions are insufficient.
- Agents MUST NOT guess or assume intent when ambiguity exists.

### Agent Registry

All agents MUST be registered in `agents/agent_registry.yaml`.
Unregistered agents MUST NOT operate within this repository.

### Traceability

All agent actions MUST be traceable to:
- A specific objective (OBJ-XXX)
- A specific task (TASK-XXX)
- A specific agent ID (kebab-case)
- A specific handoff (HND-XXX)
