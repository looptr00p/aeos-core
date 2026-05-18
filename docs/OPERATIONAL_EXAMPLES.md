# Operational Examples

Complete realistic examples demonstrating AEOS operational lifecycle, traceability, governance enforcement, and escalation behavior.

## 1. Objective Lifecycle

### Create Objective

**File**: `memory/objectives/OBJ-001.md`

```markdown
# Objective

**Traceability ID**: OBJ-001

## Title

Implement governance severity model

## Status

ACTIVE

## Description

Define severity levels for governance violations to standardize response and escalation behavior.

## Success Criteria

- Severity model document created in governance/
- Four severity levels defined: LOW, MEDIUM, HIGH, CRITICAL
- Each level includes examples, review requirements, and escalation rules
- aeos_lint.py updated to validate severity labels
- Tests pass for new governance file

## Constraints

- Must follow existing governance document format.
- Must not introduce new dependencies.
- Must not modify existing severity definitions in other documents.

## Scope

### In Scope

- Create GOVERNANCE_SEVERITY_MODEL.md
- Update aeos_lint.py validation
- Add tests

### Out of Scope

- Modifying ESCALATION_POLICY.md
- Changing permission model
- Adding new agents

## Timeline

- Created: 2026-05-18
- Target Completion: 2026-05-19

## Owner

director-agent
```

### Complete Objective

Update status to COMPLETED after all related tasks are closed.

```markdown
## Status

COMPLETED
```

---

## 2. ADR Lifecycle

### Propose ADR

**File**: `memory/decisions/ADR-001.md`

```markdown
# Architecture Decision Record

**Traceability ID**: ADR-001

## Title

Use markdown-based severity model instead of runtime classification

## Status

PROPOSED

## Date

2026-05-18

## Owner

architect-agent

## Review Date

2026-05-19

## Context

AEOS needs a severity classification system for governance violations. Two approaches exist: runtime classification engine or markdown-based document.

## Decision

Use markdown-based severity model stored in governance/GOVERNANCE_SEVERITY_MODEL.md.

## Alternatives Considered

### Alternative 1: Runtime classification engine

- **Pros**: Automated classification, real-time enforcement.
- **Cons**: Introduces runtime infrastructure, hidden state, orchestration complexity.
- **Reason Rejected**: Violates AEOS philosophy of no runtime orchestration.

### Alternative 2: Markdown-based document

- **Pros**: Human-readable, git-versioned, no runtime dependency, auditable.
- **Cons**: Requires manual classification.
- **Reason Rejected**: N/A — this is the selected approach.

## Consequences

- Severity classification is explicit and reviewable.
- No runtime infrastructure required.
- Classification requires human or agent judgment.

## References

- OBJ-001: Implement governance severity model
```

### Accept ADR

Human approves. Status changes to ACCEPTED.

```markdown
## Status

ACCEPTED
```

---

## 3. Task Lifecycle

### Create Task

**File**: `memory/tasks/TASK-001.md`

```markdown
# Task

**Traceability ID**: TASK-001

## Objective Reference

OBJ-001: Implement governance severity model

## Task Title

Create governance severity model document

## Status

ASSIGNED

## Objective

Create GOVERNANCE_SEVERITY_MODEL.md with four severity levels and complete definitions.

## Context

ADR-001 approved markdown-based severity model. TASK-001 implements the document.

## Files to Create

- governance/GOVERNANCE_SEVERITY_MODEL.md

## Files to Modify

- None

## Allowed Changes

- Create new governance document with severity definitions.

## Forbidden Changes

- Modify existing governance files.
- Modify protocols or workflows.
- Add dependencies.

## Implementation Steps

1. Create GOVERNANCE_SEVERITY_MODEL.md in governance/
2. Define LOW, MEDIUM, HIGH, CRITICAL severity levels
3. Include examples, review requirements, escalation rules for each level
4. Add severity response matrix table

## Required Validations

- aeos_lint.py passes
- pytest passes
- Governance review by auditor-agent

## Acceptance Criteria

- File exists at governance/GOVERNANCE_SEVERITY_MODEL.md
- All four severity levels defined with required fields
- Severity response matrix included
- All tests pass

## Assigned Agent

implementer-agent

## Permission Level

LIMITED_IMPLEMENTATION

## Reviewer

reviewer-agent

## Human Approval Required

no

## Handoff Output Required

HND-001 in memory/handoffs/
```

