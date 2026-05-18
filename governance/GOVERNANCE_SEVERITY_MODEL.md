# Governance Severity Model

## Purpose

Classify governance violations and changes by severity to determine required review, audit, and escalation responses.

## Severity Levels

### LOW

**Description**: Minor issues with no governance impact. Cosmetic or formatting changes.

**Examples**:
- Markdown typo in documentation.
- Formatting adjustment in non-governance files.
- Clarification in existing documentation without semantic change.

**Required Review**: None. Standard documentation review if applicable.

**Required Audit**: None.

**Human Approval**: Not required.

**Escalation**: Not required unless pattern indicates systemic issue.

**Rollback**: Not required.

---

### MEDIUM

**Description**: Changes that affect workflows, protocols, or documentation semantics but do not weaken governance.

**Examples**:
- Workflow modification that preserves governance boundaries.
- Protocol clarification that does not alter enforcement.
- Template update that adds fields without removing requirements.
- Agent definition update that does not expand permissions.

**Required Review**: reviewer-agent conducts scope and implementation review.

**Required Audit**: auditor-agent validates no governance drift occurred.

**Human Approval**: Recommended.

**Escalation**: Required if review finds governance boundary violation.

**Rollback**: Recommended if governance drift is detected.

---

### HIGH

**Description**: Changes that directly affect governance policies, validation logic, or permissions.

**Examples**:
- Governance policy modification (AGENTS.md, PERMISSION_MODEL.md, SAFETY_RULES.md).
- Validation logic changes in aeos_lint.py.
- Permission level modifications.
- Protocol changes that alter enforcement behavior.
- Test removal or modification that reduces coverage.

**Required Review**: reviewer-agent conducts full review. auditor-agent conducts governance review. director-agent validates direction.

**Required Audit**: Full audit per audit_workflow.md. AUD-XXX required.

**Human Approval**: Required.

**Escalation**: Required before implementation begins.

**Rollback**: Required if human approval is withdrawn or audit fails.

---

### CRITICAL

**Description**: Violations or changes that compromise AEOS governance integrity.

**Examples**:
- CI weakening or validation gate removal.
- Workflow bypass attempts.
- Hidden memory introduction.
- Autonomous execution attempts.
- Permission escalation without approval.
- Audit trail deletion attempts.
- Self-approval attempts.
- Safety rule violations.

**Required Review**: Immediate review by director-agent, auditor-agent, and reviewer-agent.

**Required Audit**: Emergency audit. AUD-XXX with CRITICAL severity.

**Human Approval**: Required before any further operations.

**Escalation**: Immediate escalation to human. All affected operations halted.

**Rollback**: Mandatory. Affected operations must be restored to last known valid state.

## Severity Assignment Rules

- Severity is assigned by the detecting agent or human.
- If severity is uncertain, assign the higher level.
- Severity can be downgraded only by human approval.
- Severity can be upgraded by any agent at any time.
- All severity assignments must be documented in an incident report (INC-XXX) or escalation report (ESC-XXX).

## Severity Response Matrix

| Severity | Response Time | Halt Operations | Human Approval | Audit Required |
|----------|--------------|-----------------|----------------|----------------|
| LOW      | Next cycle   | No              | No             | No             |
| MEDIUM   | Within 1 cycle | No            | Recommended    | Yes            |
| HIGH     | Immediate    | Affected only   | Required       | Yes            |
| CRITICAL | Immediate    | All             | Required       | Emergency      |
