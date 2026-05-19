# Gap Analysis — AEOS Core

**Generated**: 2026-05-19
**Method**: Documentation claims vs. actual repository state

---

## Critical Inconsistencies

### GAP-001: README Repository Tree Does Not Match Actual Structure

**Severity**: HIGH
**Affected Files**: `README.md` (lines 47-59)
**Impact**: Misleading onboarding; developers will look for files in wrong locations

**Claim** (README.md):
```
aeos-core/
  governance/       Rules, constraints, and policies
  protocols/        How work is done
  templates/        Reusable artifact templates
  agents/           Agent definitions and registry
  workflows/        End-to-end process definitions
  memory/           Explicit institutional memory
  scripts/          Operational validation (aeos_lint.py)
  tests/            Repository structure validation
  docs/             Operational documentation
```

**Reality**: All these directories exist at the **repository root level**, NOT under `aeos-core/`. The `aeos-core/` subdirectory is a separate experimental lab with its own subset of these directories.

**Resolution**: Update README.md repository tree to show root-level directories. Clarify that `aeos-core/` is a nested experimental subproject, not the canonical structure.

**Governance Impact**: Repository structure documentation is a governance artifact. Misleading structure docs violate the "repo-driven traceability" principle.

---

### GAP-002: ESTADO_DEL_ARTE.md Repository Tree Also Incorrect

**Severity**: HIGH
**Affected Files**: `ESTADO_DEL_ARTE.md` (lines 30-100)

**Claim**: Same incorrect tree as README — shows all directories under `aeos-core/`.

**Reality**: Directories are at root level.

**Resolution**: Same as GAP-001. Additionally, ESTADO_DEL_ARTE.md is in Spanish while README.md is in English — this dual-language inconsistency should be intentional or resolved.

**Governance Impact**: Same as GAP-001.

---

### GAP-003: Reviews Stored in Wrong Directory

**Severity**: MEDIUM
**Affected Files**: `memory/index/README.md` (line 40), actual file placement

**Claim** (memory/index/README.md): Reviews are stored in `memory/audits/` with REV- prefix.

**Reality**: Reviews (REV-001 through REV-009) are stored in `memory/reviews/`, NOT `memory/audits/`. Audits (AUD-001 through AUD-003) are correctly in `memory/audits/`.

**Resolution**: Update `memory/index/README.md` line 40 to show `memory/reviews/` for Reviews.

**Governance Impact**: Traceability index is the canonical artifact relationship map. Incorrect directory mapping breaks the "explicit memory" principle.

---

### GAP-004: Version Inconsistency Across Artifacts

**Severity**: MEDIUM
**Affected Files**: `README.md` (line 1), `ESTADO_DEL_ARTE.md` (line 7), `pyproject.toml` (line 7)

| Artifact | Claimed Version |
|----------|----------------|
| README.md | v0.3 |
| ESTADO_DEL_ARTE.md | v0.1.0 |
| pyproject.toml | 0.1.0 |

**Reality**: README claims v0.3, but pyproject.toml and ESTADO_DEL_ARTE.md both say 0.1.0.

**Resolution**: Align all version references. If the repo is at v0.3, update pyproject.toml and ESTADO_DEL_ARTE.md. If at v0.1.0, update README.md.

**Governance Impact**: Version inconsistency undermines reproducibility and auditability claims.

---

### GAP-005: ESTADO_DEL_ARTE.md Metrics Are Stale

**Severity**: MEDIUM
**Affected Files**: `ESTADO_DEL_ARTE.md` (lines 216-231)

**Claimed Metrics**:
| Metric | Claimed | Actual |
|--------|---------|--------|
| Total files | 52 | ~170+ |
| Governance files | 6 | 7 (+1 in aeos-core) |
| Template files | 7 | 11 (+2 in aeos-core) |
| Operational docs | 3 | 14 |
| Test modules | 5 | 11 (+3 in aeos-core) |
| Memory directories | 8 | 10 |

**Resolution**: Update metrics or mark ESTADO_DEL_ARTE.md as a historical snapshot with date.

**Governance Impact**: Stale metrics in a "state of the art" document misrepresent system capability.

---

### GAP-006: Test Count Claim Does Not Match Reality

**Severity**: LOW
**Affected Files**: `ESTADO_DEL_ARTE.md` (line 226), `README.md` (lines 86-88)

