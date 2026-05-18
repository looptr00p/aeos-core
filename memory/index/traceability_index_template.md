# Traceability Index Template

**Index ID**: IDX-XXX
**Date**: YYYY-MM-DD
**Created By**: [agent-id or human]

## Scope

[Description of what this index covers — e.g., specific objective, sprint, or audit period]

## Artifact Map

### Objectives

| ID | Title | Status | Related ADRs | Related Tasks |
|----|-------|--------|-------------|---------------|
| OBJ-XXX | [Title] | [Status] | [ADR-XXX] | [TASK-XXX] |

### Architecture Decisions

| ID | Title | Status | Related Tasks | Supersedes |
|----|-------|--------|---------------|------------|
| ADR-XXX | [Title] | [Status] | [TASK-XXX] | [ADR-XXX or N/A] |

### Tasks

| ID | Title | Status | Objective | Handoff | Review | Audit |
|----|-------|--------|-----------|---------|--------|-------|
| TASK-XXX | [Title] | [Status] | OBJ-XXX | HND-XXX | REV-XXX | AUD-XXX |

### Reviews

| ID | Task | Result | Reviewer | Date |
|----|------|--------|----------|------|
| REV-XXX | TASK-XXX | [PASS/FAIL] | [agent-id] | YYYY-MM-DD |

### Audits

| ID | Scope | Result | Auditor | Date |
|----|-------|--------|---------|------|
| AUD-XXX | [Scope] | [PASS/FAIL] | [agent-id] | YYYY-MM-DD |

### Handoffs

| ID | Task | Agent | Date | Next Step |
|----|------|-------|------|-----------|
| HND-XXX | TASK-XXX | [agent-id] | YYYY-MM-DD | [Description] |

### Incidents

| ID | Severity | Category | Status | Related Artifacts |
|----|----------|----------|--------|-------------------|
| INC-XXX | [Severity] | [Category] | [Status] | [TASK-XXX, OBJ-XXX] |

## Traceability Gaps

| Gap | Description | Impact | Resolution |
|-----|-------------|--------|------------|
| [Gap ID] | [Description] | [Impact] | [Resolution or ESCALATED] |

## Validation Results

- [ ] All tasks reference valid objectives
- [ ] All closed tasks reference handoffs
- [ ] All ADR references use valid prefixes
- [ ] All handoff references use valid prefixes
- [ ] All incident references use valid prefixes
- [ ] No orphaned artifacts detected

## Notes

[Additional context, observations, or recommendations]
