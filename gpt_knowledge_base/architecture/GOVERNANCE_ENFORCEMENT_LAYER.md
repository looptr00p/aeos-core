# Governance Enforcement Layer — Complete Design

**Date**: 2026-05-19
**Reference**: OBJ-007, ADR-002
**Status**: PROPOSED

---

## Summary

This document defines the first Governance Enforcement Layer for AEOS Core. It transforms governance from declarative (documented rules) to operationally enforceable (validated, tracked, auditable) through three mechanisms:

1. **Extended lint checks** — 10 new deterministic checks in `scripts/aeos_lint.py`
2. **Approval record artifacts** — APR-XXX files in `memory/approvals/`
3. **Lifecycle transition logging** — Embedded in task files

All enforcement is file-based, deterministic, locally executable, repository-driven, and human-governed. No autonomous systems, runtime orchestration, databases, or hidden state are introduced.

---

## Current Governance Gaps

| Gap | Impact | Severity |
|-----|--------|----------|
| No approval records | Human approval is undocumented and unauditable | HIGH |
| No ADR enforcement | Governance changes can occur without documented decisions | HIGH |
| No CI governance validation | Governance violations are not detected on push/PR | HIGH |
| No lifecycle transition tracking | State changes are not recorded or validated | MEDIUM |
| No orphan artifact detection | Broken references go undetected | MEDIUM |
| No stale objective detection | Inactive objectives degrade governance continuity | MEDIUM |
| No escalation aging | Open escalations persist indefinitely | MEDIUM |
| No version enforcement | Inconsistent versions create identity ambiguity | MEDIUM |
| No broken reference detection | Path errors degrade documentation integrity | LOW |
| No invalid phase transition detection | Phase changes without approval go undetected | MEDIUM |

---

## Proposed Enforcement Architecture

### Three-Layer Model

```
Layer 1: Detection (lint checks)
  └── File-based, deterministic, locally executable
  └── 10 new checks added to aeos_lint.py
  └── Results: PASS / FAIL / WARN

Layer 2: Recording (approval artifacts)
  └── APR-XXX files in memory/approvals/
  └── Manual creation by human or agent documenting human approval
  └── Template-based, auditable, git-versioned

Layer 3: Tracking (lifecycle transitions)
  └── Embedded table in task files
  └── Manual entry at each state change
  └── Validated by lint checks
```

### Enforcement Flow

```
Change proposed
  → Review conducted (REV-XXX)
  → Human approval obtained
  → Approval recorded (APR-XXX)
  → Change applied
  → CI runs lint checks (detection layer)
  → Lint results: PASS → merge / FAIL → block or escalate
  → Lifecycle transition logged (in task file)
  → Audit conducted (AUD-XXX)
  → Handoff produced (HND-XXX)
```

---

## Required Artifacts

### Created

| Artifact | Location | Purpose |
|----------|----------|---------|
| OBJ-007.md | `memory/objectives/` | Governance enforcement objective |
| ADR-002.md | `memory/decisions/` | Deterministic governance enforcement decision |
| approval_record_template.md | `templates/` | Template for approval records |
| APR-001.md | `memory/approvals/` | Example approval record for ADR-001 |
| memory/approvals/.gitkeep | `memory/approvals/` | Directory marker |

### To Be Created

| Artifact | Location | Purpose |
|----------|----------|---------|
| TASK-021 to TASK-030 | `memory/tasks/` | Enforcement implementation tasks |
| REV-011 | `memory/reviews/` | Review of enforcement layer |
| AUD-004 | `memory/audits/` | Audit of enforcement layer |
| HND-008 | `memory/handoffs/` | Handoff for enforcement layer |

---

## Proposed Validation Checks

### 10 New Lint Checks

| # | Check Name | Description | Severity | Method |
|---|-----------|-------------|----------|--------|
| 12 | Approval Record Presence | For each governance/protocol/CI/permission change, verify an APR-XXX exists that references the change | HIGH | Scan `memory/approvals/` for APR files referencing modified files |
| 13 | ADR Compliance | For each governance/protocol/CI/permission/architecture change, verify an ADR-XXX exists | HIGH | Scan `memory/decisions/` for ADR files referencing modified files |
| 14 | Lifecycle Transition Validity | For each task, verify state transitions follow valid paths (DRAFT→ASSIGNED→IN_PROGRESS→REVIEW→COMPLETE→CLOSED) | MEDIUM | Parse lifecycle transition tables in task files |
| 15 | Orphan Artifact Detection | Detect artifacts that reference non-existent IDs | MEDIUM | Cross-reference all traceability IDs against existing files |
| 16 | Stale Objective Detection | Detect ACTIVE objectives with no IN_PROGRESS tasks for >14 days | MEDIUM | Compare objective status dates with task status dates |
| 17 | Unresolved Escalation Detection | Detect OPEN/IN_REVIEW escalations older than 14 days | HIGH | Parse ESC-XXX files for status and date |
| 18 | Broken Governance Reference Detection | Detect references to governance files that do not exist | MEDIUM | Scan all .md files for governance/ paths and verify existence |
| 19 | Invalid Phase Transition Detection | Detect phase changes without corresponding ADR and human approval | HIGH | Check PHASE_POLICY.md references against ADRs and APRs |
| 20 | Missing Human Approval Detection | For changes requiring human approval, verify APR-XXX exists | HIGH | Cross-reference REVIEW_REQUIREMENTS.md against APR files |
| 21 | Version Consistency Check | Verify version is consistent across README.md, pyproject.toml, and ESTADO_DEL_ARTE.md | MEDIUM | Extract version from each file and compare |

