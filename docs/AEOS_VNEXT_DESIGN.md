# AEOS MVP vNext — Scalable Design

**Date**: 2026-05-19
**Basis**: Repository truth reconciliation audit, governance review, deterministic validation review
**Principle**: Scale governance clarity, not complexity
**Operational State**: PROPOSED

---

## Current State

### What Works

- **Governance framework is comprehensive**: 7 governance files, 7 protocols, 11 templates, 6 workflows, 7 agents — all present and internally consistent.
- **Traceability system is functional**: 47 lifecycle IDs, all cross-references resolve, no orphaned artifacts.
- **Lint validation is operational**: 11 checks pass, covering file existence, memory directories, agent registry, traceability, workflow closure, severity labels, and lifecycle continuity.
- **Experimental lab is isolated**: `aeos-core/` subproject provides controlled testing ground with porting governance.
- **Tiering and minimization guidance exist**: Workflow tiering (LOW/MEDIUM/HIGH) and review minimization reduce overhead for low-risk changes.
- **Memory model is explicit**: All institutional memory is markdown, git-versioned, and human-readable.

### What Is Broken

- **CI validates 3 tests, misses 11**: The root governance validation suite is not executed on push/PR.
- **Version is inconsistent**: README says v0.3, pyproject.toml says 0.1.0.
- **No human approval records**: Governance requires human approval but produces no approval artifacts.
- **No ADR enforcement**: ADR protocol exists but no automated check validates compliance.
- **Phase designation is ambiguous**: Claims Phase 0 but active objectives describe Phase 1+ activity.
- **Documentation contains errors**: Incorrect tree diagrams, stale metrics, wrong directory mappings (partially fixed).
- **26 broken path references**: aeos-core artifacts reference root-level paths for files that exist under `aeos-core/` (4 fixed).

### Bottleneck Summary

| Bottleneck | Impact | Root Cause |
|-----------|--------|------------|
| CI gap | Governance changes bypass automated detection | Workflow runs wrong test path |
| No approval records | Human governance is undocumented | Missing approval artifact type |
| No ADR enforcement | Protocol exists without enforcement | Missing lint/test check |
| Phase ambiguity | Governance boundaries unclear | Objective scope exceeds phase definition |
| Path reference errors | Documentation integrity degraded | Dual directory structure not documented |

---

## Core Bottlenecks

### B-001: CI Does Not Validate Canonical Governance

**Current**: CI runs `pytest aeos-core/tests` (3 tests). Root `tests/` (11 tests) is skipped.

**Impact**: An agent or contributor could delete `governance/AGENTS.md`, `governance/SAFETY_RULES.md`, or any protocol file without CI detection. The governance validation suite exists but is not enforced.

**Fix Complexity**: Low — single CI workflow change.

### B-002: Human Governance Has No Audit Trail

**Current**: Governance documents require human approval. No artifact records that approval occurred.

**Impact**: There is no way to audit whether a change was human-approved. The governance model is aspirational — the rules exist but compliance cannot be verified.

**Fix Complexity**: Low — new artifact type (APPROVAL-XXX) and template.

### B-003: ADR Protocol Is Not Enforced

**Current**: ADR_PROTOCOL.md requires ADRs for governance, architecture, CI, permission, and protocol changes. No test validates this.

**Impact**: An agent could modify `governance/PERMISSION_MODEL.md` without creating an ADR, and no automated check would detect it.

**Fix Complexity**: Low — extend aeos_lint.py with git-diff-based ADR compliance check.

### B-004: Dual Directory Structure Is Undocumented

**Current**: Root directories contain canonical artifacts. `aeos-core/` contains experimental artifacts. References use inconsistent path conventions.

**Impact**: 22 broken path references remain. Contributors cannot determine which path convention to use.

**Fix Complexity**: Medium — requires path convention standardization and documentation (ADR-001 addresses this).

### B-005: Phase 0 Exit Criteria Cannot Be Verified

**Current**: Phase 0 exit requires "tests passing." pytest is not installed. Test execution cannot be verified.

**Impact**: Phase transition is blocked by an unverifiable criterion.

**Fix Complexity**: Low — install pytest in CI (already in workflow), document that local verification requires `pip install pytest pyyaml`.

---

## Scaling Risks

### R-001: Reviewer Contention Under Concurrency

