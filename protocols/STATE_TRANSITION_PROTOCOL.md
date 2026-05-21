# State Transition Protocol

## Propósito

Definir cómo se registran, validan y gestionan las transiciones de estado en el grafo de workflows de AEOS.

## Qué es una Transición

Una transición es el movimiento de un nodo del grafo de estado a otro. Cada transición:
- Tiene un estado origen y un estado destino
- Es ejecutada por un agente específico
- Produce al menos un artifact
- Debe ser validada antes de considerar completada
- Debe ser registrada en `memory/state-log/`

## Registro de Transiciones

### Ubicación

Todas las transiciones se registran en `memory/state-log/ST-NNN.md`

### Formato

```markdown
# State Transition — ST-NNN

**Traceability ID:** ST-NNN
**From:** [estado origen del grafo]
**To:** [estado destino del grafo]
**Date:** YYYY-MM-DD
**Agent:** [agent-id]
**Task:** TASK-XXX
**Objective:** OBJ-XXX
**Trigger:** [qué causó esta transición]
**Artifact:** [qué artifact se produjo]
**Result:** PASS | FAIL | ESCALATE
**Notes:** [contexto adicional, decisiones, riesgos]
```

### Asignación de IDs

Los IDs de transición siguen el formato `ST-NNN` (ST-001, ST-002, etc.) y son secuenciales.

## Validación de Transiciones

### Forward Transitions (avance en el grafo)

Antes de avanzar al siguiente nodo:
1. El artifact requerido existe y está completo
2. El artifact pasa validación (review, tests, audit según corresponda)
3. La trazabilidad es correcta (referencia TASK-XXX y OBJ-XXX)
4. No hay governance violations

### Feedback Loop Transitions (retorno en el grafo)

Antes de retornar a un nodo anterior:
1. La razón del retorno está documentada en el artifact de review/test/audit
2. Los issues específicos están identificados con referencia a archivos/líneas
3. El agente destino entiende qué debe corregir
4. Se produce un nuevo handoff con el feedback

### Escalation Transitions (escalación al director)

Antes de escalar:
1. El agente ha intentado resolver con contexto disponible
2. La ambigüedad/conflicto/riesgo está documentado
3. Se referencia el TASK-XXX y el nodo actual
4. Se sugiere acción al director

## Reglas de Transición

1. **No skip:** Ninguna transición puede ser saltada. Cada nodo del grafo debe ser visitado.
2. **No auto-approve:** Ningún agente puede validar su propia transición.
3. **Artifact required:** Cada transición debe producir al menos un artifact.
4. **Traceability required:** Cada transición debe referenciar TASK-XXX y OBJ-XXX.
5. **Log required:** Cada transición debe registrarse en `memory/state-log/`.
6. **Validation required:** Cada transición forward debe pasar validación antes de avanzar.

## Transiciones por Nodo

### objective_defined → architecture_reviewed
- **Agente:** director → architect
- **Trigger:** El objetivo implica cambio arquitectónico
- **Artifact:** Delegación a architect con contexto
- **Validación:** Architect confirma que hay cambio arquitectónico

### objective_defined → task_defined
- **Agente:** director
- **Trigger:** No hay cambio arquitectónico
- **Artifact:** TASK-XXX creado
- **Validación:** TASK-XXX tiene acceptance criteria claros

### architecture_reviewed → task_defined
- **Agente:** director
- **Trigger:** ADR creado o architect confirma que no hay cambio
- **Artifact:** TASK-XXX + ADR-XXX (si aplica)
- **Validación:** TASK-XXX incorpora decisiones del ADR

### task_defined → implementing
- **Agente:** director → implementer
- **Trigger:** TASK-XXX creado y asignado
- **Artifact:** Delegación a implementer con scope
- **Validación:** Implementer confirma scope entendido

### implementing → reviewing
- **Agente:** implementer → reviewer
- **Trigger:** Código implementado y validado por implementer
- **Artifact:** HND-XXX del implementer
- **Validación:** HND-XXX completo y correcto

### reviewing → testing
- **Agente:** reviewer → qa
- **Trigger:** Review passed (REV-XXX = APPROVE)
- **Artifact:** REV-XXX
- **Validación:** REV-XXX no tiene issues blocking

### testing → auditing
- **Agente:** qa → auditor
- **Trigger:** Tests passed
- **Artifact:** Resultados de tests
- **Validación:** Todos los tests relevantes pasan

### auditing → documenting
- **Agente:** auditor → documentation
- **Trigger:** Audit passed (AUD-XXX = PASS)
- **Artifact:** AUD-XXX
- **Validación:** AUD-XXX no tiene violations

### documenting → handoff_complete
- **Agente:** documentation → director
- **Trigger:** Memoria actualizada
- **Artifact:** Confirmación de memoria actualizada
- **Validación:** `aeos_lint.py` pasa

### handoff_complete → closed
- **Agente:** director
- **Trigger:** Operador humano confirma cierre
- **Artifact:** OBJ-XXX status = CLOSED
- **Validación:** Todos los acceptance criteria cumplidos

## Loops de Feedback — Transiciones de Retorno

### reviewing → implementing
- **Trigger:** REV-XXX = REQUEST_CHANGES
- **Re-entry:** implementing → reviewing (nuevo HND-XXX requerido)
- **Límite:** Si 3 loops sin resolución → escalar al director

### testing → implementing
- **Trigger:** Tests = FAIL
- **Re-entry:** implementing → reviewing → testing
- **Límite:** Si 3 loops sin resolución → escalar al director

### testing → task_defined
- **Trigger:** Spec ambigua para testear
- **Re-entry:** task_defined → implementing → testing
- **Límite:** Si spec no se puede clarificar → escalar al operador

### auditing → reviewing
- **Trigger:** AUD-XXX = FAIL con gaps de review
- **Re-entry:** reviewing → testing (si hay nuevos issues)
- **Límite:** Si gaps son de gobernanza → escalar al director

### auditing → objective_defined
- **Trigger:** Inconsistencia estratégica
- **Re-entry:** objective_defined → ... (ciclo reinicia)
- **Límite:** Siempre requiere aprobación del operador humano

### implementing → architecture_reviewed
- **Trigger:** Constraint técnico descubierto
- **Re-entry:** architecture_reviewed → task_defined → implementing
- **Límite:** Si architect confirma que no hay cambio → implementar workaround

### implementing → task_defined
- **Trigger:** Scope insuficiente
- **Re-entry:** task_defined → implementing
- **Límite:** Si scope no se puede expandir → escalar al operador

## Métricas de Transiciones

El director debe monitorear:
- **Velocidad:** tiempo promedio por transición
- **Loop rate:** frecuencia de loops de feedback
- **Escalation rate:** frecuencia de escalaciones
- **Blockers:** transiciones que no avanzan
- **Re-trabajo:** transiciones que retornan más de 2 veces

Estas métricas se registran en `memory/research/OPR-NNN.md` periódicamente.
