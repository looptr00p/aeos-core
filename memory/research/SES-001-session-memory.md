# Session Memory — AEOS Evolution to AI Engineering Studio

**Traceability ID:** SES-001
**Date:** 2026-05-20 to 2026-05-21
**Operator:** Nicolas (human)
**Director Agent:** opencode
**Branch:** `feature/ai-engineering-studio-evolution`
**Repository:** `github.com/looptr00p/aeos-core`

---

## 1. Problem Statement

### Original Problem

The operator works with multiple AI agents when building applications but has become "the messenger between IAs" — manually routing context between agents for planning, prompts, and coding. There is no orchestration, no governance, and loss of context over time.

### Desired State

A system where the operator talks to a single agent (the Director) which orchestrates a team of specialized agents behind the scenes, like a company. The Director handles strategy and delegation; specialized agents handle execution. All project memory lives in the project itself (markdown files in the repo), maintained by the agents according to governance rules.

---

## 2. Strategic Insight (from ChatGPT analysis)

The operator shared this conversation with ChatGPT, which provided critical analysis:

### Key Insight: AEOS is not a "multi-agent framework"

The real problem is **organizational cognition infrastructure** — how to preserve strategic and operational continuity while multiple intelligences participate in a project.

### What AEOS Already Had Right

- **Markdown-first:** portable, git-native, auditable, human-readable, model-readable, durable
- **Explicit governance:** agents without governance eventually diverge
- **Organizational roles:** the problem is not "which model to use" but "what cognitive responsibility does each actor have"
- **"Memory of the project lives in the project":** this is the strongest differentiator — project-native cognition

### What Was Missing

- **State graph orchestration, not pipeline:** real projects are not linear. They are cognitive loops (QA finds bugs → redefines spec → PM reprioritizes → architecture changes → developer blocked → devops resolves constraint → reviewer finds strategic inconsistency → director realigns)
- **3-layer architecture:**
  - Layer 1: Cognitive Governance Layer (permanent)
  - Layer 2: Agent Orchestration Layer (replaceable)
  - Layer 3: Execution Layer (replaceable — OpenCode, Claude Code, Cursor, etc.)

### What to Avoid

- Converting to SaaS too quickly
- Dashboard-heavy approach
- Multi-user/auth-first before the core value is proven
- Cloud orchestration before operational cognition integrity is established

---

## 3. Architecture Decision

### Decision: Evolve AEOS, Don't Replace

AEOS Core v0.3 already had solid governance (8 files, 7 protocols, 6 workflows, 12 templates, 7 agents, validation tools). The decision was to evolve it rather than build from scratch.

### ADR-004

Created `memory/decisions/ADR-004.md` documenting:
- Context: AEOS v0.3 has gaps (no execution integration, linear workflows, not template-izable)
- Options: Build from scratch (rejected), Evolve with layered architecture (accepted), Integrate with existing framework (rejected — violates AEOS safety rules)
- Decision: Evolve AEOS Core with layered architecture in 4 phases

---

## 4. Implementation Plan

### Phase 1: OpenCode Integration (Capa 2 — Agent Orchestration)
- Create `.opencode/opencode.json` with 7 agents and mixed models
- Create agent definition files in `.opencode/agents/`
- Create `aeos-governance` skill for OpenCode
- Models: claude-sonnet-4 for director/architect (strategic reasoning), claude-3.5-haiku for execution agents (cost efficiency)

### Phase 2: State Graph Orchestration
- Create `workflows/state_graph.md` defining nodes, edges, and feedback loops
- Create `protocols/STATE_TRANSITION_PROTOCOL.md` for recording transitions
- Create `memory/state-log/` for transition records
- Update all existing workflows to reference state graph and feedback loops

### Phase 3: Template-ization
- Create reusable AEOS template structure
- Adapt governance to be project-agnostic (`.aegos/` prefix)
- Create `project-charter.md` template
- Adapt `aeos_lint.py` to be configurable via environment variables
- Create `template/README.md` with instructions and governance profiles

### Phase 4: CLI `studio`
- Build CLI tool for bootstrapping, managing, and auditing AEOS projects
- Commands: `studio init`, `studio status`, `studio audit`, `studio validate`
- Built with typer + rich + pyyaml
- Support for governance profiles (full, standard, lite)

### Phase 5: Validation (Future)
- Apply template to a real project
- Execute first operational cycle
- Document learnings
- Iterate

