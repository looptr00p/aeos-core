# Operating Model

**Operational State**: STRATEGIC

## Overview

This document describes how AEOS Core operates in practice, including roles, responsibilities, and operational constraints.

## Roles

### Human Operator

- Ultimate decision authority.
- Approves critical changes.
- Resolves escalated issues.
- Defines objectives.
- Reviews and approves ADRs.

### Director Agent

- Owns governance direction.
- Routes escalations to human.
- Assigns agents to tasks.
- Validates phase transitions.
- Cannot implement code.

### Architect Agent

- Proposes architecture changes via ADRs.
- Maintains architecture documentation.
- Reviews implementations for architectural consistency.
- Cannot self-approve architecture.

### Implementer Agent

- Executes scoped implementation.
- Creates and modifies files within task scope.
- Produces handoff reports.
- Cannot expand scope.

### Reviewer Agent

- Validates correctness and compliance.
- Conducts scope, implementation, and handoff reviews.
- Cannot merge autonomously.
- Cannot review own work.

### Auditor Agent

- Validates governance compliance.
- Validates traceability and reproducibility.
- Conducts audits per audit workflow.
- Cannot implement changes.

### QA Agent

- Validates tests and acceptance criteria.
- Executes and validates CI checks.
- Cannot implement production code.

### Documentation Agent

- Updates documentation and memory.
- Maintains template currency.
- Cannot independently modify governance decisions.

## Operational Constraints

### Permission Model

All agents operate within defined permission levels:

- READ_ONLY: Read access only.
- DOCS_ONLY: Read + documentation write.
- TESTS_ONLY: Read + test write.
- LIMITED_IMPLEMENTATION: Read + scoped implementation write.
- CRITICAL_SYSTEM_CHANGE: Requires human approval.

### Review Requirements

All changes require review:

- Governance changes: director-agent + auditor-agent + human approval.
- Workflow changes: director-agent + reviewer-agent + human approval.
- Architecture changes: architect-agent + auditor-agent + human approval.
- CI changes: qa-agent + auditor-agent + human approval.
- Permission changes: director-agent + auditor-agent + human approval.
- Protocol changes: director-agent + auditor-agent + human approval.
- Memory changes: auditor-agent + human approval (for governance-relevant).

### Escalation

Agents escalate when:

- Requirements are unclear.
- Documentation conflicts.
- Validation fails.
- Permissions are unsafe.
- Acceptance criteria are missing.
- Architecture is uncertain.

Escalation routes to director-agent, then to human.

### Safety Rules

- No autonomous execution.
- No self-approval.
- No hidden memory.
- No unrestricted write access.
- No CI weakening.
- No deletion of audit trails.
- No uncontrolled tool access.

## Phase Progression

AEOS Core starts in Phase 0 (governance/bootstrap).

Phase transitions require human approval and documented justification.

See PHASE_POLICY.md for detailed phase definitions.
