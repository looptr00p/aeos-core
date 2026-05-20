# Operational Ergonomics

**Operational State**: EXPERIMENTAL

## Context

This document records operational ergonomics findings from AEOS operational validation cycles 001 and 002. It identifies what should remain manual, what may be mechanically assisted, and what should never be automated.

These findings come from real operational experience, not theoretical design.

## Governance Friction Findings

### What Works Well

- **Explicit governance rules**: Having AGENTS.md, SAFETY_RULES.md, PERMISSION_MODEL.md before any work eliminates ambiguity. This is AEOS's strongest asset.
- **Severity model**: LOW/MEDIUM/HIGH/CRITICAL classification provides clear guidance on response requirements.
- **Escalation lifecycle**: ESC-001 proved the escalation path works — observation was tracked, reviewed, and resolved without governance weakening.
- **Template structure**: Pre-defined templates reduce cognitive load significantly.

### What Creates Friction

- **Workflow stage count**: 12-stage feature workflow creates overhead for simple changes.
- **Review type proliferation**: 6 review types per task is excessive for LOW-tier changes.
- **Manual traceability maintenance**: Updating TRACEABILITY_INDEX.md manually becomes tedious at 15+ artifacts.
- **Cross-referencing**: Verifying references requires opening multiple files.

## Cognitive Overhead Findings

### Low Overhead

- Traceability ID format (OBJ-XXX, TASK-XXX, etc.) is intuitive and consistent.
- Template field names are self-explanatory.
- Governance document structure is predictable.

### Moderate Overhead

- Tracking which review types apply to which task types requires referencing multiple documents.
- Verifying traceability completeness requires opening 2-3 files per artifact.
- Understanding workflow stage requirements requires reading the full workflow document.

### High Overhead

- Manual traceability index maintenance — requires careful attention to ensure all relationships are documented.
- Cross-referencing lifecycle artifacts across multiple memory directories.

## Workflow Ergonomics Findings

### Feature Workflow (12 stages)

**Assessment**: Comprehensive but heavy for simple changes.

**Recommendation**: Use workflow tiering guidance to apply lightweight variant (4-6 stages) for LOW-tier changes.

### Bugfix Workflow (12 stages)

**Assessment**: Appropriate. Severity classification naturally filters complexity.

**Recommendation**: Keep as-is.

### Architecture Change Workflow (13 stages)

**Assessment**: Appropriate. ADR requirement is justified for architecture changes.

**Recommendation**: Keep as-is.

### Audit Workflow (12 stages)

**Assessment**: Well-structured. No excessive overhead.

**Recommendation**: Keep as-is.

### Incident Workflow (12 stages)

**Assessment**: Clear escalation paths. Severity model improves response clarity.

**Recommendation**: Keep as-is.

### Research Workflow (9 stages)

**Assessment**: Lightweight and appropriate.

**Recommendation**: Keep as-is.

## Traceability Usability Findings

### What Works

- ID format is clear and consistent.
- Cross-references between artifacts are explicit.
- Traceability index provides single-view mapping.

### What Needs Improvement

- Manual index maintenance is the primary bottleneck.
- No automated completeness check exists.
- Cross-referencing requires multiple file opens.

## Review Fatigue Findings

### Current State

- 6 review types defined per review template.
- External validation used all 6 types for every task.
- Review latency was < 1 day per review (acceptable).
- Cumulative review time across multiple tasks is noticeable.

### Assessment

Review fatigue is not yet a problem (2 tasks, 2 reviews each). Risk increases if:
- Task count grows to 10+ per cycle.
- All 6 review types continue to be used for every task.

### Mitigation

Apply review minimization guidance:
- LOW-tier: 2-3 review types.
- MEDIUM-tier: 3-4 review types.
- HIGH/CRITICAL: All 6 types (no consolidation).

## What Should Remain Manual

The following must NEVER be automated. This is a critical AEOS governance invariant:

1. **Human approval authority** — humans must retain final decision authority for critical changes.
2. **Governance modification** — governance changes require human judgment about organizational context.
3. **Permission escalation** — permission changes require human understanding of trust and risk.
4. **Review judgment** — review outcomes require human understanding of context and nuance.
5. **Audit judgment** — audit findings require human understanding of governance intent.
6. **Escalation resolution** — escalation outcomes require human understanding of organizational priorities.
7. **Severity classification** — severity assignment requires contextual judgment.
8. **Tier assignment** — task tier assignment requires understanding of change impact.

## What May Be Mechanically Assisted

The following may be assisted by lightweight mechanical tools (scripts, templates, checklists). No decision-making is automated:

1. **Traceability index updates** — script that reads memory/*.md files and updates the index table. Mechanical aggregation only.
2. **Reference validation** — aeos_lint.py already validates reference existence. Extend to validate completeness.
3. **Template field validation** — check that all required template fields are populated.
4. **ID format validation** — verify traceability IDs follow correct prefix format.
5. **Duplicate ID detection** — detect if the same ID is used for multiple artifacts.
6. **Missing artifact detection** — detect if a closed task lacks a handoff, or a task lacks a review.

## What Should Never Be Automated

Reiterating the critical boundary:

- No autonomous governance decisions.
- No automatic approvals.
- No automatic audits.
- No automatic escalation resolution.
- No automatic review outcomes.
- No automatic severity classification.
- No automatic tier assignment.
- No automatic scope expansion.
- No automatic permission changes.

Mechanical assistance is limited to: reading files, checking format, detecting missing references, aggregating data into tables. All judgment remains human.

## Recommended Ergonomics Improvements

| Priority | Improvement | Type | Impact |
|----------|------------|------|--------|
| HIGH | Workflow tiering guidance | Guidance | Reduces overhead for LOW-tier changes |
| HIGH | Review minimization guidance | Guidance | Reduces review fatigue |
| MEDIUM | Traceability assistance template | Template | Reduces manual index maintenance |
| MEDIUM | Lightweight traceability validation in aeos_lint.py | Script | Detects missing references and duplicates |
| LOW | Operational ergonomics documentation | Documentation | Preserves institutional knowledge |

## Summary

AEOS governance structure is operationally sound. The main ergonomics improvements are:

1. Apply workflow tiering to reduce unnecessary process overhead for LOW-tier changes.
2. Apply review minimization to reduce review type proliferation.
3. Provide traceability assistance template to reduce manual index maintenance burden.
4. Add lightweight mechanical validation to aeos_lint.py for missing references and duplicate IDs.

All improvements preserve the human governance boundary. No governance invariants are weakened. No autonomous behavior is introduced.
