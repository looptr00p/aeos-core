# AEOS GPT Knowledge Base

**Purpose**: Curated cognition package for AEOS Prompt Engineering GPT
**Created**: 2026-05-19
**Version**: 1.0
**Total Files**: 57
**Total Size**: ~120KB

---

## Purpose

This is a **curated AEOS cognition package** — not a repository backup, not a full export, not a documentation dump.

It contains:
- Stable AEOS philosophy and governance principles
- Operational cognition principles and anti-entropy heuristics
- Longitudinal discoveries from real operational cycles
- Operational prompting philosophy and patterns
- Governance framework structure and protocols

It does **NOT** contain:
- Volatile operational state (active tasks, current metrics, open incidents)
- Transient lifecycle artifacts (individual task files, review reports, audit records)
- Test files, scripts, CI configuration, or build artifacts
- Experimental lab artifacts with low strategic signal

**The repository itself remains the source of truth** for:
- Active objectives and their current status
- Current ADRs and their approval state
- Current lifecycle state (tasks, reviews, audits, handoffs)
- Current governance metrics and dashboard data
- Current incidents and escalations
- Current governance maturity assessment

The GPT should use this knowledge base for **philosophical grounding** and **governance cognition**, and reference the repository for **current operational state**.

---

## Included Categories

| Category | Directory | Files | Purpose |
|----------|-----------|-------|---------|
| Philosophy | `philosophy/` | 4 | Core AEOS worldview, operating model, governance continuity |
| Governance | `governance/` | 7 | All governance policies, rules, and severity models |
| Protocols | `protocols/` | 7 | All operational protocols (task, review, memory, handoff, etc.) |
| Templates | `templates/` | 12 | All canonical artifact templates including approval records |
| Strategic Research | `strategic_research/` | 3 | Updated state of the art, enforcement layer and pressure simulation objectives |
| Operational Patterns | `operational_patterns/` | 12 | Ergonomics, workflow tiering, review minimization, learnings, governance review, validation report |
| Prompt Engineering | `prompt_engineering/` | 2 | Index structure documentation, operational examples |
| Architecture | `architecture/` | 8 | vNext design, enforcement layer, metrics framework, pressure simulation, dashboard template, 3 ADRs |

---

## Excluded Categories

| Category | Reason for Exclusion |
|----------|---------------------|
| `tests/` | Implementation artifacts, not governance cognition |
| `scripts/` | Operational tooling, not philosophy |
| `.github/` | CI configuration, volatile and platform-specific |
| `memory/tasks/` (individual files) | Volatile lifecycle state — repository is source of truth |
| `memory/reviews/` (individual files) | Transient review reports — repository is source of truth |
| `memory/audits/` (individual files) | Transient audit records — repository is source of truth |
| `memory/handoffs/` (individual files) | Transient handoff artifacts — repository is source of truth |
| `memory/incidents/` (individual files) | Volatile incident state — repository is source of truth |
| `memory/objectives/` (OBJ-001 through OBJ-005) | Completed/closed objectives with no strategic discoveries beyond what is captured in learnings docs |
| `memory/decisions/` (beyond ADRs) | No additional decisions exist |
| `memory/research/` (OPR-001 through OPR-006, GHR-001 through GHR-006) | Point-in-time operational reports — OPR-007 is the first under the new framework and contains baseline methodology |
| `aeos-core/` | Experimental lab artifacts — low strategic signal for GPT cognition |
| `REPO_INVENTORY.md`, `GAP_ANALYSIS.md`, `CURRENT_CAPABILITY_MATRIX.md` | Audit artifacts — findings are incorporated into operational patterns and strategic research |
| `ESTADO_DEL_ARTE.md` | Superseded by ESTADO_DEL_ARTE_ACTUALIZADO.md |
| `docs/MVP_SCOPE.md` | Superseded by AEOS_VNEXT_DESIGN.md |
| `docs/OPERATIONAL_EXAMPLES.md` | Included in prompt_engineering/ |

---

## Repository-First Principle

This knowledge base is a **snapshot of stable governance cognition**, not a replacement for the repository.

**When the GPT needs current state**, it should reference:
- The repository for active objectives, tasks, incidents, escalations
- The governance dashboard template for current metric values
- The traceability index for current artifact relationships

**When the GPT needs philosophical grounding**, it should reference:
- This knowledge base for governance principles, operational patterns, and longitudinal discoveries

**Knowledge refresh cycle**: This package should be regenerated when:
1. Governance policies change (new rules, modified protocols)
2. New ADRs are accepted that change architectural direction
3. New strategic discoveries are made in operational cycles
4. The vNext design evolves significantly