**Claim** (ESTADO_DEL_ARTE.md): "42 passed in 0.15s, 0 failed"

**Reality**: pytest is not installed in the current environment (`python3 -m pytest` fails with "No module named pytest"). The claimed test results cannot be independently verified. The CI workflow references `aeos-core/tests` path but root tests are at `tests/`.

**Resolution**: 
1. Install pytest and run tests to verify actual count
2. Update ESTADO_DEL_ARTE.md with actual test results or remove the specific numbers
3. Fix CI workflow path if needed

**Governance Impact**: Unverifiable test claims undermine the "reproducibility" principle.

---

### GAP-007: CI Workflow Tests aeos-core/tests, Not Root tests/

**Severity**: HIGH
**Affected Files**: `.github/workflows/aeos-validation.yml` (line 23)

**Claim**: CI runs `pytest aeos-core/tests`

**Reality**: The main test suite (11 files) is at `tests/` (root level). `aeos-core/tests/` contains only 3 enforcement tests. The CI workflow will NOT run the main test suite.

**Resolution**: Update CI workflow to run both `tests/` and `aeos-core/tests/`, or consolidate to a single test root.

**Governance Impact**: CI not running the main test suite means governance validation tests are not executed on push/PR.

---

### GAP-008: memory/decisions/ Is Empty (No ADRs Exist)

**Severity**: LOW
**Affected Files**: `memory/decisions/` (only .gitkeep), `memory/index/TRACEABILITY_INDEX.md` (line 25)

**Claim**: The traceability model includes ADR-XXX artifacts in `memory/decisions/`.

**Reality**: `memory/decisions/` contains only `.gitkeep`. No ADR files exist. TRACEABILITY_INDEX.md confirms: "None created during these cycles."

**Resolution**: This is acceptable for Phase 0, but should be explicitly noted in documentation as an expected gap. No action required unless Phase 0 exit criteria require ADRs.

**Governance Impact**: Low — ADRs are only needed when architecture decisions are made.

---

### GAP-009: memory/architecture/ Is Empty

**Severity**: LOW
**Affected Files**: `memory/architecture/` (only .gitkeep)

**Reality**: Directory exists but contains no content.

**Resolution**: Acceptable for Phase 0. No action required.

**Governance Impact**: None.

---

### GAP-010: Duplicate aeos_lint.py Scripts

**Severity**: LOW
**Affected Files**: `scripts/aeos_lint.py`, `aeos-core/scripts/aeos_lint.py`

**Reality**: Two lint scripts exist. The aeos-core version delegates to the root version and adds experimental lab checks.

**Resolution**: This is intentional design (delegation pattern). Document the relationship clearly to avoid confusion.

**Governance Impact**: None if intentional.

---

### GAP-011: TRACEABILITY_INDEX.md Claims 60 Artifacts But Counts Don't Add Up

**Severity**: LOW
**Affected Files**: `memory/index/TRACEABILITY_INDEX.md` (lines 286-295)

**Claim**: Total artifact count = 60

**Reality**: Summing the table columns: 7+12+5+12+12+9+4 = 61, not 60. The "Total" row shows 5 objectives + 11 tasks + 9 reviews + 3 audits + 7 handoffs + 3 incidents + 3 escalations + 12 reports + 4 ergonomics + 4 learnings = 61.

**Resolution**: Fix the total count in TRACEABILITY_INDEX.md.

**Governance Impact**: Minor — affects traceability accuracy.

---

### GAP-012: Documentation Agent Has Typo in YAML

**Severity**: LOW
**Affected Files**: `agents/documentation/documentation_agent.yaml` (line 59)

**Reality**: Line 59 reads "Escalarate" instead of "Escalate".

**Resolution**: Fix typo.

**Governance Impact**: None — cosmetic.

---

### GAP-013: memory/research/ Contains Non-Research Artifacts

**Severity**: MEDIUM
**Affected Files**: `memory/research/` directory, `memory/index/README.md`

**Claim**: `memory/research/` is for "Research findings" per memory/index/README.md and docs/MVP_SCOPE.md.

**Reality**: `memory/research/` contains GHR-XXX (Governance Health Reports) and OPR-XXX (Operational Reports), which are operational reports, not research findings.

**Resolution**: Either:
- (a) Rename directory to `memory/reports/` or `memory/operational_reports/`, OR
- (b) Update documentation to reflect that research/ also holds operational reports

