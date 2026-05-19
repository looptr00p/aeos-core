# Current Capability Matrix — AEOS Core

**Generated**: 2026-05-19
**Basis**: Verified repository state (not documentation claims)

---

## Governance Capability

| Capability | Status | Evidence |
|-----------|--------|----------|
| Universal agent constraints | IMPLEMENTED | `governance/AGENTS.md` |
| Phase definitions and transitions | IMPLEMENTED | `governance/PHASE_POLICY.md` |
| Permission model | IMPLEMENTED | `governance/PERMISSION_MODEL.md` |
| Review requirements | IMPLEMENTED | `governance/REVIEW_REQUIREMENTS.md` |
| Escalation policy | IMPLEMENTED | `governance/ESCALATION_POLICY.md` |
| Safety rules | IMPLEMENTED | `governance/SAFETY_RULES.md` |
| Severity model (LOW/MED/HIGH/CRIT) | IMPLEMENTED | `governance/GOVERNANCE_SEVERITY_MODEL.md` |
| Porting policy (experimental) | IMPLEMENTED | `aeos-core/governance/PORTING_POLICY.md` |

**Coverage**: 8/8 governance files present and validated.

---

## Protocol Capability

| Protocol | Status | Evidence |
|----------|--------|----------|
| Task lifecycle | IMPLEMENTED | `protocols/TASK_PROTOCOL.md` |
| Review process | IMPLEMENTED | `protocols/REVIEW_PROTOCOL.md` |
| Context requirements | IMPLEMENTED | `protocols/CONTEXT_PROTOCOL.md` |
| Memory management | IMPLEMENTED | `protocols/MEMORY_PROTOCOL.md` |
| Handoff requirements | IMPLEMENTED | `protocols/HANDOFF_PROTOCOL.md` |
| Incident response | IMPLEMENTED | `protocols/INCIDENT_PROTOCOL.md` |
| ADR process | DEFINED (not enforced) | `protocols/ADR_PROTOCOL.md` |

**Coverage**: 7/7 protocol files present. ADR enforcement not tested.

---

## Template Capability

| Template | Status | Evidence |
|----------|--------|----------|
| Objective | IMPLEMENTED | `templates/objective_template.md` |
| ADR | IMPLEMENTED | `templates/adr_template.md` |
| Task | IMPLEMENTED | `templates/task_template.md` |
| Review | IMPLEMENTED | `templates/review_template.md` |
| Audit | IMPLEMENTED | `templates/audit_template.md` |
| Handoff | IMPLEMENTED | `templates/handoff_template.md` |
| Incident | IMPLEMENTED | `templates/incident_template.md` |
| Operational Report | IMPLEMENTED | `templates/operational_report_template.md` |
| Escalation | IMPLEMENTED | `templates/escalation_template.md` |
| Governance Health Report | IMPLEMENTED | `templates/governance_health_report_template.md` |
| Traceability Assistance | IMPLEMENTED | `templates/traceability_assistance_template.md` |
| Experiment (experimental) | IMPLEMENTED | `aeos-core/templates/experiment_template.md` |
| Porting Review (experimental) | IMPLEMENTED | `aeos-core/templates/porting_review_template.md` |

**Coverage**: 13/13 templates present.

---

## Agent Capability

| Agent | Registered | YAML Defined | Required Fields | Self-Approval Forbidden |
|-------|-----------|--------------|-----------------|------------------------|
| director-agent | Yes | Yes | Yes (20 fields) | Yes |
| architect-agent | Yes | Yes | Yes (20 fields) | Yes |
| implementer-agent | Yes | Yes | Yes (20 fields) | Yes |
| reviewer-agent | Yes | Yes | Yes (20 fields) | Yes |
| auditor-agent | Yes | Yes | Yes (20 fields) | Yes |
| qa-agent | Yes | Yes | Yes (20 fields) | Yes |
| documentation-agent | Yes | Yes | Yes (20 fields) | Yes |

**Coverage**: 7/7 agents fully defined with all required fields. No unrestricted permissions detected.

---

## Workflow Capability