### Phase 6: Scaling (Future)
- Multi-project support
- Dashboard
- Agent/skill registry

---

## 5. What Was Built

### Phase 1: OpenCode Integration

**Files created:**
- `.opencode/opencode.json` — 7 agents, mixed models, permission rules
- `.opencode/agents/director.md` — Primary agent, human interface, delegation
- `.opencode/agents/architect.md` — Architecture proposals, ADRs
- `.opencode/agents/implementer.md` — Code implementation within scope
- `.opencode/agents/reviewer.md` — Code review against specs and governance
- `.opencode/agents/auditor.md` — Governance compliance audit
- `.opencode/agents/qa.md` — Test generation and execution
- `.opencode/agents/documentation.md` — Memory and docs updates
- `.opencode/skills/aeos-governance/SKILL.md` — Governance rules, protocols, permissions

**Agent model assignments:**
| Agent | Model | Rationale |
|-------|-------|-----------|
| director | claude-sonnet-4-20250514 | Strategic reasoning, complex coordination |
| architect | claude-sonnet-4-20250514 | Complex architectural analysis |
| implementer | claude-3-5-haiku-20241022 | Cost-efficient code generation |
| reviewer | claude-3-5-haiku-20241022 | Cost-efficient review |
| auditor | claude-3-5-haiku-20241022 | Cost-efficient compliance checks |
| qa | claude-3-5-haiku-20241022 | Cost-efficient test generation |
| documentation | claude-3-5-haiku-20241022 | Cost-efficient doc updates |

### Phase 2: State Graph Orchestration

**Files created:**
- `workflows/state_graph.md` — Complete state graph with 10 nodes, forward edges, 8 feedback loops, and escalation paths
- `protocols/STATE_TRANSITION_PROTOCOL.md` — Protocol for recording each state transition (ST-NNN format)
- `memory/state-log/.gitkeep` — Directory for state transition records

**Files updated:**
- `workflows/feature_workflow.md` — Added state graph mapping, feedback loops table, ST-NNN artifacts
- `workflows/bugfix_workflow.md` — Added state graph integration
- `workflows/architecture_change_workflow.md` — Added state graph integration
- `workflows/audit_workflow.md` — Added state graph integration
- `workflows/incident_workflow.md` — Added state graph integration
- `workflows/research_workflow.md` — Added state graph integration

**State Graph Nodes:**
1. `objective_defined` → `architecture_reviewed` → `task_defined` → `implementing` → `reviewing` → `testing` → `auditing` → `documenting` → `handoff_complete` → `closed`

