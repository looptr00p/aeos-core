# Workflow Tiering Guidance

**Operational State**: EXPERIMENTAL

## Purpose

Reduce governance overhead for low-risk operational work without weakening governance invariants.

This is GUIDANCE ONLY. It does not change governance rules, permission models, or escalation policies.

## Governance Invariants (Never Weakened)

- Human approval still exists for all governance-relevant changes.
- Audits still exist for all completed tasks.
- Reviews still exist for all completed tasks.
- Governance is never bypassed regardless of tier.
- Escalation lifecycle remains mandatory when conditions are met.
- Traceability IDs remain mandatory for all artifacts.
- Handoff reports remain mandatory for all completed tasks.

## Tier Definitions

### LOW

**Description**: Changes with no governance, architecture, or CI impact. Purely operational or documentation changes.

**Examples**:
- Documentation updates (non-governance files).
- Template formatting adjustments.
- Memory artifact creation (OBJ, TASK, REV, AUD, HND).
- Research findings documentation.

**Recommended Workflow Intensity**: Lightweight (4-6 stages).
- Objective reference → Task definition → Implementation → Review → Handoff → Close.
- Skip: ADR, architecture review, CI validation (unless CI files affected).

**Recommended Review Depth**: Combined implementation + validation review.
- Scope review + validation review combined into single review pass.
- Governance review: lightweight check (no governance files modified).

**Recommended Audit Depth**: Lightweight audit.
- Verify traceability IDs present.
- Verify handoff complete.
- Verify no forbidden files modified.

**Recommended Documentation Requirements**: Standard templates. No additional documentation.

**Recommended Approval Requirements**: Director-agent review sufficient. Human approval recommended but not mandatory unless governance boundary is uncertain.

---

### MEDIUM

**Description**: Changes that affect workflows, protocols, or documentation semantics but do not weaken governance.

**Examples**:
- Workflow modification that preserves governance boundaries.
- Protocol clarification that does not alter enforcement.
- Template update that adds fields without removing requirements.
- Agent definition update that does not expand permissions.

**Recommended Workflow Intensity**: Standard (8-10 stages).
- Full workflow minus ADR (unless architecture affected).
- Include: Objective → ADR (if needed) → Task → Implementation → Review → Audit → Validation → Handoff → Close.

**Recommended Review Depth**: Separate review types.
- Scope review (separate).
- Implementation review (separate).
- Governance review (separate).
- Validation review (may combine with implementation if no code changes).

**Recommended Audit Depth**: Standard audit.
- Full compliance summary.
- Traceability verification.
- Governance boundary check.

**Recommended Documentation Requirements**: Standard templates. ADR if workflow or protocol semantics change.

**Recommended Approval Requirements**: Human approval recommended. Director-agent + auditor-agent review required.

---

### HIGH

**Description**: Changes that directly affect governance policies, validation logic, or permissions.

**Examples**:
- Governance policy modification.
- Validation logic changes in aeos_lint.py.
- Permission level modifications.
- Protocol changes that alter enforcement behavior.
- Test removal or modification that reduces coverage.

**Recommended Workflow Intensity**: Full (12 stages).
- Complete workflow with all stages.
- ADR mandatory.
- All review types mandatory.

**Recommended Review Depth**: Full separation.
- All 6 review types conducted separately.
- No consolidation allowed.

**Recommended Audit Depth**: Full audit.
- Complete compliance summary.
- Full traceability verification.
- Governance boundary verification.
- Severity classification documented.

**Recommended Documentation Requirements**: All templates. ADR mandatory. Operational report recommended.

**Recommended Approval Requirements**: Human approval REQUIRED. Director-agent + auditor-agent + reviewer-agent review required.

---

### CRITICAL

**Description**: Changes that compromise AEOS governance integrity or attempt to bypass governance.

**Examples**:
- CI weakening or validation gate removal.
- Workflow bypass attempts.
- Hidden memory introduction.
- Autonomous execution attempts.
- Permission escalation without approval.
- Audit trail deletion attempts.

**Recommended Workflow Intensity**: Full + emergency procedures.
- All workflow stages.
- Emergency escalation before implementation begins.
- Human approval before any work starts.

**Recommended Review Depth**: Emergency full review.
- All 6 review types.
- Additional security review.
- Governance integrity verification.

**Recommended Audit Depth**: Emergency audit.
- Full audit with CRITICAL severity.
- Immediate escalation to human.
- All affected operations halted until resolved.

**Recommended Documentation Requirements**: All templates. Incident report mandatory. Escalation report mandatory.

**Recommended Approval Requirements**: Human approval REQUIRED before any work. Director-agent + auditor-agent + reviewer-agent emergency review.

---

## Tier Assignment Rules

- Tier is assigned during task definition (TASK-XXX).
- If tier is uncertain, assign the higher tier.
- Tier can be upgraded by any agent at any time.
- Tier can be downgraded only by human approval.
- Tier assignment must be documented in the task definition.

## Relationship to GOVERNANCE_SEVERITY_MODEL.md

Workflow tiering guidance is operational guidance for process intensity. GOVERNANCE_SEVERITY_MODEL.md defines violation severity and response requirements. They are complementary:

- Tier determines process intensity during normal operation.
- Severity determines response when something goes wrong.
- A LOW-tier change can still have HIGH severity if it violates governance.
- A HIGH-tier change can have LOW severity if executed correctly.
