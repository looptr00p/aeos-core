# Repository Inventory — AEOS Core

**Generated**: 2026-05-19
**Scope**: Full repository audit at `/Users/nicolas/Documents/AEOS_Core_opencode`

---

## Directory Structure

```
AEOS_Core_opencode/
├── .github/workflows/
│   └── aeos-validation.yml
├── .pytest_cache/
├── aeos-core/
│   ├── docs/
│   │   ├── EXPERIMENTAL_LAB_CHARTER.md
│   │   └── EXPERIMENTAL_LAB_OPERATING_NOTES.md
│   ├── governance/
│   │   └── PORTING_POLICY.md
│   ├── memory/
│   │   ├── audits/
│   │   │   ├── AUD-EXP-001.md
│   │   │   ├── AUD-EXP-002.md
│   │   │   └── FORMAT_READABILITY_AUDIT_001.md
│   │   ├── experiments/
│   │   │   ├── EXP-001.md
│   │   │   ├── FORMAT_REMEDIATION_AUDIT.md
│   │   │   ├── PORT-001.md
│   │   │   ├── PORTABILITY_RISK_ASSESSMENT_001.md
│   │   │   └── PORTING_CANDIDATE_REVIEW_001.md
│   │   ├── handoffs/
│   │   │   ├── HND-AUD-001.md
│   │   │   └── HND-EXP-001.md
│   │   ├── objectives/
│   │   │   ├── OBJ-AUD-001.md
│   │   │   └── OBJ-EXP-001.md
│   │   ├── reviews/
│   │   │   └── REV-EXP-001.md
│   │   └── tasks/
│   │       ├── TASK-AUD-001.md
│   │       └── TASK-EXP-001.md
│   ├── scripts/
│   │   └── aeos_lint.py
│   ├── templates/
│   │   ├── experiment_template.md
│   │   └── porting_review_template.md
│   └── tests/
│       └── enforcement/
│           ├── test_experiment_evaluation_cycle_001.py
│           ├── test_experimental_governance_audit_001.py
│           └── test_experimental_lab_role.py
├── agents/
│   ├── agent_registry.yaml
│   ├── architect/
│   │   └── architect_agent.yaml
│   ├── auditor/
│   │   └── auditor_agent.yaml
│   ├── director/
│   │   └── director_agent.yaml
│   ├── documentation/
│   │   └── documentation_agent.yaml
│   ├── implementer/
│   │   └── implementer_agent.yaml
│   ├── qa/
│   │   └── qa_agent.yaml
│   └── reviewer/
│       └── reviewer_agent.yaml
├── docs/
│   ├── AEOS_OVERVIEW.md
│   ├── CONCURRENT_OPERATIONS_LEARNINGS.md
│   ├── GOVERNANCE_CONTINUITY.md
│   ├── GOVERNANCE_DEBT_RECOVERY_LEARNINGS.md
│   ├── GOVERNANCE_STABILIZATION_LEARNINGS.md
│   ├── MVP_SCOPE.md
│   ├── OPERATING_MODEL.md
│   ├── OPERATIONAL_ERGONOMICS.md
│   ├── OPERATIONAL_EXAMPLES.md
│   ├── OPERATIONAL_LEARNINGS_EXTERNAL_VALIDATION.md
│   ├── REAL_OPERATIONS_LEARNINGS.md
│   ├── REVIEW_CADENCE.md
│   ├── REVIEW_MINIMIZATION_GUIDANCE.md
│   └── WORKFLOW_TIERING_GUIDANCE.md
├── governance/
│   ├── AGENTS.md
│   ├── ESCALATION_POLICY.md
│   ├── GOVERNANCE_SEVERITY_MODEL.md
│   ├── PERMISSION_MODEL.md
│   ├── PHASE_POLICY.md
│   ├── REVIEW_REQUIREMENTS.md
│   └── SAFETY_RULES.md
├── memory/
│   ├── architecture/ (.gitkeep)
│   ├── audits/
│   │   ├── AUD-001.md
│   │   ├── AUD-002.md
│   │   └── AUD-003.md
│   ├── decisions/ (.gitkeep)
│   ├── handoffs/
│   │   ├── HND-001.md through HND-007.md (7 files)
│   ├── incidents/
│   │   ├── ESC-001.md, ESC-002.md, ESC-003.md
│   │   ├── INC-001.md, INC-002.md, INC-003.md
│   ├── index/
│   │   ├── README.md
│   │   ├── TRACEABILITY_INDEX.md
│   │   └── traceability_index_template.md
│   ├── objectives/
│   │   ├── OBJ-001.md through OBJ-005.md (5 files)
│   ├── research/
│   │   ├── GHR-001.md through GHR-006.md (6 files)
│   │   └── OPR-001.md through OPR-006.md (6 files)
│   ├── reviews/
│   │   ├── REV-001.md through REV-009.md (9 files)
│   └── tasks/
│       ├── TASK-001.md through TASK-011.md (11 files)
├── protocols/
│   ├── ADR_PROTOCOL.md
│   ├── CONTEXT_PROTOCOL.md
│   ├── HANDOFF_PROTOCOL.md
│   ├── INCIDENT_PROTOCOL.md
│   ├── MEMORY_PROTOCOL.md
│   ├── REVIEW_PROTOCOL.md
│   └── TASK_PROTOCOL.md
├── scripts/
│   └── aeos_lint.py
├── templates/
│   ├── adr_template.md
│   ├── audit_template.md
│   ├── escalation_template.md
│   ├── governance_health_report_template.md
│   ├── handoff_template.md
│   ├── incident_template.md
│   ├── objective_template.md
│   ├── operational_report_template.md
│   ├── review_template.md
│   ├── task_template.md
│   └── traceability_assistance_template.md
├── tests/
│   ├── agents/
│   │   └── test_agent_registry.py
│   ├── governance/
│   │   └── test_required_governance_files.py
│   ├── protocols/
│   │   └── test_required_protocol_files.py
│   ├── templates/
│   │   └── test_required_template_files.py
│   ├── workflows/
│   │   └── test_required_workflows.py
│   ├── test_concurrent_operations.py
│   ├── test_governance_debt_recovery.py
│   ├── test_governance_stabilization.py
│   ├── test_lifecycle_continuity.py
│   ├── test_v02_operational_continuity.py
│   └── test_v03_operational_readiness.py
├── workflows/
│   ├── architecture_change_workflow.md
│   ├── audit_workflow.md
│   ├── bugfix_workflow.md
│   ├── feature_workflow.md
│   ├── incident_workflow.md
│   └── research_workflow.md
├── .gitignore
├── pyproject.toml
├── README.md
└── ESTADO_DEL_ARTE.md
```