### Check Implementation Approach

All checks are implemented as Python functions in `scripts/aeos_lint.py`. Each check:

1. Reads repository files (no external dependencies)
2. Applies deterministic logic (no probabilistic reasoning)
3. Returns PASS, FAIL, or WARN with specific details
4. Is independently testable

### Check Output Format

```
[12] Approval Record Presence
  PASS: 3 governance changes have approval records
  FAIL: 1 governance change missing approval record: ADR-001

[13] ADR Compliance
  PASS: 5 architecture changes have ADRs
  FAIL: 0 architecture changes missing ADRs

[14] Lifecycle Transition Validity
  PASS: 11 tasks have valid transition sequences
  WARN: 5 tasks missing transition log entries

...
```

---

## CI Enforcement Strategy

### Current CI Workflow

```yaml
- name: Run pytest
  run: pytest aeos-core/tests

- name: Run AEOS lint
  run: python aeos-core/scripts/aeos_lint.py
```

### Proposed CI Workflow

```yaml
jobs:
  # Job 1: Canonical test suite
  test-canonical:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install pytest pyyaml
      - run: pytest tests/ -v

  # Job 2: Experimental lab tests
  test-experimental:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install pytest pyyaml
      - run: pytest aeos-core/tests/ -v

  # Job 3: Governance enforcement (lint)
  governance-enforcement:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: python -m pip install pyyaml
      - name: Run AEOS governance enforcement
        run: python scripts/aeos_lint.py
      - name: Governance enforcement summary
        if: always()
        run: |
          echo "Governance enforcement checks completed."
          echo "Review lint output for PASS/FAIL/WARN results."
```

### Enforcement Behavior

- **PASS**: All checks pass. CI proceeds normally.
- **FAIL with HIGH severity**: CI fails. Change cannot merge without resolution or human override.
- **FAIL with MEDIUM severity**: CI warns. Change can merge but warning is logged.
- **WARN**: Informational. No CI impact.

### GitHub Environment Protection (Complementary)

For governance file changes (`governance/*.md`), configure GitHub environment protection:

```yaml
environment: governance-approval
```

This requires human review in GitHub UI before changes to governance files merge. This is complementary to, not a replacement for, repository-level enforcement.

---

## Human Governance Preservation

### What Enforcement Does NOT Do

| Action | Why Not |
|--------|---------|
| Auto-approve changes | Violates human authority principle |
| Auto-create approval records | Approval must be explicit human decision |
| Auto-transition lifecycle states | Transitions require human/agent judgment |
| Auto-resolve escalations | Escalation resolution requires human decision |
| Auto-enforce phase transitions | Phase changes require human approval |
| Make governance decisions | Enforcement detects, it does not decide |

### What Enforcement Does

| Action | How |
|--------|-----|
| Detect missing approval records | Scan for APR-XXX files referencing changes |
| Detect missing ADRs | Scan for ADR-XXX files referencing changes |
| Detect invalid lifecycle transitions | Parse transition tables and validate sequences |
| Detect orphan artifacts | Cross-reference all IDs against existing files |
| Detect stale objectives | Compare objective dates with task activity |
| Detect unresolved escalations | Parse ESC-XXX status and dates |
| Detect broken references | Verify referenced files exist |
| Detect version inconsistencies | Compare version across artifacts |
| Report findings | Output PASS/FAIL/WARN with details |

### Human Authority Preserved

- Enforcement checks **inform** human decisions; they do not **make** decisions.
- Approval records **document** human decisions; they do not **replace** them.
- Lifecycle transitions **record** state changes; they do not **trigger** them.
- CI **reports** governance compliance; it does not **enforce** it autonomously.

---

## Risks

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Lint checks produce false positives | LOW | Medium | Test against known-good state; refine checks iteratively |
| Approval records become bureaucratic overhead | LOW | Low | Records are lightweight (5 fields); not a bottleneck |
| CI enforcement blocks legitimate changes | LOW | Low | HIGH-severity failures block; MEDIUM-severity warn only |
| Enforcement checks cannot verify human authenticity | MEDIUM | High | Checks verify record existence, not authenticity. Authenticity is a social trust issue. |
| Lint complexity grows unmanageable | LOW | Low | Cap at 15 checks; consolidate existing checks to make room |
| Lifecycle transition logging is incomplete | LOW | Medium | Missing transitions are detectable; gaps are flagged |
| Approval records are created without genuine human approval | MEDIUM | Low | Social trust issue, not technical. Audit trail exists for review. |