**Feedback Loops:**
- reviewing → implementing (review finds issues)
- testing → implementing (tests fail)
- testing → task_defined (spec ambiguous)
- auditing → reviewing (gaps in review)
- auditing → objective_defined (strategic inconsistency)
- implementing → architecture_reviewed (technical constraint discovered)
- implementing → task_defined (scope insufficient)
- documenting → implementing (memory doesn't match code)

### Phase 3: Template-ization

**Files created (61 total in `template/`):**
- `template/.aegos/governance/` — 8 governance files (AGENTS.md, PERMISSION_MODEL.md, SAFETY_RULES.md, etc.)
- `template/.aegos/protocols/` — 8 protocols (including STATE_TRANSITION_PROTOCOL.md)
- `template/.aegos/workflows/` — 7 workflows (including state_graph.md)
- `template/.aegos/templates/` — 12 artifact templates
- `template/.opencode/opencode.json` — Agent configuration
- `template/.opencode/agents/` — 7 agent definition files
- `template/.opencode/skills/aeos-governance/SKILL.md` — Governance skill
- `template/memory/` — 12 memory directories with .gitkeep files
- `template/scripts/aeos_lint.py` — Configurable lint script
- `template/AGENTS.md` — Universal agent constraints
- `template/project-charter.md` — Project-specific configuration template
- `template/README.md` — Template usage instructions
- `template/.gitignore`

**Governance Profiles:**
| Profile | Governance Files | Protocols | Workflows | Best For |
|---------|-----------------|-----------|-----------|----------|
| Full | All 8 | All 8 | All 7 | Complex projects |
| Standard | 5 core | 6 essential | 3 main | Most projects (default) |
| Lite | 3 essential | 3 basic | 1 | Small projects |

**Lint script adaptations:**
- Configurable via environment variables (AEOS_GOVERNANCE_DIR, AEOS_PROTOCOLS_DIR, etc.)
- Profile-aware: SKIP instead of FAIL for files not in profile
- Supports both agent_registry.yaml and opencode.json for agent registry
- Added OpenCode configuration validation check

### Phase 4: CLI `studio`

**Files created:**
- `cli/pyproject.toml` — Package definition with typer, rich, pyyaml dependencies
- `cli/src/studio/__init__.py` — Package init with version
- `cli/src/studio/cli.py` — Typer entry point with 4 subcommands + version
- `cli/src/studio/commands/init.py` — `studio init` with profile support and progress display
- `cli/src/studio/commands/status.py` — `studio status` showing objectives, tasks, ADRs, incidents, artifacts, agents
- `cli/src/studio/commands/audit.py` — `studio audit` running lint + escalation checks
- `cli/src/studio/commands/validate.py` — `studio validate` running lint + optional pytest
- `cli/README.md` — CLI documentation

**Commands:**
```
studio init [path] [-p profile] [--force]    # Bootstrap AEOS
studio status [path]                          # Show project state
studio audit [path]                           # Run governance audit
studio validate [path] [--no-tests]           # Run lint + tests
studio version                                # Show version
```

### README Update

Updated `README.md` to v0.4:
- Added 3-layer architecture diagram
- Added state graph workflows documentation
- Added reusable template section with copy instructions
- Added v0.4 additions summary
- Updated repository structure table
- Updated session boot sequence to include state transition logging

---

## 6. Commits

| Commit Hash | Description | Files Changed |
|-------------|-------------|---------------|
| `25ad10e` | Phase 1 + 2: OpenCode integration, state graph, governance skill | 18 files, +1265 lines |
| `ac3e80f` | ADR-004: Document evolution decision | 1 file, +195 lines |
| `9bb4b29` | Phase 3: Reusable template | 61 files, +4807 lines |
| `8633b84` | Fix: Configurable lint severity check | 1 file, +1/-1 |
| `db76890` | Phase 4: CLI + README + profile-aware lint | 12 files, +819/-132 |

**Total:** 5 commits, 93 files changed, ~7000+ lines added

---

## 7. Validation Results

### Template Validation (lite profile)
- Created test project with `studio init -p lite`
- Ran `aeos_lint.py` → ALL CHECKS PASSED
- Verified profile-aware SKIP behavior for missing files

### CLI Validation
- `studio version` → AEOS Studio v0.1.0
- `studio init run /tmp/test -p lite` → Success, all files copied
- `studio status run /tmp/test` → Shows 0 artifacts, 7 agents configured
- `studio validate` → Lint passes, pytest skipped (no tests/)

### State Graph
- All 6 workflows updated with state graph references
- Feedback loops documented in each workflow
- State transition protocol created with ST-NNN format

---

## 8. Decisions Made During Session

| Decision | Rationale |
|----------|-----------|
| Evolve AEOS instead of building from scratch | AEOS v0.3 governance is solid and validated; rebuilding would waste months of work |
| State graph instead of pipeline | Real development has bidirectional feedback loops, not linear progression |
| Mixed models (sonnet-4 + haiku) | Cost optimization: expensive models only where strategic reasoning is needed |
| `.aegos/` prefix for template governance | Distinguish from AEOS Core's own governance; makes template project-agnostic |
| 3 governance profiles (Full/Standard/Lite) | Not all projects need full governance; lite for small projects reduces overhead |
| Python CLI with typer | Fast to build, good CLI ergonomics, easy to extend |
| Profile-aware lint (SKIP not FAIL) | Lite profile intentionally omits files; lint should not fail for intentional omissions |
| Never merge to master | Evolution branch stays separate; operator decides when/if to merge |

---

## 9. Open Questions / Pending Items

- [ ] Define specific model IDs per agent (currently using placeholder IDs)
- [ ] Design exact ADR format for template projects
- [ ] Define concrete governance rules (what each agent can/cannot do)
- [ ] Protocol for handoff between agents (how context is passed)
- [ ] Long context management strategy (compaction, summarization)
- [ ] CLI design for future commands (new-objective, new-task, handoff, update, migrate, add-agent)
- [ ] Validation in a real project of the operator
- [ ] "AEOS Lite" profile for very small projects
- [ ] Multi-project support (Phase 2 of AEOS)
- [ ] Dashboard for state graph visualization (Phase 6)
- [ ] Agent/skill registry (Phase 6)

---

## 10. Risks Identified

| Risk | Severity | Mitigation |
|------|----------|------------|
| Too much bureaucracy for small projects | MEDIUM | Lite governance profile with minimal files |
| Agents don't update memory | MEDIUM | Governance skill enforces memory updates as part of workflow |
| Context becomes stale | MEDIUM | state.md and context.md updated at each handoff |
| Token cost with 8 agents | MEDIUM | Mixed models already optimize cost; monitor and adjust |
| Adoption complexity | LOW | Template ready to copy, clear documentation, AGENTS.md as entry point |
| OpenCode integration doesn't work as expected | LOW | Agent definitions are markdown and portable; can adapt to other platforms |
| State graph too complex for simple projects | MEDIUM | Lite profile with simplified graph |

---

## 11. Principles Established

1. **Memory of the project lives in the project** — context lives in the repo, not in chats
2. **Markdown-first** — portable, git-native, auditable, readable by humans and models
3. **Explicit governance** — clear rules, not implicit
4. **State graph, not pipeline** — bidirectional cognitive loops
5. **Separated layers** — permanent governance, replaceable agents, replaceable executors
6. **Executor-agnostic** — works with OpenCode, Claude, Cursor, etc.
7. **Evolvable** — structure grows with the project
8. **Human governance** — no self-approval, critical changes require human approval
9. **No hidden memory** — all memory is explicit markdown files
10. **Repository state is truth** — always inspect current repo state before acting

---

## 12. Files Inventory

### Created (new files)
```
.opencode/opencode.json
.opencode/agents/director.md
.opencode/agents/architect.md
.opencode/agents/implementer.md
.opencode/agents/reviewer.md
.opencode/agents/auditor.md
.opencode/agents/qa.md
.opencode/agents/documentation.md
.opencode/skills/aeos-governance/SKILL.md
workflows/state_graph.md
protocols/STATE_TRANSITION_PROTOCOL.md
memory/state-log/.gitkeep
memory/decisions/ADR-004.md
template/ (61 files total)
cli/ (10 files total)
```

### Modified (existing files)
```
README.md — Updated to v0.4
workflows/feature_workflow.md — Added state graph integration
workflows/bugfix_workflow.md — Added state graph integration
workflows/architecture_change_workflow.md — Added state graph integration
workflows/audit_workflow.md — Added state graph integration
workflows/incident_workflow.md — Added state graph integration
workflows/research_workflow.md — Added state graph integration
scripts/aeos_lint.py — Made configurable and profile-aware (also copied to template/)
```

---

## 13. Next Steps

1. **Apply template to a real project** — Use `studio init` on one of Nicolas's existing projects
2. **Execute first operational cycle** — Create OBJ-001, follow state graph, produce all artifacts
3. **Document learnings** — Create OPR-001 in memory/research/
4. **Iterate** — Adjust governance, protocols, and templates based on real usage
5. **Phase transition to Phase 1** — When validation criteria are met (per PHASE_POLICY.md)

---

## 14. Audit Trail

| Timestamp | Action | Agent | Artifact |
|-----------|--------|-------|----------|
| 2026-05-20 | Session started | opencode (director) | This document |
| 2026-05-20 | Problem analysis | opencode + ChatGPT analysis | Strategic insight section |
| 2026-05-20 | Architecture decision | opencode (director) | ADR-004 |
| 2026-05-20 | Branch created | opencode | `feature/ai-engineering-studio-evolution` |
| 2026-05-20 | Phase 1 implemented | opencode | `.opencode/` directory (9 files) |
| 2026-05-20 | Phase 2 implemented | opencode | `workflows/state_graph.md`, `protocols/STATE_TRANSITION_PROTOCOL.md` |
| 2026-05-20 | Workflows updated | opencode + subagent | 6 workflow files |
| 2026-05-20 | Phase 3 implemented | opencode | `template/` directory (61 files) |
| 2026-05-20 | Template validated | opencode | ALL CHECKS PASSED on test project |
| 2026-05-20 | Phase 4 implemented | opencode | `cli/` directory (10 files) |
| 2026-05-20 | CLI validated | opencode | All commands tested successfully |
| 2026-05-20 | README updated | opencode | `README.md` v0.4 |
| 2026-05-20 | Session memory created | opencode | This document |

---

**End of Session Memory — SES-001**