---

## Lifecycle Artifacts

| Type | Count | Location |
|------|-------|----------|
| Objectives | 5 | `memory/objectives/` |
| Tasks | 11 | `memory/tasks/` |
| Reviews | 9 | `memory/reviews/` |
| Audits | 3 | `memory/audits/` |
| Handoffs | 7 | `memory/handoffs/` |
| Incidents | 3 | `memory/incidents/` |
| Escalations | 3 | `memory/incidents/` (ESC- prefix) |
| Operational Reports | 6 | `memory/research/` (OPR- prefix) |
| Governance Health Reports | 6 | `memory/research/` (GHR- prefix) |
| **Total main memory** | **53** | |
| Experimental Objectives | 2 | `aeos-core/memory/objectives/` |
| Experimental Tasks | 2 | `aeos-core/memory/tasks/` |
| Experimental Reviews | 1 | `aeos-core/memory/reviews/` |
| Experimental Audits | 3 | `aeos-core/memory/audits/` |
| Experimental Handoffs | 2 | `aeos-core/memory/handoffs/` |
| Experiments | 5 | `aeos-core/memory/experiments/` |
| **Total aeos-core memory** | **15** | |

---

## Governance Files

| File | Location | Status |
|------|----------|--------|
| AGENTS.md | `governance/` | Present |
| PHASE_POLICY.md | `governance/` | Present |
| PERMISSION_MODEL.md | `governance/` | Present |
| REVIEW_REQUIREMENTS.md | `governance/` | Present |
| ESCALATION_POLICY.md | `governance/` | Present |
| SAFETY_RULES.md | `governance/` | Present |
| GOVERNANCE_SEVERITY_MODEL.md | `governance/` | Present |
| PORTING_POLICY.md | `aeos-core/governance/` | Present (experimental) |

