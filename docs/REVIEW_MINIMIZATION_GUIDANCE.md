# Review Minimization Guidance

## Purpose

Reduce review type proliferation discovered during external operational validation.

This is GUIDANCE ONLY. It does not change review requirements for HIGH/CRITICAL changes. It provides practical guidance for selecting appropriate review types based on change characteristics.

## Governance Invariants (Never Weakened)

- All changes require at least one review type.
- HIGH/CRITICAL changes require full review separation.
- Governance review is mandatory for any governance-adjacent change.
- Handoff review is mandatory for all completed tasks.
- Review outcomes require human or agent judgment — never automated.

## Review Type Selection Matrix

### Scope Review

**When Necessary**: Always required. Verifies changes remain within defined task scope.

**When May Be Combined**: May be combined with implementation review for LOW-tier changes.

**When Mandatory Separately**: HIGH/CRITICAL changes.

---

### Architecture Review

**When Necessary**: When changes affect architecture documentation, agent definitions, or system structure.

**When May Be Skipped**: Pure documentation changes, memory artifact creation, research findings.

**When Mandatory Separately**: Any change that modifies architecture documentation or agent definitions.

---

### Implementation Review

**When Necessary**: Always required for any file creation or modification.

**When May Be Combined**: May be combined with validation review for LOW-tier changes with no code modifications.

**When Mandatory Separately**: HIGH/CRITICAL changes. Any change that modifies implementation code.

---

### Governance Review

**When Necessary**: When changes affect or are adjacent to governance documents, protocols, or workflows.

**When May Be Lightweight**: LOW-tier changes that only create memory artifacts (no governance file modifications).

**When Mandatory Separately**: Any change that modifies governance documents, protocols, or workflows. HIGH/CRITICAL changes.

---

### Validation Review

**When Necessary**: Always required. Verifies tests pass and acceptance criteria are met.

**When May Be Combined**: May be combined with implementation review for LOW-tier changes.

**When Mandatory Separately**: HIGH/CRITICAL changes. Any change that modifies tests or CI configuration.

---

### Handoff Review

**When Necessary**: Always required for all completed tasks.

**When May Be Combined**: May be combined with validation review for LOW-tier changes.

**When Mandatory Separately**: HIGH/CRITICAL changes.

## Consolidation Rules

### LOW-Tier Changes

May consolidate to 2-3 review types:
- Combined scope + implementation review.
- Combined validation + handoff review.
- Lightweight governance review (separate if governance-adjacent).

Minimum: 2 review types.

### MEDIUM-Tier Changes

May consolidate to 3-4 review types:
- Scope review (separate).
- Combined implementation + validation review.
- Governance review (separate).
- Handoff review (may combine with validation).

Minimum: 3 review types.

### HIGH-Tier Changes

No consolidation allowed. All 6 review types conducted separately.

### CRITICAL-Tier Changes

No consolidation allowed. All 6 review types + emergency security review conducted separately.

## Review Fatigue Prevention

- Do not require all 6 review types for documentation-only changes.
- Do not require architecture review for changes that don't affect architecture.
- Do not require governance review for pure memory artifact creation.
- Track review type usage per cycle — if all tasks use all 6 types, guidance is not being followed.

## Decision Flow

1. What is the change tier? (LOW / MEDIUM / HIGH / CRITICAL)
2. What files are affected? (governance / protocols / workflows / implementation / tests / documentation / memory)
3. Based on tier and file types, select review types from matrix above.
4. Document selected review types in TASK-XXX.
5. Conduct selected review types per REVIEW_PROTOCOL.

## Examples

### Example 1: Documentation Update (LOW)

- Files: docs/new_guide.md
- Tier: LOW
- Review types: Combined scope + implementation, combined validation + handoff
- Total: 2 review passes

### Example 2: Workflow Modification (MEDIUM)

- Files: workflows/new_workflow.md
- Tier: MEDIUM
- Review types: Scope (separate), implementation + validation (combined), governance (separate), handoff (combined with validation)
- Total: 3 review passes

### Example 3: Governance Policy Change (HIGH)

- Files: governance/SAFETY_RULES.md
- Tier: HIGH
- Review types: All 6 separately
- Total: 6 review passes

### Example 4: Memory Artifact Creation (LOW)

- Files: memory/tasks/TASK-XXX.md
- Tier: LOW
- Review types: Combined scope + implementation, combined validation + handoff, lightweight governance check
- Total: 2-3 review passes
