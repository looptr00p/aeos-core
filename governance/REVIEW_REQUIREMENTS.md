# REVIEW_REQUIREMENTS.md

## Review Requirements

All changes within AEOS Core MUST undergo review. The type and depth of review depends on the change category.

### Governance Changes

- Files: `governance/*.md`
- Review Type: Full governance review.
- Required Reviewers: director-agent, auditor-agent.
- Human Approval: REQUIRED.
- Documentation: ADR required.
- Validation: All tests must pass after change.

### Workflow Changes

- Files: `workflows/*.md`
- Review Type: Workflow and governance review.
- Required Reviewers: director-agent, reviewer-agent.
- Human Approval: REQUIRED.
- Documentation: ADR required if workflow logic changes.
- Validation: Workflow consistency check.

### Architecture Changes

- Files: `memory/architecture/*`, agent definitions, protocols.
- Review Type: Architecture and governance review.
- Required Reviewers: architect-agent, auditor-agent.
- Human Approval: REQUIRED.
- Documentation: ADR required.
- Validation: Architecture consistency check.

### CI Changes

- Files: `pyproject.toml`, test files, CI configuration.
- Review Type: Validation and governance review.
- Required Reviewers: qa-agent, auditor-agent.
- Human Approval: REQUIRED.
- Documentation: ADR required if CI logic changes.
- Validation: All tests must pass.

### Permission Changes

- Files: `governance/PERMISSION_MODEL.md`, agent permission definitions.
- Review Type: Full governance and security review.
- Required Reviewers: director-agent, auditor-agent.
- Human Approval: REQUIRED.
- Documentation: ADR required.
- Validation: Permission model consistency check.

### Protocol Changes

- Files: `protocols/*.md`
- Review Type: Protocol and governance review.
- Required Reviewers: director-agent, auditor-agent.
- Human Approval: REQUIRED.
- Documentation: ADR required.
- Validation: Protocol consistency check.

### Memory Changes

- Files: `memory/*`
- Review Type: Governance review.
- Required Reviewers: auditor-agent.
- Human Approval: REQUIRED for governance-relevant memory.
- Documentation: Reference to originating task or decision.
- Validation: Memory format and traceability check.

### Review Process

1. Change is proposed with explicit scope.
2. Assigned reviewers conduct review per REVIEW_PROTOCOL.
3. Review results are documented.
4. Human approval is obtained (where required).
5. Change is applied or rejected.
6. Audit trail is updated.