---

## Protocol Files

| File | Location | Status |
|------|----------|--------|
| TASK_PROTOCOL.md | `protocols/` | Present |
| REVIEW_PROTOCOL.md | `protocols/` | Present |
| CONTEXT_PROTOCOL.md | `protocols/` | Present |
| MEMORY_PROTOCOL.md | `protocols/` | Present |
| HANDOFF_PROTOCOL.md | `protocols/` | Present |
| INCIDENT_PROTOCOL.md | `protocols/` | Present |
| ADR_PROTOCOL.md | `protocols/` | Present |

---

## Template Files

| File | Location | Status |
|------|----------|--------|
| objective_template.md | `templates/` | Present |
| adr_template.md | `templates/` | Present |
| task_template.md | `templates/` | Present |
| review_template.md | `templates/` | Present |
| audit_template.md | `templates/` | Present |
| handoff_template.md | `templates/` | Present |
| incident_template.md | `templates/` | Present |
| operational_report_template.md | `templates/` | Present |
| escalation_template.md | `templates/` | Present |
| governance_health_report_template.md | `templates/` | Present |
| traceability_assistance_template.md | `templates/` | Present |
| experiment_template.md | `aeos-core/templates/` | Present (experimental) |
| porting_review_template.md | `aeos-core/templates/` | Present (experimental) |

---

## Workflow Files

| File | Location | Status |
|------|----------|--------|
| feature_workflow.md | `workflows/` | Present |
| bugfix_workflow.md | `workflows/` | Present |
| architecture_change_workflow.md | `workflows/` | Present |
| audit_workflow.md | `workflows/` | Present |
| incident_workflow.md | `workflows/` | Present |
| research_workflow.md | `workflows/` | Present |

---

## Agent Definitions

| Agent | Registry Entry | YAML Definition | Status |
|-------|---------------|-----------------|--------|
| director-agent | Yes | `agents/director/director_agent.yaml` | Present |
| architect-agent | Yes | `agents/architect/architect_agent.yaml` | Present |
| implementer-agent | Yes | `agents/implementer/implementer_agent.yaml` | Present |
| reviewer-agent | Yes | `agents/reviewer/reviewer_agent.yaml` | Present |
| auditor-agent | Yes | `agents/auditor/auditor_agent.yaml` | Present |
| qa-agent | Yes | `agents/qa/qa_agent.yaml` | Present |
| documentation-agent | Yes | `agents/documentation/documentation_agent.yaml` | Present |

---

## Test Files

| File | Location | Purpose |
|------|----------|---------|
| test_required_governance_files.py | `tests/governance/` | Governance file existence |
| test_required_protocol_files.py | `tests/protocols/` | Protocol file existence |
| test_required_template_files.py | `tests/templates/` | Template file existence |
| test_agent_registry.py | `tests/agents/` | Agent registry validation |
| test_required_workflows.py | `tests/workflows/` | Workflow file existence |
| test_concurrent_operations.py | `tests/` | Concurrent objective validation |
| test_governance_debt_recovery.py | `tests/` | Debt recovery state validation |
| test_governance_stabilization.py | `tests/` | Stabilization state validation |
| test_lifecycle_continuity.py | `tests/` | Lifecycle reference validation |
| test_v02_operational_continuity.py | `tests/` | v0.2 artifact validation |
| test_v03_operational_readiness.py | `tests/` | v0.3 artifact validation |
| test_experiment_evaluation_cycle_001.py | `aeos-core/tests/enforcement/` | Experimental cycle validation |
| test_experimental_governance_audit_001.py | `aeos-core/tests/enforcement/` | Experimental audit validation |
| test_experimental_lab_role.py | `aeos-core/tests/enforcement/` | Experimental lab role validation |