**Risk**: 2 ACTIVE objectives (OBJ-004, OBJ-005) with 5 IN_PROGRESS tasks compete for shared reviewer pool (reviewer-agent, auditor-agent). INC-002 (reviewer contention) and ESC-003 (cross-objective governance overload) are active.

**Scaling Impact**: Adding more objectives will increase reviewer contention linearly. Without mitigation, review latency will grow faster than task completion rate.

**Mitigation**: Implement review scheduling (first-come-first-served with objective priority). Consider adding a second reviewer role for MEDIUM-tier changes.

### R-002: Governance Pressure Accumulation

**Risk**: ESC-002 (IN_REVIEW) and ESC-003 (OPEN) are unresolved. Recovery capacity grows slower than pressure accumulation. 5 IN_PROGRESS tasks across 2 objectives.

**Scaling Impact**: As objectives multiply, unresolved escalations accumulate. Each unresolved escalation degrades governance continuity for all concurrent objectives.

**Mitigation**: Implement escalation aging — escalations older than 2 review cycles auto-escalate to human with governance degradation warning.

### R-003: Memory Index Growth

**Risk**: TRACEABILITY_INDEX.md is 299 lines and manually maintained. At 61 artifacts, it is already complex. At 200+ artifacts, it will become unwieldy.

**Scaling Impact**: Manual index maintenance becomes a bottleneck. Errors (like the 60 vs 61 count) become more likely.

**Mitigation**: Split index by objective. Each objective gets its own index file (`memory/index/IDX-OBJ-001.md`, etc.). A master index (`memory/index/MASTER_INDEX.md`) lists objectives and their index files.

### R-004: Template Proliferation

**Risk**: 13 templates exist. As new artifact types are introduced (approval records, scheduling records, split indexes), template count grows.

**Scaling Impact**: Template proliferation increases cognitive load. Contributors must choose from many templates.

**Mitigation**: Consolidate related templates. Create a template selection guide. Cap template count at 15 through consolidation.

### R-005: CI Execution Time

**Risk**: Currently CI runs 3 tests + lint. Adding 11 root tests will increase execution time. As test count grows, CI becomes slower.

**Scaling Impact**: Slow CI reduces feedback velocity. Contributors wait longer for validation results.

**Mitigation**: Parallelize test execution in CI. Separate fast tests (file existence) from slow tests (lint execution, subprocess calls).

---

## Recommended Architecture

### Principle: Composable, Not Autonomous

AEOS scales by adding composable validation layers, not autonomous agents. Each layer is:
- Explicitly defined
- Independently testable
- Human-reviewable
- Markdown-documented

### Structural Changes

#### 1. Single Source of Truth for Paths

**Problem**: aeos-core artifacts reference root paths for files under `aeos-core/`.

**Solution**: Establish a path convention:
- Root-level references use root-relative paths (e.g., `governance/AGENTS.md`).
- aeos-core references use `aeos-core/`-prefixed paths (e.g., `aeos-core/governance/PORTING_POLICY.md`).
- The aeos-core lint script's `_resolve_artifact_path()` fallback is a safety net, not the primary convention.

**Action**: Fix remaining 22 broken references. Document convention in README.md.

#### 2. Split Traceability Index

**Problem**: Single 299-line index file is hard to maintain and error-prone.

**Solution**: Split by objective:
```
memory/index/
├── MASTER_INDEX.md          # Lists all objectives, their status, and index file
├── IDX-OBJ-001.md           # Objective-specific index
├── IDX-OBJ-002.md
├── IDX-OBJ-003.md
├── IDX-OBJ-004.md
├── IDX-OBJ-005.md
├── IDX-OBJ-006.md
└── README.md                # Index structure documentation
```

Each objective index contains only the artifacts for that objective. The master index provides a summary view.

**Action**: Create split index structure. Migrate existing TRACEABILITY_INDEX.md content into objective-specific files.

#### 3. Approval Record Artifact Type

**Problem**: No record of human approval exists.

**Solution**: New artifact type `APPROVAL-XXX`:
```
memory/approvals/
├── APPROVAL-001.md  # Approval for ADR-001
├── APPROVAL-002.md  # Approval for OBJ-006
└── ...
```

Template includes: approved artifact ID, approver identity, date, conditions, and scope of approval.

