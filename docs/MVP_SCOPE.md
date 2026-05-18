# MVP Scope

## Current Phase: Phase 0

AEOS Core v0 is in Phase 0: Governance/Bootstrap.

## MVP Deliverables

### Governance

- AGENTS.md: Universal agent constraints.
- PHASE_POLICY.md: Phase definitions and transitions.
- PERMISSION_MODEL.md: Permission levels and assignments.
- REVIEW_REQUIREMENTS.md: Review requirements by change category.
- ESCALATION_POLICY.md: Escalation conditions and process.
- SAFETY_RULES.md: Non-negotiable safety rules.

### Protocols

- TASK_PROTOCOL.md: Task definition and lifecycle.
- REVIEW_PROTOCOL.md: Review types and process.
- CONTEXT_PROTOCOL.md: Explicit context requirements.
- MEMORY_PROTOCOL.md: Explicit memory management.
- HANDOFF_PROTOCOL.md: Handoff report requirements.
- INCIDENT_PROTOCOL.md: Incident categorization and response.
- ADR_PROTOCOL.md: Architecture Decision Record process.

### Templates

- objective_template.md: Objective definition.
- adr_template.md: Architecture Decision Record.
- task_template.md: Task definition.
- review_template.md: Review report.
- audit_template.md: Audit report.
- handoff_template.md: Handoff report.
- incident_template.md: Incident report.

### Agents

- director-agent: Governance direction and approvals.
- architect-agent: Architecture proposals.
- implementer-agent: Scoped implementation.
- reviewer-agent: Validation and review.
- auditor-agent: Governance audit.
- qa-agent: Test validation.
- documentation-agent: Documentation updates.

### Workflows

- feature_workflow.md: New feature implementation.
- bugfix_workflow.md: Bug identification and fix.
- architecture_change_workflow.md: Architecture change process.
- audit_workflow.md: Governance audit process.
- incident_workflow.md: Incident response process.
- research_workflow.md: Research and analysis process.

### Memory Structure

- objectives/: Active and completed objectives.
- decisions/: ADRs and governance decisions.
- tasks/: Task definitions and status.
- handoffs/: Handoff reports.
- audits/: Review and audit records.
- incidents/: Incident reports.
- architecture/: Architecture documentation.
- research/: Research findings.

### Tests

- Governance file existence tests.
- Protocol file existence tests.
- Template file existence tests.
- Agent registry and field tests.
- Workflow file existence tests.

## Out of Scope for MVP

- Autonomous execution systems.
- Runtime orchestration.
- Database or vector store integration.
- API or networking layers.
- Frontend or web applications.
- Cloud infrastructure.
- Distributed systems.
- Plugin or extension systems.
- Self-modifying agents.
- Hidden memory systems.

## Success Criteria for MVP

- All governance files exist and are operationally useful.
- All protocols are defined and implementable.
- All templates are copy-paste ready.
- All agent definitions contain required fields.
- All workflows have entry/exit criteria and validation gates.
- Memory structure is in place.
- All tests pass.
- No autonomous runtime exists.
- No infrastructure complexity exists.
- No hidden autonomy exists.
