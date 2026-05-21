# Project Charter — [Project Name]

**Created:** YYYY-MM-DD
**Operator:** [Human operator name]
**AEOS Version:** [AEOS template version used]

---

## Vision

[What problem does this project solve? What is the desired outcome?]

## Strategic Objectives

1. [Objective 1 — measurable outcome]
2. [Objective 2 — measurable outcome]
3. [Objective 3 — measurable outcome]

## Technology Stack

| Layer | Technology | Version | Notes |
|-------|-----------|---------|-------|
| Language | [e.g., TypeScript] | [version] | |
| Framework | [e.g., Next.js] | [version] | |
| Database | [e.g., PostgreSQL] | [version] | |
| Infrastructure | [e.g., AWS] | | |
| CI/CD | [e.g., GitHub Actions] | | |

## Project Constraints

- [Constraint 1 — e.g., "Must be deployable by single developer"]
- [Constraint 2 — e.g., "Budget limit: $X/month"]
- [Constraint 3 — e.g., "Must use existing AWS account"]

## Governance Profile

This project uses AEOS governance. Profile selection:

- [ ] **Full** — All governance files, all protocols, all workflows (recommended for complex projects)
- [ ] **Standard** — Core governance, essential protocols, main workflows (recommended for most projects)
- [ ] **Lite** — Minimal governance, basic protocols, single workflow (recommended for small projects)

### Active Governance Files

| File | Status | Notes |
|------|--------|-------|
| `.aegos/governance/AGENTS.md` | Active | Universal agent constraints |
| `.aegos/governance/PERMISSION_MODEL.md` | Active | Permission levels |
| `.aegos/governance/SAFETY_RULES.md` | Active | Non-negotiable rules |
| `.aegos/governance/ESCALATION_POLICY.md` | Active | Escalation rules |
| `.aegos/governance/REVIEW_REQUIREMENTS.md` | Active | Review standards |
| `.aegos/governance/GOVERNANCE_SEVERITY_MODEL.md` | Active | Severity classification |
| `.aegos/governance/STATE_CLASSIFICATION_POLICY.md` | Active | Operational states |
| `.aegos/governance/PHASE_POLICY.md` | Active | Phase definitions |

### Active Protocols

| Protocol | Status | Notes |
|----------|--------|-------|
| `TASK_PROTOCOL.md` | Active | Task lifecycle |
| `REVIEW_PROTOCOL.md` | Active | Review process |
| `CONTEXT_PROTOCOL.md` | Active | Context passing |
| `MEMORY_PROTOCOL.md` | Active | Memory management |
| `HANDOFF_PROTOCOL.md` | Active | Handoff process |
| `INCIDENT_PROTOCOL.md` | Active | Incident handling |
| `ADR_PROTOCOL.md` | Active | Architecture decisions |
| `STATE_TRANSITION_PROTOCOL.md` | Active | State graph transitions |

### Active Workflows

| Workflow | Status | Notes |
|----------|--------|-------|
| `feature_workflow.md` | Active | New feature implementation |
| `bugfix_workflow.md` | Active | Bug fixing |
| `architecture_change_workflow.md` | Active | Architecture changes |
| `audit_workflow.md` | Active | Governance audits |
| `incident_workflow.md` | Active | Incident response |
| `research_workflow.md` | Active | Research and exploration |

## Agent Configuration

| Agent | Role | Model | Status |
|-------|------|-------|--------|
| `director` | Strategy, delegation, coordination | [model] | Active |
| `architect` | Architecture proposals, ADRs | [model] | Active |
| `implementer` | Code implementation | [model] | Active |
| `reviewer` | Code review, validation | [model] | Active |
| `auditor` | Governance audit | [model] | Active |
| `qa` | Test generation and execution | [model] | Active |
| `documentation` | Memory and docs updates | [model] | Active |

## Operational Phase

**Current Phase:** Phase 0 — Governance/Bootstrap

See `.aegos/governance/PHASE_POLICY.md` for phase definitions and exit criteria.

## Success Criteria

- [ ] First operational cycle completed successfully
- [ ] `aeos_lint.py` passes with all checks
- [ ] All governance violations = 0
- [ ] Traceability complete for all artifacts
- [ ] Operator satisfaction: [subjective assessment]

## Notes

[Any additional context, decisions, or considerations specific to this project]
