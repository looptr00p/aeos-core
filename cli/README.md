# AEOS Studio CLI

CLI tool for bootstrapping, managing, and auditing AEOS-governed projects.

## Installation

```bash
cd cli
pip install -e .
```

## Commands

### `studio init`

Bootstrap AEOS in a new or existing project.

```bash
studio init                          # Use standard profile in current directory
studio init /path/to/project         # Use standard profile in specific directory
studio init -p full                  # Full governance profile
studio init -p lite                  # Lite governance profile
studio init --force                  # Overwrite existing AEOS files
```

### `studio status`

Show the current state of an AEOS-governed project.

```bash
studio status                        # Show status for current directory
studio status /path/to/project       # Show status for specific directory
```

Shows: objectives, tasks, ADRs, incidents, state transitions, artifact counts, and agent configuration.

### `studio audit`

Run a full governance audit including lint and traceability checks.

```bash
studio audit                         # Audit current directory
studio audit /path/to/project        # Audit specific directory
```

### `studio validate`

Run governance lint and optionally pytest.

```bash
studio validate                      # Lint + tests (if tests/ exists)
studio validate --no-tests           # Lint only
```

### `studio version`

Show AEOS Studio version.

```bash
studio version
```

## Governance Profiles

| Profile | Governance Files | Protocols | Workflows | Best For |
|---------|-----------------|-----------|-----------|----------|
| **full** | All 8 files | All 8 protocols | All 7 workflows | Complex projects |
| **standard** | 5 core files | 6 essential protocols | 3 main workflows | Most projects (default) |
| **lite** | 3 essential files | 3 basic protocols | 1 workflow | Small projects |

## Architecture

```
cli/
├── pyproject.toml
├── src/
│   └── studio/
│       ├── __init__.py
│       ├── cli.py                    # Typer entry point
│       ├── commands/
│       │   ├── __init__.py
│       │   ├── init.py               # studio init
│       │   ├── status.py             # studio status
│       │   ├── audit.py              # studio audit
│       │   └── validate.py           # studio validate
│       ├── core/                     # Shared utilities (future)
│       └── templates/                # Jinja2 templates (future)
└── tests/
```
