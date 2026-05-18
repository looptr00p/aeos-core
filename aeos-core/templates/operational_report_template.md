# Operational Report Template

**Report ID**: RPT-XXX
**Reporting Period**: YYYY-MM-DD to YYYY-MM-DD
**Prepared By**: [agent-id or human]
**Date**: YYYY-MM-DD

## Reporting Period

[Start date] to [End date]

## Objectives Completed

| ID | Title | Status | Handoff |
|----|-------|--------|---------|
| OBJ-XXX | [Title] | COMPLETED | HND-XXX |
| OBJ-XXX | [Title] | COMPLETED | HND-XXX |

## Tasks Completed

| ID | Title | Objective | Status | Handoff | Review |
|----|-------|-----------|--------|---------|--------|
| TASK-XXX | [Title] | OBJ-XXX | COMPLETE | HND-XXX | REV-XXX |
| TASK-XXX | [Title] | OBJ-XXX | COMPLETE | HND-XXX | REV-XXX |

## ADRs Created

| ID | Title | Status | Owner | Decision Summary |
|----|-------|--------|-------|------------------|
| ADR-XXX | [Title] | ACCEPTED | [agent-id] | [Summary] |
| ADR-XXX | [Title] | PROPOSED | [agent-id] | [Summary] |

## Audits Completed

| ID | Scope | Result | Auditor | Date |
|----|-------|--------|---------|------|
| AUD-XXX | [Scope] | PASS | [agent-id] | YYYY-MM-DD |
| AUD-XXX | [Scope] | FAIL | [agent-id] | YYYY-MM-DD |

## Governance Violations

| ID | Description | Severity | Resolution | Related Incident |
|----|-------------|----------|------------|------------------|
| [ID] | [Description] | [CRITICAL/HIGH/MEDIUM/LOW] | [Resolution] | INC-XXX |

## Incidents

| ID | Severity | Category | Status | Root Cause | Resolution |
|----|----------|----------|--------|------------|------------|
| INC-XXX | [Severity] | [Category] | RESOLVED | [Cause] | [Resolution] |
| INC-XXX | [Severity] | [Category] | OPEN | [Pending] | [Pending] |

## Risks

| Risk | Severity | Impact | Mitigation | Status |
|------|----------|--------|------------|--------|
| [Risk] | [Severity] | [Impact] | [Mitigation] | [OPEN/CLOSED] |

## Workflow Failures

| Workflow | Failure Point | Cause | Resolution |
|----------|---------------|-------|------------|
| [Workflow] | [Stage] | [Cause] | [Resolution] |

## Context Continuity Issues

| Issue | Description | Impact | Resolution |
|-------|-------------|--------|------------|
| [Issue] | [Description] | [Impact] | [Resolution] |

## Recommended Actions

- [Action 1]
- [Action 2]
- [Action 3]

## Open Escalations

| Escalation ID | Origin | Condition | Status | Assigned To |
|---------------|--------|-----------|--------|-------------|
| [ESC-XXX] | [agent-id] | [Condition] | OPEN | [agent-id/human] |

## Validation Results

- [ ] aeos_lint.py passed
- [ ] pytest passed
- [ ] All closed tasks reference objectives
- [ ] All closed tasks reference handoffs
- [ ] All ADR references valid
- [ ] All handoff references valid
- [ ] All incident references valid