| Workflow | Status | Evidence |
|----------|--------|----------|
| Feature development | IMPLEMENTED | `workflows/feature_workflow.md` |
| Bug fix | IMPLEMENTED | `workflows/bugfix_workflow.md` |
| Architecture change | IMPLEMENTED | `workflows/architecture_change_workflow.md` |
| Audit | IMPLEMENTED | `workflows/audit_workflow.md` |
| Incident response | IMPLEMENTED | `workflows/incident_workflow.md` |
| Research | IMPLEMENTED | `workflows/research_workflow.md` |

**Coverage**: 6/6 workflows present.

---

## Memory Capability

| Artifact Type | Directory | Files Present | Template Available |
|--------------|-----------|---------------|-------------------|
| Objectives (OBJ-XXX) | `memory/objectives/` | 5 | Yes |
| Tasks (TASK-XXX) | `memory/tasks/` | 11 | Yes |
| Reviews (REV-XXX) | `memory/reviews/` | 9 | Yes |
| Audits (AUD-XXX) | `memory/audits/` | 3 | Yes |
| Handoffs (HND-XXX) | `memory/handoffs/` | 7 | Yes |
| Incidents (INC-XXX) | `memory/incidents/` | 3 | Yes |
| Escalations (ESC-XXX) | `memory/incidents/` | 3 | Yes (escalation_template) |
| Operational Reports (OPR-XXX) | `memory/research/` | 6 | Yes |
| Governance Health Reports (GHR-XXX) | `memory/research/` | 6 | Yes |
| ADRs (ADR-XXX) | `memory/decisions/` | 0 | Yes |
| Architecture docs | `memory/architecture/` | 0 | N/A |

**Experimental Memory** (aeos-core):
| Artifact Type | Files Present |
|--------------|---------------|
| Objectives | 2 |
| Tasks | 2 |
| Reviews | 1 |
| Audits | 3 |
| Handoffs | 2 |
| Experiments | 5 |

---

## Traceability Capability

| Check | Status | Evidence |
|-------|--------|----------|
| All tasks reference objectives | PASS | aeos_lint.py check 5, 9 |
| Closed tasks reference handoffs | PASS | aeos_lint.py check 5 |
| All referenced IDs are defined | PASS | aeos_lint.py check 8 |
| No malformed ID prefixes | PASS | aeos_lint.py check 8 |
| Active incidents have valid refs | PASS | aeos_lint.py check 9 |
| Open escalations have valid refs | PASS | aeos_lint.py check 9 |
| IN_PROGRESS tasks reference objectives | PASS | aeos_lint.py check 9 |
| Recovery continuity | PASS | aeos_lint.py check 11 |

**Coverage**: All traceability checks pass. Cross-referencing is extensive (expected behavior).

---

## Validation Capability

| Validation | Status | Evidence |
|-----------|--------|----------|
| Required file existence (lint) | PASS | `scripts/aeos_lint.py` — 11 checks |
| Required file existence (pytest) | UNVERIFIED | pytest not installed in environment |
| Governance file tests | DEFINED | `tests/governance/test_required_governance_files.py` |
| Protocol file tests | DEFINED | `tests/protocols/test_required_protocol_files.py` |
| Template file tests | DEFINED | `tests/templates/test_required_template_files.py` |
| Agent registry tests | DEFINED | `tests/agents/test_agent_registry.py` |
| Workflow file tests | DEFINED | `tests/workflows/test_required_workflows.py` |
| Lifecycle continuity tests | DEFINED | `tests/test_lifecycle_continuity.py` |
| Concurrent operations tests | DEFINED | `tests/test_concurrent_operations.py` |
| Governance debt recovery tests | DEFINED | `tests/test_governance_debt_recovery.py` |
| Governance stabilization tests | DEFINED | `tests/test_governance_stabilization.py` |
| v0.2 continuity tests | DEFINED | `tests/test_v02_operational_continuity.py` |
| v0.3 readiness tests | DEFINED | `tests/test_v03_operational_readiness.py` |
| Experimental lab tests | DEFINED | `aeos-core/tests/enforcement/` (3 files) |

**Coverage**: 14 test files defined. Actual test execution not verifiable (pytest not installed).

---

## CI/CD Capability

