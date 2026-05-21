# State Graph — AEOS Workflows

## Propósito

Los workflows de AEOS NO son pipelines lineales. Son grafos de estado con loops de feedback bidireccionales que reflejan la realidad del desarrollo de software.

## Nodos del Grafo

| Nodo | Agente Responsable | Entrada Requerida | Artifact de Salida |
|------|-------------------|-------------------|-------------------|
| `objective_defined` | director | Input del operador humano | OBJ-XXX |
| `architecture_reviewed` | architect | OBJ-XXX | ADR-XXX (si aplica) |
| `task_defined` | director | OBJ-XXX + ADR (si aplica) | TASK-XXX |
| `implementing` | implementer | TASK-XXX + scope definido | Código + validación |
| `reviewing` | reviewer | Código + TASK-XXX + HND-XXX | REV-XXX |
| `testing` | qa | Código + TASK-XXX | Resultados de tests |
| `auditing` | auditor | REV-XXX + resultados de tests | AUD-XXX |
| `documenting` | documentation | AUD-XXX pass | Memoria actualizada |
| `handoff_complete` | director | Todos los artifacts completos | HND-XXX |
| `closed` | director | HND-XXX | OBJ-XXX CLOSED |

## Estado Inicial

Todo ciclo operacional comienza en `objective_defined`. El operador humano proporciona el input inicial al director.

## Estado Final

Todo ciclo operacional termina en `closed` cuando:
- Todos los acceptance criteria del OBJ-XXX están cumplidos
- Todos los artifacts de trazabilidad existen (OBJ, TASK, ADR si aplica, REV, AUD, HND)
- `aeos_lint.py` pasa
- `pytest tests/` pasa
- El operador humano confirma cierre

## Edges — Transiciones Principales

### Flujo Forward

```
objective_defined → architecture_reviewed    (si hay cambio arquitectónico)
objective_defined → task_defined             (si no hay cambio arquitectónico)
architecture_reviewed → task_defined         (ADR creado o no necesario)
task_defined → implementing                  (TASK-XXX creado y asignado)
implementing → reviewing                     (código entregado con handoff)
reviewing → testing                          (review passed)
testing → auditing                           (tests passed)
auditing → documenting                       (audit passed)
documenting → handoff_complete               (memoria actualizada)
handoff_complete → closed                    (operador confirma)
```

## Edges — Loops de Feedback

### reviewing → implementing
**Trigger:** Reviewer encuentra issues en el código
**Condición:** REV-XXX resultado = REQUEST_CHANGES
**Acción:** Implementer corrige issues específicos referenciados en REV-XXX
**Re-entry:** implementing → reviewing (nuevo handoff requerido)

### testing → implementing
**Trigger:** QA encuentra bugs o tests fallan
**Condición:** Resultados de tests = FAIL
**Acción:** Implementer corrige bugs, agrega/actualiza tests
**Re-entry:** implementing → reviewing → testing

### testing → task_defined
**Trigger:** QA descubre que la spec es ambigua o insuficiente para testear
**Condición:** No se pueden definir tests claros contra acceptance criteria
**Acción:** Director delega a re-definir TASK-XXX con criterios más claros
**Re-entry:** task_defined → implementing → testing

### auditing → reviewing
**Trigger:** Auditor encuentra gaps en el review
**Condición:** AUD-XXX resultado = FAIL con gaps de review
**Acción:** Reviewer re-revisa con foco en los gaps identificados
**Re-entry:** reviewing → testing (si hay nuevos issues)

### auditing → objective_defined
**Trigger:** Auditor encuentra inconsistencia estratégica
**Condición:** El trabajo no se alinea con el OBJ-XXX o hay contradicción con ADRs existentes
**Acción:** Director re-alinea con el operador humano, posiblemente re-definir OBJ-XXX
**Re-entry:** objective_defined → ... (ciclo reinicia con nueva dirección)

### implementing → architecture_reviewed
**Trigger:** Implementer descubre constraint técnico no documentado
**Condición:** La implementación revela que la arquitectura actual es insuficiente o incorrecta
**Acción:** Director delega a architect para re-evaluar y crear/actualizar ADR
**Re-entry:** architecture_reviewed → task_defined → implementing

### implementing → task_defined
**Trigger:** Implementer descubre que el scope es insuficiente
**Condición:** No se puede cumplir acceptance criteria con el scope definido
**Acción:** Director delega a expandir TASK-XXX con nuevo scope
**Re-entry:** task_defined → implementing

### documenting → implementing
**Trigger:** Documentador descubre que la memoria no refleja lo implementado
**Condición:** Hay discrepancia entre código y documentación existente
**Acción:** Implementer provee contexto adicional para actualizar docs correctamente
**Re-entry:** implementing → documenting

## Edges — Escalaciones

Cualquier nodo puede escalar al director cuando:
- Ambigüedad que no se puede resolver con contexto existente
- Conflicto entre constraints
- Riesgo identificado que requiere decisión humana
- El agente no tiene permisos suficientes para continuar

El director escala al humano cuando:
- Cambio de dirección estratégica
- Aprobación de CRITICAL_SYSTEM_CHANGE
- Conflictos que no se resuelven entre agentes
- El operador lo solicita

## Registro de Transiciones

Cada transición se registra en `memory/state-log/ST-NNN.md`:

```markdown
# State Transition — ST-NNN

**Traceability ID:** ST-NNN
**From:** [estado origen]
**To:** [estado destino]
**Date:** YYYY-MM-DD
**Agent:** [agent-id]
**Task:** TASK-XXX
**Objective:** OBJ-XXX
**Trigger:** [qué causó la transición]
**Artifact:** [artifact producido]
**Result:** PASS → proceed / FAIL → loop back / ESCALATE → director
**Notes:** [contexto adicional]
```

## Reglas del Grafo

1. Cada transición debe producir un artifact
2. Cada transición debe ser validada antes de avanzar
3. Cada loop de feedback debe registrar la razón del retorno
4. Cada escalación debe seguir `protocols/ESCALATION_POLICY.md`
5. Ninguna transición puede ser skippeada
6. El estado del proyecto es la suma de todos los artifacts en `memory/`
7. No hay estado oculto — todo es visible en el repo