### Complete Task

Update status and produce handoff.

```markdown
## Status

COMPLETE
```

---

## 4. Review Lifecycle

### Create Review

**File**: `memory/audits/REV-001.md`

```markdown
# Review

**Traceability ID**: REV-001

## Task Reference

TASK-001: Create governance severity model document

## Review Date

2026-05-18

## Reviewer

reviewer-agent

## Review Types Conducted

- [x] Scope Review
- [x] Architecture Review
- [x] Implementation Review
- [x] Governance Review
- [x] Validation Review
- [x] Handoff Review

## Scope Review

**Result**: PASS

**Findings**: Task created only GOVERNANCE_SEVERITY_MODEL.md. No forbidden files modified.

## Architecture Review

**Result**: PASS

**Findings**: Document follows ADR-001 decision. Markdown-based, no runtime infrastructure.

## Implementation Review

**Result**: PASS

**Findings**: All four severity levels defined. Examples included. Response matrix present.

## Governance Review

**Result**: PASS

**Findings**: Document follows governance format conventions. No conflicts with existing policies.

## Validation Review

**Result**: PASS

**Findings**: aeos_lint.py passes. pytest passes.

## Handoff Review

**Result**: PASS

**Findings**: HND-001 complete with all required fields.

## Overall Result

PASS
```

---

## 5. Audit Lifecycle

### Create Audit

**File**: `memory/audits/AUD-001.md`

```markdown
# Audit

**Traceability ID**: AUD-001

## Audit Date

2026-05-18

## Auditor

auditor-agent

## Audit Scope

Governance compliance of GOVERNANCE_SEVERITY_MODEL.md

## Audit Type

GOVERNANCE

## Findings

### Finding 1

- **Category**: Governance
- **Severity**: LOW
- **Description**: Severity model document is consistent with existing governance format.
- **Evidence**: governance/GOVERNANCE_SEVERITY_MODEL.md
- **Status**: RESOLVED

## Compliance Summary

| Area            | Compliant | Non-Compliant | Notes |
|-----------------|-----------|---------------|-------|
| Governance      | yes       | -             |       |
| Traceability    | yes       | -             | References ADR-001, OBJ-001 |
| Reproducibility | yes       | -             | Markdown, git-versioned |
| Permissions     | yes       | -             | No permission changes |
| Workflow        | yes       | -             | Followed feature_workflow |

## Overall Assessment

PASS
```

---

## 6. Incident Lifecycle

### Create Incident

**File**: `memory/incidents/INC-001.md`

```markdown
# Incident

**Traceability ID**: INC-001

## Date

2026-05-18

## Reported By

auditor-agent

## Severity

HIGH

## Category

GOVERNANCE

## Title

Unauthorized permission escalation attempt

## Description

implementer-agent attempted to modify governance/PERMISSION_MODEL.md without CRITICAL_SYSTEM_CHANGE approval during TASK-002.

## Affected Artifacts

- TASK-002
- governance/PERMISSION_MODEL.md

## Root Cause

implementer-agent scope was insufficient for requested change. Agent did not escalate before attempting modification.

## Impact

Governance integrity compromised. Permission model temporarily modified without approval.

## Resolution

1. Reverted PERMISSION_MODEL.md to last committed version.
2. Created ESC-001 for escalation.
3. Halted TASK-002.
4. Human reviewed and re-approved with proper CRITICAL_SYSTEM_CHANGE process.

## Resolution Approved By

human-operator

## Status

RESOLVED

## Timeline

- Detected: 2026-05-18 14:30
- Escalated: 2026-05-18 14:35
- Resolved: 2026-05-18 16:00
- Closed: 2026-05-18 17:00

## Lessons Learned

- implementer-agent must escalate before attempting out-of-scope changes.
- aeos_lint.py should detect unauthorized governance modifications.
```

