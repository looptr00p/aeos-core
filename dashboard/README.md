# AEOS Governance Dashboard

Read-only observability layer for AEOS Core governance state.

**Repository markdown is the source of truth.** The dashboard only visualizes what already exists.

## Quick Start

```bash
cd dashboard
npm install
npm run scan    # Generate aeos-state.json from repository
npm run dev     # Start local dev server (opens browser)
```

## Architecture

```
Repository markdown → scan-aeos-repo.mjs → generated/aeos-state.json → Dashboard (React)
```

- **No backend** — static files only
- **No database** — JSON generated from markdown
- **No auth** — local development only
- **No governance decisions** — read-only visualization
- **No autonomous logic** — deterministic scanner only

## State Classification

The dashboard is:

- **PROPOSED** before implementation
- **EXPERIMENTAL** once a working local prototype exists
- **IMPLEMENTED** only after dashboard files, scanner, setup instructions, and local execution are verified

## Scripts

| Command | Description |
|---------|-------------|
| `npm run scan` | Scan repository markdown and generate `aeos-state.json` |
| `npm run dev` | Start Vite dev server (opens browser automatically) |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build locally |

## Views

1. **Overview** — Governance counts, active/draft objectives, proposed ADRs, baseline info
2. **State Classification** — Documents grouped by IMPLEMENTED/EXPERIMENTAL/PROPOSED/STRATEGIC/UNLABELED
3. **Objectives** — All objectives with ID, title, status, state classification
4. **ADRs** — Architecture Decision Records with status and classification
5. **Governance** — Governance files, protocols, templates, workflows, agents
6. **Baseline** — Governance baseline version, metrics, recommended git tag
7. **Risks** — Operational risks extracted from baseline document
