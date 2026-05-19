# Review Cadence

## Purpose

Define operational review cycles to maintain governance continuity and operational health.

## Daily Review

**Conducted by**: reviewer-agent, implementer-agent

**Scope**:
- Task continuity — are active tasks progressing within scope?
- Unresolved blockers — are there blocked tasks awaiting escalation?
- Workflow integrity — are workflows being followed without deviation?

**Artifacts**:
- Active TASK-XXX status check.
- Open ESC-XXX review.
- Handoff completeness check for completed tasks.

**Output**: Brief status note in memory/tasks/ or escalation if issues found.

**Duration**: Lightweight — no formal report required unless issues detected.

---

## Weekly Review

**Conducted by**: director-agent, auditor-agent

**Scope**:
- Governance review — are governance rules being followed?
- Workflow friction — are workflows causing delays or failures?
- Incident review — what incidents occurred? Are they resolved?
- Context continuity — is context complete for active objectives?

**Artifacts**:
- INC-XXX from the week.
- ESC-XXX from the week.
- REV-XXX from completed reviews.
- Active OBJ-XXX status.

**Output**: Weekly operational note using operational_report_template.md (abbreviated).

**Duration**: 1 operational cycle.

---

## Monthly Review

**Conducted by**: director-agent, auditor-agent, human

**Scope**:
- Operational metrics — task completion rate, incident frequency, escalation patterns.
- Governance drift — has governance been weakened or bypassed over time?
- Workflow effectiveness — are workflows still fit for purpose?
- Escalation analysis — are escalations being resolved promptly?

**Artifacts**:
- All INC-XXX from the month.
- All ESC-XXX from the month.
- All AUD-XXX from the month.
- All HND-XXX from the month.
- Operational report using operational_report_template.md.

**Output**: Monthly operational report using operational_report_template.md.

**Duration**: 1-2 operational cycles.

---

## Quarterly Review

**Conducted by**: director-agent, architect-agent, auditor-agent, human

**Scope**:
- Architecture review — is architecture still aligned with objectives?
- Governance simplification — can governance be simplified without weakening?
- Organizational scaling — is AEOS supporting multiple projects effectively?
- Phase assessment — should phase transition be considered?

**Artifacts**:
- All ADR-XXX from the quarter.
- All AUD-XXX from the quarter.
- Monthly operational reports.
- Architecture documentation.

**Output**: Quarterly review report with recommendations. ADR-XXX if governance changes are proposed.

**Duration**: 2-3 operational cycles.

---

## Cadence Enforcement

- Daily reviews are lightweight and may be skipped if no active tasks exist.
- Weekly reviews are mandatory if any tasks were active during the week.
- Monthly reviews are mandatory regardless of activity level.
- Quarterly reviews require human scheduling and approval.
- Missed reviews must be documented as incidents (INC-XXX).