Recommended refresh cadence: **Monthly** or upon significant governance change.

---

## Recommended GPT Usage

### What the GPT Should Use This For

- Understanding AEOS governance philosophy and principles
- Applying correct protocols when generating artifacts
- Following template structures for new objectives, tasks, reviews, etc.
- Understanding governance severity levels and response requirements
- Applying operational patterns from real experience
- Understanding the dual directory structure (canonical vs experimental)
- Applying anti-entropy heuristics from longitudinal discoveries

### What the GPT Should NOT Use This For

- Determining current repository state (use the repository directly)
- Knowing which objectives are currently active (use the repository)
- Knowing current metric values (calculate from repository state)
- Making autonomous governance decisions (human authority required)
- Creating artifacts without following proper protocols
- Bypassing review, audit, or approval requirements

---

## Knowledge Refresh Strategy

### When to Refresh

| Trigger | Action |
|---------|--------|
| New governance policy created | Add to governance/ |
| New protocol created | Add to protocols/ |
| New template created | Add to templates/ |
| New ADR accepted | Add to architecture/ |
| New strategic discovery | Add to operational_patterns/ or strategic_research/ |
| vNext design updated | Replace architecture/AEOS_VNEXT_DESIGN.md |
| Monthly cadence | Full review and regeneration |

### How to Refresh

1. Review current repository state
2. Identify new high-signal artifacts
3. Identify stale artifacts to remove
4. Update this README with file count changes
5. Regenerate the knowledge base directory
6. Upload to GPT configuration

### Entropy Control

To prevent knowledge drift and entropy accumulation:
- **Cap total files at 50** — current count is 47
- **Remove before adding** — if a new artifact is added, evaluate whether an existing one should be removed
- **Prefer philosophy over state** — operational artifacts should only be included if they contain strategic discoveries
- **Document removals** — when removing an artifact, note why in this README

---

## File Inventory

### philosophy/ (4 files)
- AEOS_OVERVIEW.md
- OPERATING_MODEL.md
- GOVERNANCE_CONTINUITY.md
- README.md

### governance/ (7 files)
- AGENTS.md
- PHASE_POLICY.md
- PERMISSION_MODEL.md
- REVIEW_REQUIREMENTS.md
- ESCALATION_POLICY.md
- SAFETY_RULES.md
- GOVERNANCE_SEVERITY_MODEL.md

### protocols/ (7 files)
- TASK_PROTOCOL.md
- REVIEW_PROTOCOL.md
- CONTEXT_PROTOCOL.md
- MEMORY_PROTOCOL.md
- HANDOFF_PROTOCOL.md
- INCIDENT_PROTOCOL.md
- ADR_PROTOCOL.md

### templates/ (12 files)
- objective_template.md
- adr_template.md
- task_template.md
- review_template.md
- audit_template.md
- handoff_template.md
- incident_template.md
- operational_report_template.md
- escalation_template.md
- governance_health_report_template.md
- traceability_assistance_template.md
- approval_record_template.md

### strategic_research/ (3 files)
- ESTADO_DEL_ARTE_ACTUALIZADO.md
- OBJ-007.md (Governance Enforcement Layer objective)
- OBJ-008.md (Governance Pressure Simulation objective)

### operational_patterns/ (13 files)
- OPERATIONAL_ERGONOMICS.md
- WORKFLOW_TIERING_GUIDANCE.md
- REVIEW_MINIMIZATION_GUIDANCE.md
- REVIEW_CADENCE.md
- CONCURRENT_OPERATIONS_LEARNINGS.md
- GOVERNANCE_DEBT_RECOVERY_LEARNINGS.md
- GOVERNANCE_STABILIZATION_LEARNINGS.md
- OPERATIONAL_LEARNINGS_EXTERNAL_VALIDATION.md
- REAL_OPERATIONS_LEARNINGS.md
- OPR-007.md (First governance pressure baseline)
- REV-010.md (Governance review report)
- VAL-001.md (Deterministic validation report)
- APR-001.md (Approval record example)

### prompt_engineering/ (2 files)
- README.md (memory index structure)
- OPERATIONAL_EXAMPLES.md

### architecture/ (8 files)
- AEOS_VNEXT_DESIGN.md
- GOVERNANCE_ENFORCEMENT_LAYER.md
- GOVERNANCE_METRICS_FRAMEWORK.md
- GOVERNANCE_PRESSURE_SIMULATION.md
- GOVERNANCE_DASHBOARD_TEMPLATE.md
- ADR-001.md (Dual Directory Structure)
- ADR-002.md (Deterministic Governance Enforcement)
- ADR-003.md (Operational Governance Observability)

---

**Total**: 57 files across 8 categories