| Component | Status | Evidence |
|-----------|--------|----------|
| GitHub Actions workflow | DEFINED | `.github/workflows/aeos-validation.yml` |
| Python setup | CONFIGURED | Python 3.11 |
| Dependency installation | CONFIGURED | pytest, pyyaml |
| Test execution | PARTIAL | Runs `aeos-core/tests` only (misses root `tests/`) |
| Lint execution | CONFIGURED | Runs `aeos-core/scripts/aeos_lint.py` |

**Coverage**: CI is defined but incomplete — does not run root-level test suite.

---

## Documentation Capability

| Document | Status | Currency |
|----------|--------|----------|
| README.md | PRESENT | Stale (incorrect tree, version mismatch) |
| ESTADO_DEL_ARTE.md | PRESENT | Stale (v0.1.0 metrics, incorrect tree) |
| AEOS_OVERVIEW.md | PRESENT | Current |
| OPERATING_MODEL.md | PRESENT | Current |
| MVP_SCOPE.md | PRESENT | Current |
| GOVERNANCE_CONTINUITY.md | PRESENT | Current |
| REVIEW_CADENCE.md | PRESENT | Current |
| OPERATIONAL_EXAMPLES.md | PRESENT | Current |
| OPERATIONAL_ERGONOMICS.md | PRESENT | Current |
| WORKFLOW_TIERING_GUIDANCE.md | PRESENT | Current |
| REVIEW_MINIMIZATION_GUIDANCE.md | PRESENT | Current |
| CONCURRENT_OPERATIONS_LEARNINGS.md | PRESENT | Current |
| GOVERNANCE_DEBT_RECOVERY_LEARNINGS.md | PRESENT | Current |
| GOVERNANCE_STABILIZATION_LEARNINGS.md | PRESENT | Current |
| OPERATIONAL_LEARNINGS_EXTERNAL_VALIDATION.md | PRESENT | Current |
| REAL_OPERATIONS_LEARNINGS.md | PRESENT | Current |

---

## What AEOS Core CANNOT Do (Verified)

| Capability | Status |
|-----------|--------|
| Autonomous execution | NOT PRESENT (by design) |
| Runtime orchestration | NOT PRESENT (by design) |
| Workflow execution engine | NOT PRESENT (by design) |
| Database/vector store | NOT PRESENT (by design) |
| API/networking layers | NOT PRESENT (by design) |
| Distributed runtime | NOT PRESENT (by design) |
| Self-modifying agents | NOT PRESENT (by design) |
| Hidden memory | NOT PRESENT (by design) |
| Automated test execution (local) | NOT FUNCTIONAL (pytest not installed) |
| Complete CI validation | INCOMPLETE (misses root tests) |
| ADR enforcement | NOT ENFORCED (no tests) |

---

## Operational State Summary

| Metric | Value |
|--------|-------|
| Active objectives | 3 (OBJ-003, OBJ-004, OBJ-005) |
| Closed tasks | 6 (TASK-001 through TASK-005, TASK-007) |
| In-progress tasks | 5 (TASK-006, TASK-008 through TASK-011) |
| Resolved incidents | 1 (INC-001) |
| Active incidents | 2 (INC-002, INC-003) |
| Open escalations | 1 (ESC-003) |
| In-review escalations | 1 (ESC-002) |
| Resolved escalations | 1 (ESC-001) |
| Total memory artifacts | 53 (main) + 15 (experimental) = 68 |
| Governance files | 8 |
| Protocol files | 7 |
| Template files | 13 |
| Workflow files | 6 |
| Agent definitions | 7 |
| Test files | 14 |
| Lint checks | 11 (all passing) |

---

## Phase Assessment

**Claimed Phase**: Phase 0 (Governance/Bootstrap)

**Exit Criteria Status**:
| Criterion | Status |
|-----------|--------|
| All governance files created | PASS (7/7 + 1 experimental) |
| All protocols defined | PASS (7/7) |
| All templates ready | PASS (11/11 + 2 experimental) |
| Tests passing | UNVERIFIED (pytest not installed) |

**Assessment**: Phase 0 exit criteria are nearly met. The only unverifiable criterion is test execution. However, active objectives (OBJ-004, OBJ-005) describe activities beyond Phase 0 scope.