**Governance Impact**: Directory naming should match artifact purpose for auditability.

---

### GAP-014: README Claims "Phase 0" But Active Objectives Suggest Phase 1 Activity

**Severity**: MEDIUM
**Affected Files**: `README.md` (line 161), `governance/PHASE_POLICY.md`, memory objectives

**Claim**: Current phase is "Phase 0: Governance/Bootstrap"

**Reality**: OBJ-004 and OBJ-005 describe "real engineering project usage" and "cross-project operational governance coordination" — activities that align more with Phase 1 ("Controlled Internal Adoption") or Phase 2 ("Operational Multi-Project Usage") per PHASE_POLICY.md.

**Resolution**: Either update phase designation or narrow objective scope descriptions to match Phase 0 boundaries.

**Governance Impact**: Phase misalignment could indicate governance boundary violation.

---

### GAP-015: .gitignore Missing .DS_Store

**Severity**: LOW
**Affected Files**: `.gitignore`

**Reality**: `.DS_Store` exists in the repository root but is not in `.gitignore`.

**Resolution**: Add `.DS_Store` to `.gitignore`.

**Governance Impact**: None — cosmetic.

---

### GAP-016: TRACEABILITY_INDEX WARN Messages Are Expected, Not Errors

**Severity**: INFO
**Affected Files**: `scripts/aeos_lint.py` (check_traceability_integrity function)

**Reality**: The lint script logs WARN for every ID referenced in multiple files. This is by design (traceability IDs ARE meant to be cross-referenced), but the output looks like errors. The check still returns `all_ok = True`.

**Resolution**: Consider changing WARN to INFO or adding a clarifying message that cross-referencing is expected behavior.

**Governance Impact**: None — cosmetic.

---

### GAP-017: No ADR Protocol Enforcement

**Severity**: MEDIUM
**Affected Files**: `protocols/ADR_PROTOCOL.md`, `memory/decisions/`, test suite

**Reality**: ADR_PROTOCOL.md exists but no tests validate ADR compliance. No ADRs have been created. The lifecycle model requires ADRs for architecture changes, but there is no enforcement mechanism.

**Resolution**: Add ADR compliance tests or explicitly note that ADR enforcement is deferred.

**Governance Impact**: Missing enforcement for a core protocol.

---

### GAP-018: CI Workflow Uses Python 3.11, pyproject.toml Requires 3.10+

**Severity**: LOW
**Affected Files**: `.github/workflows/aeos-validation.yml` (line 17), `pyproject.toml` (line 9)

**Reality**: CI uses Python 3.11, pyproject.toml requires >=3.10. This is compatible but the mismatch should be intentional.

**Resolution**: Align versions or document the intentional difference.

**Governance Impact**: None.

---

## Structural Observations

### OBS-001: Dual Directory System (Root + aeos-core/)

The repository has two parallel directory structures:
- Root: Main AEOS Core governance, protocols, templates, agents, workflows, memory, tests
- aeos-core/: Experimental lab with its own governance, memory, templates, tests

This is intentional per README.md (lines 167-173), but the README tree diagram contradicts this by showing everything under `aeos-core/`.

### OBS-002: Test Suite Fragmentation

Tests are split between:
- `tests/` (root) — 11 test files
- `aeos-core/tests/enforcement/` — 3 test files

CI only runs `aeos-core/tests`, missing the root test suite entirely.

### OBS-003: memory/reviews/ Not in Index Directory Map

`memory/index/README.md` lists memory directories but does not include `memory/reviews/` in its directory list, even though 9 review files exist there. The index map shows Reviews pointing to `memory/audits/` which is incorrect.

### OBS-004: ESC-XXX Files Mixed with INC-XXX Files

Escalations (ESC-001, ESC-002, ESC-003) are stored in `memory/incidents/` alongside incidents (INC-001, INC-002, INC-003). This is a design choice but should be documented. The memory index does not mention ESC- as a separate artifact type.

### OBS-005: OPR-XXX and GHR-XXX in research/ Directory

Operational Reports and Governance Health Reports are stored in `memory/research/` which is semantically incorrect. These are not research findings — they are operational governance artifacts.

### OBS-006: No memory/reviews/ Entry in TRACEABILITY_INDEX Directory Map

The TRACEABILITY_INDEX.md artifact count table includes Reviews (9 total) but the directory structure documentation in memory/index/README.md does not list `memory/reviews/` as a directory.