**Action**: Create approval template. Require approval records for all human-approved changes.

#### 4. Version Alignment

**Problem**: Three artifacts, two versions.

**Solution**: Single source of truth for version: `pyproject.toml`. All other artifacts reference it or derive from it.

**Action**: Human decides canonical version. Update README.md and ESTADO_DEL_ARTE.md to match. Add version reference in README: "Version: see pyproject.toml."

---

## Recommended Workflow Improvements

### W-001: Enforce Tiered Workflows

**Current**: Workflow tiering guidance exists but is not enforced. All workflows go through the same stages regardless of tier.

**Recommendation**: Add tier field to task template. aeos_lint.py validates that LOW-tier tasks skip unnecessary stages (ADR, architecture review).

**Impact**: Reduces overhead for documentation-only changes by ~50% (4-6 stages vs 10-12).

### W-002: Audit Scheduling for IN_PROGRESS Tasks

**Current**: 5 tasks are IN_PROGRESS with no audit artifacts scheduled.

**Recommendation**: Add audit scheduling field to task template. When a task moves to IN_PROGRESS, it must reference a planned AUD-XXX (even if the audit file doesn't exist yet).

**Impact**: Prevents audit deferral. Ensures every task has an audit path before closure.

### W-003: Workflow Stage Transition Records

**Current**: No record of when tasks moved between lifecycle stages.

**Recommendation**: Add a lightweight transition log to each task file:
```
## Lifecycle Transitions
| From | To | Date | Agent |
|------|----|------|-------|
| DRAFT | IN_PROGRESS | 2026-05-18 | implementer-agent |
```

**Impact**: Enables audit trail reconstruction. No new artifact type needed — embedded in existing task files.

### W-004: Consolidate Review Types for MEDIUM-Tier

**Current**: 6 review types defined. MEDIUM-tier tasks may not need all 6.

**Recommendation**: Per REVIEW_MINIMIZATION_GUIDANCE.md, MEDIUM-tier tasks use 2-3 review types:
- Scope review (always)
- Implementation review (always)
- Governance review (only if governance-adjacent)

Skip: architecture review, validation review, handoff review (combined with implementation).

**Impact**: Reduces review overhead for MEDIUM-tier tasks by ~50%.

---

## Recommended Governance Improvements

### G-001: ADR Enforcement in Lint

**Current**: ADR protocol exists without enforcement.

**Recommendation**: Add to aeos_lint.py:
```
Check: For each modified governance/protocol/CI/permission file,
       verify an ADR-XXX exists that references the change.
Method: Git diff + ADR reference scan.
Severity: HIGH if missing.
```

**Impact**: Prevents governance changes without documented decisions.

### G-002: Approval Record Requirement

**Current**: Human approval is required but not recorded.

**Recommendation**: Add to REVIEW_REQUIREMENTS.md:
```
All human approvals MUST produce an APPROVAL-XXX artifact.
Approval artifacts MUST reference the approved change and scope.
Approval artifacts MUST be stored in memory/approvals/.
```

**Impact**: Creates auditable human governance trail.

### G-003: Phase Designation Resolution

**Current**: Phase 0 claimed but objectives exceed Phase 0 scope.

**Recommendation**: Human decision — one of:
- **Option A**: Advance to Phase 1. Update PHASE_POLICY.md entry criteria. Document justification.
- **Option B**: Narrow OBJ-004 and OBJ-005 scope to Phase 0 boundaries. Move超出-scope items to future objectives.
- **Option C**: Create Phase 0.5 (Governance Validation) as intermediate phase.

**Impact**: Resolves governance boundary ambiguity.

### G-004: Escalation Aging Policy

**Current**: Escalations persist indefinitely without aging mechanism.

**Recommendation**: Add to ESCALATION_POLICY.md:
```
Escalations older than 2 review cycles (14 days) MUST:
1. Auto-escalate to human with governance degradation warning.
2. Document the aging in the escalation artifact.
3. Trigger a governance health report update.
```

**Impact**: Prevents escalation accumulation from degrading governance continuity.

### G-005: Agent Naming Convention Documentation

**Current**: Agent YAML files use snake_case filenames but kebab-case agent IDs. Not documented.

**Recommendation**: Add to AGENTS.md:
```
Agent YAML files MUST follow naming convention:
- Directory: agents/{agent-name}/ (kebab-case, no "-agent" suffix)
- File: {agent-name}/agent.yaml (e.g., director/agent.yaml)
- agent_id field: {agent-name}-agent (kebab-case, with "-agent" suffix)
```

**Impact**: Eliminates naming ambiguity. Simplifies agent discovery.

---

## CI/CD Recommendations

### CI-001: Run Complete Test Suite

**Current**: `pytest aeos-core/tests` only.

**Recommended**:
```yaml
- name: Run canonical tests
  run: pytest tests/ -v

- name: Run experimental lab tests
  run: pytest aeos-core/tests/ -v
```

**Impact**: All 14 tests execute on every push/PR. Governance validation is enforced.

### CI-002: Run Root Lint Script Directly

**Current**: `python aeos-core/scripts/aeos_lint.py` (wrapper).

**Recommended**:
```yaml
- name: Run AEOS lint
  run: python scripts/aeos_lint.py
```

**Impact**: Removes unnecessary dependency on aeos-core wrapper. Uses canonical lint directly.

### CI-003: Add Manual Approval Gate for Governance Changes

**Current**: No manual approval gate.

**Recommended** (for governance file changes):
```yaml
- name: Require human approval for governance changes
  if: contains(github.event.head_commit.modified, 'governance/')
  runs-on: ubuntu-latest
  environment: governance-approval
```

**Impact**: GitHub environment protection requires human review before governance changes merge.

### CI-004: Parallelize Test Execution

**Current**: Sequential test execution.

**Recommended**:
```yaml
jobs:
  test-canonical:
    runs-on: ubuntu-latest
    steps:
      - run: pytest tests/ -v

  test-experimental:
    runs-on: ubuntu-latest
    steps:
      - run: pytest aeos-core/tests/ -v

  lint:
    runs-on: ubuntu-latest
    steps:
      - run: python scripts/aeos_lint.py
```

**Impact**: Reduces CI execution time by ~40% (parallel jobs).

### CI-005: Python Version Alignment

**Current**: CI uses Python 3.11. pyproject.toml requires >=3.10.

**Recommended**: Align CI to Python 3.11 (current LTS-compatible). Document in pyproject.toml comment:
```toml
# CI runs Python 3.11. Local development: >=3.10.
requires-python = ">=3.10"
```

**Impact**: Eliminates version ambiguity.

---

## Memory Strategy

### M-001: Split Traceability Index

As described in architecture section. Each objective gets its own index file. Master index provides summary.

### M-002: Add Approval Records

New `memory/approvals/` directory with APPROVAL-XXX artifacts. Template includes:
- Approved artifact ID
- Approver identity
- Date
- Conditions
- Scope

### M-003: Resolve memory/research/ Naming

**Option A (recommended)**: Rename to `memory/reports/`. Update all references. Requires ADR.
**Option B**: Update memory/index/README.md to document that `memory/research/` also holds operational reports.

**Recommendation**: Option B for vNext (lower risk). Option A for vNext+1 (if structural cleanup is prioritized).

### M-004: Lifecycle Transition Logging

Embed transition logs in task files. No new directory or artifact type needed.

### M-005: Memory Growth Monitoring

Add to aeos_lint.py:
```
Check: Count artifacts per category.
Warn if: Any category exceeds 50 artifacts without split index.
```

**Impact**: Proactive detection of index growth issues.

---

## Human Oversight Strategy

### H-001: Approval Records for All Critical Changes

Every governance, protocol, CI, permission, and workflow change requires an APPROVAL-XXX artifact before merge.

### H-002: GitHub Environment Protection

Configure GitHub repository environments:
- `governance-approval`: Required for changes to `governance/`, `protocols/`, `workflows/`.
- `ci-approval`: Required for changes to `.github/workflows/`, `pyproject.toml`.

### H-003: Periodic Governance Health Review

Per REVIEW_CADENCE.md, conduct weekly governance health reviews. Automated trigger: if ESC or INC count exceeds threshold, generate governance health report.

### H-004: Phase Transition Gate

Phase transitions require:
1. Documented justification (ADR).
2. Audit review (AUD-XXX).
3. Human approval (APPROVAL-XXX).
4. All exit criteria verified.

### H-005: No Autonomous Phase Transitions

Reinforce in AGENTS.md: "No agent may initiate, propose, or execute a phase transition without explicit human approval."

---

## MVP vNext Definition

### Scope

AEOS MVP vNext addresses the 5 core bottlenecks identified in the reconciliation audit while preserving all governance invariants. It adds 3 new artifact types (approval records, split indexes, transition logs) and 5 lint checks. It does NOT add autonomous agents, orchestration, or runtime complexity.

### What Changes

| Area | Change | Complexity |
|------|--------|------------|
| CI | Run complete test suite + parallelize | Low |
| CI | Run root lint directly | Low |
| CI | Add manual approval gate for governance changes | Low |
| Artifacts | Approval records (APPROVAL-XXX) | Low |
| Artifacts | Split traceability index | Medium |
| Artifacts | Lifecycle transition logs in tasks | Low |
| Lint | ADR enforcement check | Low |
| Lint | Memory growth monitoring | Low |
| Lint | Approval record verification | Low |
| Governance | Escalation aging policy | Low |
| Governance | Agent naming convention documentation | Low |
| Governance | Phase designation resolution | Medium (human decision) |
| Documentation | Fix remaining broken path references | Low |
| Documentation | Version alignment | Low (human decision) |
| Documentation | memory/research/ naming documentation | Low |

### What Does NOT Change

- No new agents.
- No autonomous execution.
- No orchestration runtime.
- No hidden state.
- No database or vector store.
- No API or networking layers.
- No workflow execution engine.
- No self-modifying governance.
- No distributed systems.

### New Artifact Types

| Type | Prefix | Directory | Template | Purpose |
|------|--------|-----------|----------|---------|
| Approval Record | APPROVAL-XXX | `memory/approvals/` | `templates/approval_template.md` | Document human approval |
| Objective Index | IDX-OBJ-XXX | `memory/index/` | `templates/objective_index_template.md` | Per-objective traceability |
| Master Index | MASTER_INDEX | `memory/index/` | N/A | Summary of all objectives |

### New Lint Checks

| Check | Description | Severity |
|-------|-------------|----------|
| ADR compliance | Verify governance changes have ADRs | HIGH |
| Approval records | Verify human-approved changes have APPROVAL-XXX | HIGH |
| Memory growth | Warn if category exceeds 50 artifacts | LOW |
| Path convention | Verify aeos-core references use aeos-core/ prefix | MEDIUM |
| Version consistency | Verify version matches pyproject.toml | MEDIUM |

### Success Criteria for vNext

1. CI runs all 14 tests on every push/PR.
2. All governance changes have ADR and APPROVAL artifacts.
3. TRACEABILITY_INDEX.md is split by objective.
4. All 22 broken path references are fixed.
5. Version is consistent across all artifacts.
6. Phase designation is resolved.
7. Escalation aging policy is documented.
8. aeos_lint.py has 16 checks (11 existing + 5 new).
9. All existing tests pass.
10. No governance invariants are weakened.

---

## Phased Roadmap

### Phase vNext-0: Foundation (Week 1)

**Objective**: Fix critical gaps without structural changes.

| Task | Deliverable | Effort |
|------|-------------|--------|
| Fix CI to run root tests | Updated `.github/workflows/aeos-validation.yml` | 1 hour |
| Fix CI to run root lint | Updated workflow | 30 min |
| Fix remaining broken path references | 22 file edits | 2 hours |
| Align version | Human decision + 2 file edits | 1 hour |
| Add ADR enforcement to lint | Extended `scripts/aeos_lint.py` | 2 hours |
| Add approval record template | `templates/approval_template.md` | 1 hour |

**Exit Criteria**: CI runs 14 tests + lint. All path references resolve. Version is consistent.

### Phase vNext-1: Governance Hardening (Week 2)

**Objective**: Strengthen human governance and escalation management.

| Task | Deliverable | Effort |
|------|-------------|--------|
| Create approval records for ADR-001, OBJ-006 | `memory/approvals/APPROVAL-001.md`, `APPROVAL-002.md` | 1 hour |
| Add approval record lint check | Extended lint | 1 hour |
| Document escalation aging policy | Updated `governance/ESCALATION_POLICY.md` | 1 hour |
| Document agent naming convention | Updated `governance/AGENTS.md` | 30 min |
| Resolve phase designation | Human decision + documentation update | 2 hours |
| Add memory growth monitoring to lint | Extended lint | 1 hour |

**Exit Criteria**: All governance changes have approval records. Escalation aging is documented. Phase is resolved.

### Phase vNext-2: Memory Restructuring (Week 3)

**Objective**: Split traceability index and improve memory organization.

| Task | Deliverable | Effort |
|------|-------------|--------|
| Create split index structure | 6 objective index files + master index | 3 hours |
| Create objective index template | `templates/objective_index_template.md` | 1 hour |
| Migrate TRACEABILITY_INDEX.md content | Split into objective files | 2 hours |
| Update lint for split index | Extended lint | 1 hour |
| Document memory/research/ naming | Updated `memory/index/README.md` | 30 min |

**Exit Criteria**: Split index is operational. Master index provides summary view. Lint validates split index.

### Phase vNext-3: Workflow Optimization (Week 4)

**Objective**: Reduce overhead for low-risk changes.

| Task | Deliverable | Effort |
|------|-------------|--------|
| Add tier field to task template | Updated `templates/task_template.md` | 30 min |
| Add tier validation to lint | Extended lint | 1 hour |
| Add audit scheduling to task template | Updated template | 30 min |
| Add lifecycle transition logging to tasks | Updated template + existing tasks | 2 hours |
| Add CI parallelization | Updated workflow | 1 hour |
| Add GitHub environment protection | Repository settings | 1 hour |

**Exit Criteria**: Tiered workflows are enforced. Audit scheduling is mandatory. CI is parallelized.

### Phase vNext-4: Validation and Closure (Week 5)

**Objective**: Verify all changes and close vNext cycle.

| Task | Deliverable | Effort |
|------|-------------|--------|
| Run full test suite | All 14 tests pass | 30 min |
| Run full lint suite | All 16 checks pass | 30 min |
| Governance review | REV-XXX for vNext changes | 2 hours |
| Audit | AUD-XXX for vNext cycle | 2 hours |
| Handoff | HND-XXX for vNext completion | 1 hour |
| Update TRACEABILITY_INDEX master | Master index reflects vNext state | 1 hour |

**Exit Criteria**: All tests pass. All lint checks pass. Review and audit complete. Handoff produced.

---

## Risk Assessment for vNext

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Split index migration introduces errors | MEDIUM | Low | Validate each objective index against existing TRACEABILITY_INDEX.md |
| ADR enforcement check produces false positives | LOW | Medium | Test against known governance changes before deployment |
| CI parallelization introduces race conditions | LOW | Low | Jobs are independent (different test directories) |
| Phase designation decision is contentious | MEDIUM | Medium | Present options with evidence; human decides |
| Approval record requirement slows workflow | LOW | Medium | Approval records are lightweight (5 fields); not a bottleneck |
| Version alignment requires discarding v0.3 claims | LOW | Low | Version is a label; governance substance doesn't change |

---

## What vNext Explicitly Rejects

| Rejected | Reason |
|----------|--------|
| Autonomous agents | Violates human-in-the-loop principle |
| Workflow execution engine | Violates explicit non-goals |
| Database or vector store | Violates repo-driven principle |
| Runtime orchestration | Violates explicit non-goals |
| Self-modifying governance | Violates safety rules |
| Distributed systems | Violates explicit non-goals |
| Plugin system | Adds complexity without governance benefit |
| Automated approval | Violates human authority principle |
| Embedded memory in agents | Violates explicit memory model |
| AI-assisted review | Review outcomes require human/agent judgment, never automated |

---

## Summary

AEOS MVP vNext scales by **fixing what is broken** and **adding minimal enforcement**, not by adding complexity. The design adds:

- **3 artifact types** (approval records, split indexes, transition logs)
- **5 lint checks** (ADR compliance, approval records, memory growth, path convention, version consistency)
- **1 governance policy** (escalation aging)
- **1 documentation fix** (agent naming convention)
- **1 CI improvement** (complete test suite + parallelization)

Total new complexity: ~200 lines of lint code, 3 templates, 6 index files, 1 policy update. No agents, no runtime, no orchestration, no hidden state.

The result is a governance framework that is **enforced, auditable, and scalable** — without sacrificing the principles that make AEOS effective.
