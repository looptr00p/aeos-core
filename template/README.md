# AEOS Template — AI Engineering Operating System

This is a reusable AEOS template for AI-governed software projects.

## What is AEOS?

AEOS (AI Engineering Operating System) is a governance-first framework for building software with multiple AI agents. It preserves strategic and operational continuity while multiple intelligences (human and artificial) participate in a project.

**AEOS is not run. It is operated.** Each operational session follows the same pattern: define an objective, create tasks, produce artifacts, validate with lint, review, audit, and close with a handoff.

## Quick Start

### 1. Copy template to your project

```bash
cp -r path/to/aeos-core/template/.aegos ./
cp -r path/to/aeos-core/template/.opencode ./
cp -r path/to/aeos-core/template/memory ./
cp path/to/aeos-core/template/scripts/aeos_lint.py ./scripts/
cp path/to/aeos-core/template/AGENTS.md ./
cp path/to/aeos-core/template/project-charter.md ./
```

### 2. Fill in your project charter

Edit `project-charter.md` with your project's vision, stack, constraints, and agent configuration.

### 3. Validate

```bash
pip install pyyaml
python3 scripts/aeos_lint.py
```

### 4. Start operating

1. Create an objective: copy `templates/objective_template.md` to `memory/objectives/OBJ-001.md`
2. Fill in the objective with your first goal
3. Start an OpenCode session — the director agent will guide you through the workflow

## Repository Structure

```
project/
├── .aegos/                          # AEOS governance framework
│   ├── governance/                  # Rules, permissions, safety rules
│   ├── protocols/                   # How work is done
│   ├── workflows/                   # End-to-end process definitions (state graph)
│   └── templates/                   # Reusable artifact templates
├── .opencode/                       # OpenCode configuration
│   ├── opencode.json                # Agent definitions and models
│   ├── agents/                      # Agent prompt files
│   └── skills/                      # OpenCode skills (aeos-governance)
├── memory/                          # Project memory (all operational artifacts)
│   ├── objectives/                  # OBJ-XXX files
│   ├── tasks/                       # TASK-XXX files
│   ├── decisions/                   # ADR-XXX files
│   ├── handoffs/                    # HND-XXX files
│   ├── reviews/                     # REV-XXX files
│   ├── audits/                      # AUD-XXX files
│   ├── incidents/                   # INC-XXX / ESC-XXX files
│   ├── state-log/                   # ST-XXX files (state transitions)
│   └── ...
├── scripts/
│   └── aeos_lint.py                 # Governance validation
├── AGENTS.md                        # Universal agent constraints
└── project-charter.md               # Project-specific configuration
```

## Governance Profile

Choose a governance profile based on your project size:

| Profile | Governance Files | Protocols | Workflows | Best For |
|---------|-----------------|-----------|-----------|----------|
| **Full** | All 8 files | All 8 protocols | All 6 workflows | Complex projects, multiple agents |
| **Standard** | Core 5 files | Core 5 protocols | 3 main workflows | Most projects |
| **Lite** | 3 essential files | 3 essential protocols | 1 workflow | Small projects, single feature |

### Standard Profile (Recommended)

Keep these files, remove the rest:

**Governance:**
- `AGENTS.md`
- `PERMISSION_MODEL.md`
- `SAFETY_RULES.md`
- `ESCALATION_POLICY.md`
- `GOVERNANCE_SEVERITY_MODEL.md`

**Protocols:**
- `HANDOFF_PROTOCOL.md`
- `MEMORY_PROTOCOL.md`
- `REVIEW_PROTOCOL.md`
- `TASK_PROTOCOL.md`
- `ADR_PROTOCOL.md`

**Workflows:**
- `feature_workflow.md`
- `bugfix_workflow.md`
- `state_graph.md`

### Lite Profile

Keep only:

**Governance:**
- `AGENTS.md`
- `SAFETY_RULES.md`
- `ESCALATION_POLICY.md`

**Protocols:**
- `HANDOFF_PROTOCOL.md`
- `MEMORY_PROTOCOL.md`
- `TASK_PROTOCOL.md`

**Workflows:**
- `feature_workflow.md`

## Operational Session

Each session follows:

```
sync → validate → observe → operate
```

1. **Sync:** `git pull`
2. **Validate:** `python3 scripts/aeos_lint.py`
3. **Operate:** Start OpenCode session, define objective, follow workflow

## State Graph

Workflows are NOT linear pipelines. They are state graphs with feedback loops:

```
director → architect → implementer → reviewer → qa → auditor → documentation → director
                ↑          ↑            ↑         ↑       ↑
                │          └────────────┘         │       │
                └─────────────────────────────────┘       │
                        feedback loops                     │
                                                          │
                        escalations ←────────────────────┘
```

See `.aegos/workflows/state_graph.md` for the complete graph.

## Key Principles

1. **Repository state is truth** — everything lives in the repo
2. **No hidden memory** — all memory is explicit markdown files
3. **No self-approval** — agents never approve their own work
4. **Human governance** — critical changes require human approval
5. **Markdown-first** — portable, git-native, auditable
6. **State graph, not pipeline** — real development has loops

## Validation

```bash
# Governance validation
python3 scripts/aeos_lint.py

# If you have tests
pytest tests/
```

## Updating AEOS

When a new AEOS template version is available:

1. Review the changelog in the AEOS core repo
2. Copy new/updated files to your project
3. Run `aeos_lint.py` to validate
4. Update `project-charter.md` if governance profile changed

## License

[Your license here]