---

## Operational Tradeoffs

| Tradeoff | Decision | Rationale |
|----------|----------|-----------|
| Detection vs. prevention | Detection | Prevention requires runtime; detection is sufficient for auditability |
| Manual vs. automated approval records | Manual | Automated records create hidden state; manual records are explicit |
| Lint vs. governance engine | Lint | Engine introduces runtime complexity; lint is file-based |
| Comprehensive vs. minimal checks | Minimal (10 new) | Comprehensive checks increase maintenance; minimal checks address highest-impact gaps |
| Blocking vs. informational CI | Mixed (HIGH blocks, MEDIUM warns) | Blocking all failures would be too restrictive; HIGH-severity failures must block |
| Platform vs. repository enforcement | Repository | Platform enforcement ties AEOS to GitHub; repository enforcement is platform-independent |

---

## Roadmap

### Phase 1: Foundation (Week 1)

| Task | Deliverable | Effort |
|------|-------------|--------|
| Create approval record template | `templates/approval_record_template.md` | 30 min |
| Create `memory/approvals/` directory | Directory + .gitkeep | 5 min |
| Create APR-001 example | `memory/approvals/APR-001.md` | 30 min |
| Create ADR-002 | `memory/decisions/ADR-002.md` | 1 hour |
| Create OBJ-007 | `memory/objectives/OBJ-007.md` | 30 min |

**Exit Criteria**: All foundation artifacts created and validated.

### Phase 2: Lint Extension (Week 2)

| Task | Deliverable | Effort |
|------|-------------|--------|
| Implement check 12: Approval Record Presence | Extended lint | 2 hours |
| Implement check 13: ADR Compliance | Extended lint | 2 hours |
| Implement check 14: Lifecycle Transition Validity | Extended lint + task template update | 2 hours |
| Implement check 15: Orphan Artifact Detection | Extended lint | 2 hours |
| Implement check 16: Stale Objective Detection | Extended lint | 1 hour |
| Test all new checks | Validation against current repo | 1 hour |

**Exit Criteria**: All 10 new lint checks implemented and passing on current repository state.

### Phase 3: CI Integration (Week 3)

| Task | Deliverable | Effort |
|------|-------------|--------|
| Implement checks 17-21 | Extended lint | 4 hours |
| Update CI workflow | `.github/workflows/aeos-validation.yml` | 1 hour |
| Test CI workflow | Push to test branch | 30 min |
| Update task template | `templates/task_template.md` | 30 min |

**Exit Criteria**: CI runs all 21 checks. Workflow is valid. Task template updated.

### Phase 4: Validation and Closure (Week 4)

| Task | Deliverable | Effort |
|------|-------------|--------|
| Governance review | REV-011 | 2 hours |
| Audit | AUD-004 | 2 hours |
| Handoff | HND-008 | 1 hour |
| Update TRACEABILITY_INDEX.md | Index update | 30 min |
| Create approval records for existing changes | APR-002, APR-003, etc. | 2 hours |

**Exit Criteria**: Review, audit, and handoff complete. All existing governance changes have approval records.

---

## Files To Create

| File | Status | Purpose |
|------|--------|---------|
| `memory/objectives/OBJ-007.md` | ✅ Created | Governance enforcement objective |
| `memory/decisions/ADR-002.md` | ✅ Created | Deterministic governance enforcement ADR |
| `templates/approval_record_template.md` | ✅ Created | Approval record template |
| `memory/approvals/.gitkeep` | ✅ Created | Directory marker |
| `memory/approvals/APR-001.md` | ✅ Created | Example approval record |
| `scripts/aeos_lint.py` | Pending | Extended with 10 new checks |
| `.github/workflows/aeos-validation.yml` | Pending | Updated CI workflow |
| `templates/task_template.md` | Pending | Updated with lifecycle transitions |
| `memory/tasks/TASK-021.md` to `TASK-030.md` | Pending | Implementation tasks |

---

## Recommended Next Actions

1. **Human approval of OBJ-007 and ADR-002** — Required before implementation begins.
2. **Implement lint checks 12-16** (Phase 2) — Highest impact enforcement checks.
3. **Create approval records for existing governance changes** — APR-002 for OBJ-006, APR-003 for ADR-001 approval.
4. **Update CI workflow** (Phase 3) — Run both test suites + extended lint.
5. **Update task template** — Add lifecycle transition logging section.
6. **Implement lint checks 17-21** (Phase 3) — Complete enforcement coverage.
7. **Conduct review, audit, and handoff** (Phase 4) — Close OBJ-007 lifecycle.
