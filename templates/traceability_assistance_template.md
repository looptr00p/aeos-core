# Traceability Assistance Template

**Traceability ID**: TRL-XXX
**Date**: YYYY-MM-DD
**Prepared By**: [agent-id or human]

## Purpose

Structured helper for tracking traceability relationships within a specific objective or task cycle. This is NOT automation — it is a human-readable artifact that reduces manual traceability overhead.

## Linked Objective IDs

| ID | Title | Status | Present |
|----|-------|--------|---------|
| OBJ-XXX | [Title] | [Status] | [YES/NO] |

## Linked Task IDs

| ID | Title | Status | References OBJ | References HND | Present |
|----|-------|--------|---------------|----------------|---------|
| TASK-XXX | [Title] | [Status] | OBJ-XXX | HND-XXX | [YES/NO] |

## Linked Review IDs

| ID | Task | Result | Reviewer | Present |
|----|------|--------|----------|---------|
| REV-XXX | TASK-XXX | [Result] | [agent-id] | [YES/NO] |

## Linked Audit IDs

| ID | Task | Result | Auditor | Present |
|----|------|--------|---------|---------|
| AUD-XXX | TASK-XXX | [Result] | [agent-id] | [YES/NO] |

## Linked Escalation IDs

| ID | Severity | Category | Status | Present |
|----|----------|----------|--------|---------|
| ESC-XXX | [Severity] | [Category] | [Status] | [YES/NO] |
| INC-XXX | [Severity] | [Category] | [Status] | [YES/NO] |

## Linked Handoff IDs

| ID | Task | Agent | Next Step | Present |
|----|------|-------|-----------|---------|
| HND-XXX | TASK-XXX | [agent-id] | [Next step] | [YES/NO] |

## Unresolved References

| Reference | Expected In | Found | Status |
|-----------|------------|-------|--------|
| [ID] | [File] | [YES/NO] | [RESOLVED/OPEN] |

## Missing Lifecycle Artifacts

| Expected Artifact | Required By | Status |
|------------------|-------------|--------|
| [e.g., HND-XXX for TASK-XXX] | [TASK-XXX] | [PRESENT/MISSING] |

## Closure Checklist

- [ ] All tasks reference a valid objective
- [ ] All closed tasks reference a handoff
- [ ] All reviews reference a valid task
- [ ] All audits reference a valid task and review
- [ ] All handoffs reference a valid task, review, and audit
- [ ] All escalations reference affected artifacts
- [ ] No orphaned artifacts detected
- [ ] All traceability IDs follow correct prefix format

## Notes

[Any observations about traceability completeness or inconsistencies]