---

## CI Configuration

| File | Status |
|------|--------|
| `.github/workflows/aeos-validation.yml` | Present |

---

## Scripts

| File | Purpose |
|------|---------|
| `scripts/aeos_lint.py` | Main operational lint (11 checks) |
| `aeos-core/scripts/aeos_lint.py` | Delegated lint for aeos-core subproject |

---

## Documentation Files

| File | Purpose |
|------|---------|
| README.md | Main repository documentation |
| ESTADO_DEL_ARTE.md | Spanish-language state-of-the-art (v0.1.0) |
| docs/AEOS_OVERVIEW.md | System overview |
| docs/OPERATING_MODEL.md | Operating model description |
| docs/MVP_SCOPE.md | MVP deliverables |
| docs/GOVERNANCE_CONTINUITY.md | Governance continuity principles |
| docs/REVIEW_CADENCE.md | Review cycle definitions |
| docs/OPERATIONAL_EXAMPLES.md | Lifecycle examples |
| docs/OPERATIONAL_ERGONOMICS.md | Ergonomics findings |
| docs/WORKFLOW_TIERING_GUIDANCE.md | Workflow tiering guidance |
| docs/REVIEW_MINIMIZATION_GUIDANCE.md | Review minimization guidance |
| docs/CONCURRENT_OPERATIONS_LEARNINGS.md | Concurrent operations learnings |
| docs/GOVERNANCE_DEBT_RECOVERY_LEARNINGS.md | Debt recovery learnings |
| docs/GOVERNANCE_STABILIZATION_LEARNINGS.md | Stabilization learnings |
| docs/OPERATIONAL_LEARNINGS_EXTERNAL_VALIDATION.md | External validation learnings |
| docs/REAL_OPERATIONS_LEARNINGS.md | Real operations learnings |

---

## Configuration Files

| File | Purpose |
|------|---------|
| pyproject.toml | Python project config (version 0.1.0) |
| .gitignore | Git ignore rules |
| agents/agent_registry.yaml | Central agent registry |
| .github/workflows/aeos-validation.yml | CI/CD pipeline |

---

## Memory Structure

| Directory | Content | gitkeep |
|-----------|---------|---------|
| memory/objectives/ | 5 files | Yes |
| memory/tasks/ | 11 files | Yes |
| memory/reviews/ | 9 files | No |
| memory/audits/ | 3 files | Yes |
| memory/handoffs/ | 7 files | Yes |
| memory/incidents/ | 6 files | Yes |
| memory/decisions/ | 0 files | Yes |
| memory/architecture/ | 0 files | Yes |
| memory/research/ | 12 files | Yes |
| memory/index/ | 3 files | No |

---

## aeos-core Subproject Structure

| Directory | Content |
|-----------|---------|
| aeos-core/docs/ | 2 files (experimental lab) |
| aeos-core/governance/ | 1 file (porting policy) |
| aeos-core/memory/audits/ | 3 files |
| aeos-core/memory/experiments/ | 5 files |
| aeos-core/memory/handoffs/ | 2 files |
| aeos-core/memory/objectives/ | 2 files |
| aeos-core/memory/reviews/ | 1 file |
| aeos-core/memory/tasks/ | 2 files |
| aeos-core/scripts/ | 1 file (delegated lint) |
| aeos-core/templates/ | 2 files |
| aeos-core/tests/enforcement/ | 3 files |