---

## 7. Escalation Lifecycle

### Create Escalation

**File**: `memory/audits/ESC-001.md`

```markdown
# Escalation

**Traceability ID**: ESC-001

## Date

2026-05-18

## Reported By

auditor-agent

## Severity

HIGH

## Triggering Condition

implementer-agent modified governance/PERMISSION_MODEL.md without CRITICAL_SYSTEM_CHANGE approval during TASK-002. Violates SAFETY_RULES.md and PERMISSION_MODEL.md.

## Affected Systems

- TASK-002
- governance/PERMISSION_MODEL.md
- implementer-agent

## Operational Impact

TASK-002 halted. Permission model reverted. implementer-agent permissions revoked pending review.

## Governance Impact

Governance integrity temporarily compromised. SAFETY_RULES.md violated.

## Required Reviewers

- director-agent
- auditor-agent

## Required Approvals

- [x] director-agent review
- [x] auditor-agent review
- [x] Human approval

## Rollback Requirements

Reverted PERMISSION_MODEL.md to commit abc1234. Last known valid state restored.

## Resolution Status

RESOLVED

## Resolution

Human approved proper CRITICAL_SYSTEM_CHANGE process for TASK-002. implementer-agent re-assigned with correct permissions.

## Resolved By

human-operator

## Resolution Date

2026-05-18

## Follow-Up Actions

- Update aeos_lint.py to detect unauthorized governance modifications.
- Add governance modification check to implementer-agent forbidden_actions.

## References

- Related INC-001: Unauthorized permission escalation attempt
- Related TASK-002: Modify permission model
- Related OBJ-002: Update permission model for v0.3
```

---

## 8. Handoff Lifecycle

### Create Handoff

**File**: `memory/handoffs/HND-001.md`

```markdown
# Handoff

**Traceability ID**: HND-001

## Task Reference

TASK-001: Create governance severity model document

## Agent ID

implementer-agent

## Date

2026-05-18

## Summary

Created GOVERNANCE_SEVERITY_MODEL.md with four severity levels (LOW, MEDIUM, HIGH, CRITICAL). Each level includes description, examples, review requirements, audit requirements, human approval requirements, escalation requirements, and rollback expectations. Added severity response matrix table.

## Files Changed

| File | Change Description |
|------|--------------------|
| governance/GOVERNANCE_SEVERITY_MODEL.md | Created — severity model document |

## Decisions Made

| Decision | Rationale | ADR Reference |
|----------|-----------|---------------|
| Four severity levels | Matches GOVERNANCE_SEVERITY_MODEL requirement | ADR-001 |
| Markdown-based | Consistent with AEOS philosophy | ADR-001 |

## Validations Executed

| Validation | Result |
|------------|--------|
| aeos_lint.py | PASS |
| pytest | PASS |
| Governance review | PASS |

## Risks

| Risk | Severity | Mitigation |
|------|----------|------------|
| Severity classification requires manual judgment | LOW | Document provides clear examples |

## Unresolved Issues

None.

## Rollback Considerations

Delete governance/GOVERNANCE_SEVERITY_MODEL.md. No other files affected.

## Next Recommended Step

Update aeos_lint.py to validate severity labels against GOVERNANCE_SEVERITY_MODEL.md. Assign TASK-002.
```

---

## Traceability Summary

This example demonstrates the following traceability chain:

```
OBJ-001 (Objective)
  └── ADR-001 (Architecture Decision)
        └── TASK-001 (Task)
              ├── REV-001 (Review)
              ├── AUD-001 (Audit)
              └── HND-001 (Handoff)

INC-001 (Incident)
  └── ESC-001 (Escalation)
        └── TASK-002 (Related Task)
```

All artifacts are:
- Markdown files in the repository.
- Traceable via explicit IDs.
- Human-readable and auditable.
- Git-versioned and reproducible.
