---
name: aeos-governance
description: Use when working within AEOS Core to enforce governance rules, protocols, and memory management. Triggers on any task that involves creating, modifying, or reviewing AEOS artifacts, agents, or project work.
---

# AEOS Governance Skill

## Reglas de Oro

1. **Repository state is truth** — siempre inspecciona el estado actual del repo antes de actuar
2. **No hidden memory** — toda memoria vive en `memory/`, nada implícito
3. **No self-approval** — ningún agente aprueba su propio trabajo
4. **Human governance** — cambios críticos requieren aprobación humana
5. **Markdown-first** — todo es markdown, versionado en git, auditable

## Protocolos Obligatorios

| Protocol | Cuándo aplica | Archivo |
|----------|--------------|---------|
| Handoff | Al completar cualquier tarea | `protocols/HANDOFF_PROTOCOL.md` |
| Memory | Al actualizar memoria | `protocols/MEMORY_PROTOCOL.md` |
| Review | Antes de cerrar cualquier trabajo | `protocols/REVIEW_PROTOCOL.md` |
| ADR | Para decisiones arquitectónicas | `protocols/ADR_PROTOCOL.md` |
| Task | Al crear/modificar tareas | `protocols/TASK_PROTOCOL.md` |
| Context | Al pasar contexto entre agentes | `protocols/CONTEXT_PROTOCOL.md` |
| Incident | Cuando hay incidentes | `protocols/INCIDENT_PROTOCOL.md` |

## Trazabilidad

Todo artifact debe referenciar:
- Un objetivo: `OBJ-NNN`
- Una tarea: `TASK-NNN`
- Un handoff: `HND-NNN`

IDs válidos: `OBJ`, `ADR`, `TASK`, `REV`, `AUD`, `HND`, `INC`, `ESC`

## Permisos por Agente

| Agente | Permiso | Puede hacer |
|--------|---------|-------------|
| director | Full | Todo, coordina |
| architect | LIMITED_IMPLEMENTATION | ADRs, docs arquitectónicos |
| implementer | LIMITED_IMPLEMENTATION | Código dentro de scope |
| reviewer | READ_ONLY + DOCS | Reviews, docs de review |
| auditor | READ_ONLY + DOCS | Audits, docs de audit |
| qa | TESTS_ONLY | Tests, ejecución de tests |
| documentation | DOCS_ONLY | Docs, memoria |

## Validación Obligatoria

Antes de cerrar cualquier ciclo operacional:

```bash
python3 scripts/aeos_lint.py
pytest tests/
```

## Seguridad

Violaciones de `governance/SAFETY_RULES.md` son CRITICAL:
- No autonomous execution sin task assignment
- No self-approval
- No hidden memory
- No unrestricted write access
- No CI weakening
- No deletion of audit trails

## Escalación

Escalar al director (y al humano si es CRITICAL) cuando:
- Requisitos unclear
- Documentación conflictiva
- Criterios de aceptación missing
- Permisos insuficientes
- Governance violation detected

## State Graph (No Pipeline)

El trabajo fluye como grafo con loops, no como línea:

```
director → architect → implementer → reviewer → qa → auditor → documentation → director
                ↑          ↑            ↑         ↑       ↑
                │          └────────────┘         │       │
                └─────────────────────────────────┘       │
                        feedback loops                     │
                                                          │
                        escalaciones ←────────────────────┘
```

## Fase Actual

AEOS Core está en **Phase 0: Governance/Bootstrap**. Ver `governance/PHASE_POLICY.md`.
