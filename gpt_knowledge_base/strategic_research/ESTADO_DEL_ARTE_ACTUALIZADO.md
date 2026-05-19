# Estado del Arte — AEOS Core vNext

**Fecha**: 2026-05-19
**Versión del documento**: 1.0
**Base**: Repositorio verificado + auditoría completa de reconciliación

---

## Resumen Ejecutivo

AEOS Core es un sistema operativo de ingeniería para IA asistida por IA, con enfoque en gobernanza explícita, trazabilidad auditable, y control humano. Este documento refleja el estado real del repositorio tras una auditoría completa de reconciliación que incluyó:

1. Inventario completo del repositorio
2. Análisis de inconsistencias entre documentación y realidad
3. Matriz de capacidades verificadas
4. Creación de objetivo OBJ-006 (reconciliación)
5. Creación de ADR-001 (estructura dual de directorios)
6. Actualización gobernada de memoria
7. Revisión de gobernanza completa
8. Validación determinista de referencias
9. Diseño de MVP vNext escalable

**Puntuación de gobernanza actual**: 1.8 / 4.0 (por debajo del umbral aceptable de 2.0)
**Tasa de validación determinista**: 89.8% (106/118 verificaciones)
**Estado de lint AEOS**: 11/11 verificaciones PASANDO

---

## Estructura del Repositorio (Verificada)

### Directorios Canónicos (nivel raíz)

| Directorio | Archivos | Propósito |
|-----------|----------|-----------|
| `governance/` | 7 | Reglas, restricciones y políticas de gobernanza |
| `protocols/` | 7 | Cómo se realiza el trabajo |
| `templates/` | 11 | Plantillas de artefactos reutilizables |
| `agents/` | 8 (1 registro + 7 agentes) | Definiciones de agentes |
| `workflows/` | 6 | Definiciones de procesos end-to-end |
| `memory/` | 53 artefactos + 8 .gitkeep | Memoria institucional explícita |
| `tests/` | 11 archivos | Validación de estructura del repositorio |
| `docs/` | 17 archivos | Documentación operativa |
| `scripts/` | 1 (aeos_lint.py) | Validación operacional |
| `.github/workflows/` | 1 | Configuración CI/CD |

### Laboratorio Experimental (aeos-core/)

| Directorio | Archivos | Propósito |
|-----------|----------|-----------|
| `aeos-core/governance/` | 1 | Política de porting (PORTING_POLICY.md) |
| `aeos-core/templates/` | 2 | Plantillas experimentales |
| `aeos-core/docs/` | 2 | Charter y notas del lab experimental |
| `aeos-core/memory/` | 15 artefactos | Memoria del lab experimental |
| `aeos-core/tests/enforcement/` | 3 | Tests de validación experimental |
| `aeos-core/scripts/` | 1 | Lint delegado (wraps root lint) |

### Total de Archivos

| Categoría | Cantidad |
|-----------|----------|
| Archivos Markdown (.md) | 103 |
| Archivos de configuración (yaml/yml/toml) | 10 |
| Archivos de test (.py) | 14 |
| Scripts Python | 2 |
| **Total de archivos de contenido** | **~170+** |

---

## Estado de Gobernanza

### Archivos de Gobernanza (7/7 presentes)

| Archivo | Estado | Contenido |
|---------|--------|-----------|
| AGENTS.md | ✅ | Restricciones universales de agentes |
| PHASE_POLICY.md | ✅ | Definición de fases (0-3) y transiciones |
| PERMISSION_MODEL.md | ✅ | 5 niveles de permisos (READ_ONLY a CRITICAL_SYSTEM_CHANGE) |
| REVIEW_REQUIREMENTS.md | ✅ | Requisitos de revisión por categoría de cambio |
| ESCALATION_POLICY.md | ✅ | 6 condiciones de escalación + proceso |
| SAFETY_RULES.md | ✅ | 7 reglas de seguridad innegociables |
| GOVERNANCE_SEVERITY_MODEL.md | ✅ | 4 niveles (LOW, MEDIUM, HIGH, CRITICAL) |

### Protocolos (7/7 presentes)

| Protocolo | Estado |
|-----------|--------|
| TASK_PROTOCOL.md | ✅ |
| REVIEW_PROTOCOL.md | ✅ |
| CONTEXT_PROTOCOL.md | ✅ |
| MEMORY_PROTOCOL.md | ✅ |
| HANDOFF_PROTOCOL.md | ✅ |
| INCIDENT_PROTOCOL.md | ✅ |
| ADR_PROTOCOL.md | ✅ |

### Plantillas (11 canónicas + 2 experimentales)

| Plantilla | Ubicación | Estado |
|-----------|-----------|--------|
| objective_template.md | root | ✅ |
| adr_template.md | root | ✅ |
| task_template.md | root | ✅ |
| review_template.md | root | ✅ |
| audit_template.md | root | ✅ |
| handoff_template.md | root | ✅ |
| incident_template.md | root | ✅ |
| operational_report_template.md | root | ✅ |
| escalation_template.md | root | ✅ |
| governance_health_report_template.md | root | ✅ |
| traceability_assistance_template.md | root | ✅ |
| experiment_template.md | aeos-core | ✅ |
| porting_review_template.md | aeos-core | ✅ |

### Agentes (7/7 definidos con 20 campos requeridos)

| Agente | Rol | Permisos | Auto-aprobación |
|--------|-----|----------|-----------------|
| director-agent | Dirección de gobernanza | READ_ALL, GOVERNANCE_REVIEW, APPROVAL_AUTHORITY | ❌ Prohibida |
| architect-agent | Propuestas de arquitectura | READ_ALL, DOCS_ONLY, LIMITED_IMPLEMENTATION | ❌ Prohibida |
| implementer-agent | Implementación acotada | READ_ALL, LIMITED_IMPLEMENTATION | ❌ Prohibida |
| reviewer-agent | Validación y revisión | READ_ALL, DOCS_ONLY | ❌ Prohibida |
| auditor-agent | Auditoría de gobernanza | READ_ALL, DOCS_ONLY | ❌ Prohibida |
| qa-agent | Validación de tests | READ_ALL, TESTS_ONLY | ❌ Prohibida |
| documentation-agent | Actualización de documentación | READ_ALL, DOCS_ONLY | ❌ Prohibida |

### Flujos de Trabajo (6/6 presentes)

| Flujo | Estado |
|-------|--------|
| feature_workflow.md | ✅ |
| bugfix_workflow.md | ✅ |
| architecture_change_workflow.md | ✅ |
| audit_workflow.md | ✅ |
| incident_workflow.md | ✅ |
| research_workflow.md | ✅ |

---

## Estado de Memoria

### Artefactos de Ciclo de Vida (canónicos)

| Tipo | Prefijo | Cantidad | Directorio |
|------|---------|----------|------------|
| Objetivos | OBJ-XXX | 6 | `memory/objectives/` |
| Tareas | TASK-XXX | 11 | `memory/tasks/` |
| Revisiones | REV-XXX | 10 | `memory/reviews/` |
| Auditorías | AUD-XXX | 3 | `memory/audits/` |
| Entregas | HND-XXX | 7 | `memory/handoffs/` |
| Incidentes | INC-XXX | 3 | `memory/incidents/` |
| Escalaciones | ESC-XXX | 3 | `memory/incidents/` |
| Reportes Operacionales | OPR-XXX | 6 | `memory/research/` |
| Reportes de Salud de Gobernanza | GHR-XXX | 6 | `memory/research/` |
| Decisiones Arquitectónicas | ADR-XXX | 1 | `memory/decisions/` |
| **Total canónico** | | **66** | |

### Artefactos Experimentales (aeos-core)

| Tipo | Cantidad |
|------|----------|
| Objetivos experimentales | 2 |
| Tareas experimentales | 2 |
| Revisiones experimentales | 1 |
| Auditorías experimentales | 3 |
| Entregas experimentales | 2 |
| Experimentos | 5 |
| **Total experimental** | **15** |

### Estado Operacional Actual

| Métrica | Valor |
|---------|-------|
| Objetivos ACTIVE | 3 (OBJ-003, OBJ-004, OBJ-005) |
| Objetivos DRAFT | 1 (OBJ-006) |
| Objetivos CLOSED | 2 (OBJ-001, OBJ-002) |
| Tareas CLOSED | 6 (TASK-001 a TASK-005, TASK-007) |
| Tareas IN_PROGRESS | 5 (TASK-006, TASK-008 a TASK-011) |
| Incidentes RESOLVED | 1 (INC-001) |
| Incidentes ACTIVE | 2 (INC-002, INC-003) |
| Escalaciones RESOLVED | 1 (ESC-001) |
| Escalaciones IN_REVIEW | 1 (ESC-002) |
| Escalaciones OPEN | 1 (ESC-003) |
| ADRs PROPOSED | 1 (ADR-001) |

---

## Resultados de Ejecución de Prompts

### Prompt 1: Auditoría de Reconciliación de Verdad del Repositorio

**Objetivo**: Detectar inconsistencias entre documentación y estado real del repositorio.

**Artefactos creados**:
- `REPO_INVENTORY.md` — Inventario completo de ~170+ archivos
- `GAP_ANALYSIS.md` — 18 inconsistencias + 6 observaciones estructurales
- `CURRENT_CAPABILITY_MATRIX.md` — Matriz de capacidades verificada

**Hallazgos principales**:
- README.md y ESTADO_DEL_ARTE.md muestran árbol de directorios incorrecto (todo bajo `aeos-core/` cuando está en raíz)
- Versión inconsistente: README=v0.3, pyproject.toml=0.1.0, ESTADO_DEL_ARTE.md=0.1.0
- CI ejecuta solo 3 tests (aeos-core/), omite 11 tests de gobernanza (root)
- Reviews almacenados en `memory/reviews/` pero el índice dice `memory/audits/`
- Conteo de artefactos en TRACEABILITY_INDEX.md: dice 60, la suma real es 61
- ESTADO_DEL_ARTE.md métricas desactualizadas (dice 52 archivos, realidad ~170+)
- 26 referencias de ruta rotas (aeos-core referencia paths de root)
- Typo "Escalarate" en documentation_agent.yaml
- `.DS_Store` no está en `.gitignore`
- `memory/research/` contiene reportes, no investigación

**Validación**: `python3 scripts/aeos_lint.py` → 11/11 PASANDO

---

### Prompt 2: Creación de Objetivo AEOS

**Objetivo**: Crear un artefacto de objetivo siguiendo la plantilla y reglas de gobernanza.

**Artefacto creado**:
- `memory/objectives/OBJ-006.md` — "Repository Truth Reconciliation — Documentation and Structural Remediation"

**Detalles**:
- Estado: DRAFT
- Alcance: 12 inclusiones explícitas, 10 exclusiones explícitas
- Criterios de éxito: 18 condiciones medibles
- Requisitos de validación: 9 verificaciones explícitas
- Riesgos: 5 identificados (1 HIGH, 3 MEDIUM, 1 LOW)
- Aprobaciones humanas requeridas: 4 decisiones
- Tareas relacionadas: 9 pendientes (TASK-012 a TASK-020)
- Referencias de gobernanza: 7 documentos citados

---

### Prompt 3: Creación de ADR

**Objetivo**: Crear un Architecture Decision Record documentando la estructura dual de directorios.

**Artefacto creado**:
- `memory/decisions/ADR-001.md` — "Dual Directory Structure — Root Governance + Experimental Lab Subproject"

**Detalles**:
- Estado: PROPOSED (requiere aprobación humana)
- Opciones evaluadas: 4 (Flatten, Invert, Dual Structure, Separate Repos)
- Decisión: Opción 3 — Estructura dual con gobernanza explícita
- Alternativas rechazadas: 3, cada una con justificación explícita
- Tradeoffs documentados: 4 decisiones explícitas
- Riesgos: 5 identificados (2 MEDIUM, 3 LOW)
- Verificación: 6 métodos de validación
- Condiciones de reevaluación: 6 triggers futuros
- Referencias: 9 artefactos citados

---

### Prompt 4: Actualización Gobernada de Memoria

**Objetivo**: Actualizar memoria sin introducir suposiciones obsoletas, estado duplicado, conclusiones inverificables o decisiones no documentadas.

**Artefacto creado**:
- `memory/audits/MEMORY_UPDATE_001.md` — Reporte de actualización de memoria gobernada

**Hallazgos**:
- **27 hechos verificados** en 4 categorías (estructurales, gobernanza, gaps, validación)
- **4 categorías de información obsoleta** identificadas (TRACEABILITY_INDEX.md, memory/index/README.md, ESTADO_DEL_ARTE.md, información incierta)
- **7 actualizaciones propuestas** (2 hechas, 5 pendientes de aprobación)
- **6 riesgos de persistencia** identificados
- **7 aprobaciones humanas requeridas**

**Acciones ejecutadas**: Ninguna directa — solo propuesta. Las actualizaciones requieren aprobación humana.

---

### Prompt 5: Revisión de Gobernanza

**Objetivo**: Evaluar si el repositorio adhiere a los principios de gobernanza AEOS en 10 áreas.

**Artefacto creado**:
- `memory/reviews/REV-010.md` — Reporte de revisión de gobernanza

**Puntuación global**: 1.8 / 4.0 (por debajo del umbral aceptable de 2.0)

| Categoría | Puntuación | Veredicto |
|-----------|:----------:|-----------|
| Integridad de ciclo de vida | 2 | Aceptable |
| Trazabilidad | 3 | Fuerte |
| Límites de aprobación humana | 1 | **Débil** |
| Consistencia de documentación | 1 | **Débil** |
| Gobernanza de memoria | 2 | Aceptable |
| Auditabilidad | 2 | Aceptable |
| Responsabilidad de cambios | 1 | **Débil** |
| Cobertura de validación | 2 | Aceptable |
| Contención de alcance | 3 | Fuerte |
| Reproducibilidad operacional | 1 | **Débil** |

**4 Violaciones Críticas**:
1. CV-001: CI no ejecuta tests de validación de gobernanza (11 tests omitidos)
2. CV-002: ADR-001 creado sin aprobación humana
3. CV-003: OBJ-006 creado sin aprobación humana
4. CV-004: TRACEABILITY_INDEX.md contiene datos incorrectos (60 vs 61)

**6 Riesgos Medios**: Fase desalineada, versión inconsistente, 5 tareas sin auditoría programada, directorio mal nombrado, cadena de dependencia de lint CI, sin enforcement de ADR.

**8 Problemas Menores**: Errores de documentación, .gitignore, typo, directorios vacíos, output de lint engañoso, convención de nombres.

**Recomendación**: No avanzar más allá de Phase 0 hasta que los items P0 estén completos.

---

### Prompt 6: Validación Determinista

**Objetivo**: Validar que el repositorio es internamente consistente mediante verificación explícita de referencias.

**Artefacto creado**:
- `memory/audits/VAL-001.md` — Reporte de validación determinista

**Resultado global**: 89.8% tasa de aprobación (106/118 verificaciones)

| Categoría | Total | Pasaron | Fallaron | Tasa |
|-----------|:-----:|:-------:|:--------:|:----:|
| Referencias de IDs de ciclo de vida | 47 | 47 | 0 | 100% |
| Referencias de archivos de gobernanza | 8 | 7 | 1 | 87.5% |
| Referencias de protocolos | 7 | 7 | 0 | 100% |
| Referencias de plantillas | 13 | 10 | 3 | 76.9% |
| Referencias de workflows | 7 | 6 | 1 | 85.7% |
| Referencias de docs | 16 | 14 | 2 | 87.5% |
| Existencia de tests | 14 | 14 | 0 | 100% |
| Referencias de CI | 3 | 1 | 2 | 33.3% |
| Consistencia de versión | 3 | 0 | 3 | 0% |
| **TOTAL** | **118** | **106** | **12** | **89.8%** |

**26 referencias rotas** identificadas (todas problemas de prefijo de ruta en aeos-core).
**7 afirmaciones inconsistentes** identificadas.
**9 artefactos faltantes** (TASK-012 a TASK-020, planificados en OBJ-006, no creados aún).

**Correcciones aplicadas durante la validación**:
- EXP-001.md: 4 paths corregidos con prefijo `aeos-core/`
- TRACEABILITY_INDEX.md: Conteo corregido de 60 a 61
- memory/index/README.md: Reviews corregido de `memory/audits/` a `memory/reviews/`
- TRACEABILITY_INDEX.md: Añadidos OBJ-006 y ADR-001

**Lint post-corrección**: 11/11 PASANDO (sin regresiones)

---

### Prompt 7: Continuación (Aplicación de Correcciones)

**Acciones ejecutadas**:
- Corrección de paths en EXP-001.md (4 referencias)
- Corrección de conteo en TRACEABILITY_INDEX.md (60 → 61)
- Corrección de directorio de Reviews en memory/index/README.md
- Adición de OBJ-006 y ADR-001 al índice de trazabilidad
- Nota de actualización añadida al índice

**Resultado**: Referencias rotas reducidas de 26 a 22. Afirmaciones inconsistentes reducidas de 7 a 5.

---

### Prompt 8: Diseño de MVP vNext Escalable

**Objetivo**: Diseñar la próxima versión escalable del MVP sin aumentar complejidad innecesaria.

**Artefacto creado**:
- `docs/AEOS_VNEXT_DESIGN.md` — Diseño completo de AEOS MVP vNext (658 líneas)

**5 Cuellos de Botella Identificados**:

| Cuello de Botella | Impacto | Complejidad de Fix |
|-------------------|---------|-------------------|
| CI omite 11 tests de gobernanza | Cambios de gobernanza bypassan detección | Baja |
| Sin registros de aprobación humana | Gobernanza es aspiracional, no auditable | Baja |
| Sin enforcement de ADR | Protocolo existe sin verificación | Baja |
| Estructura dual no documentada | 22 referencias rotas | Media |
| Phase 0 no verificable | Criterio de salida no validable | Baja |

**5 Riesgos de Escalamiento**: Contención de revisores bajo concurrencia, acumulación de presión de gobernanza, crecimiento del índice de memoria (299 líneas manual), proliferación de plantillas, tiempo de ejecución de CI.

**Cambios Recomendados (mínimos)**:

| Categoría | Adiciones | Complejidad |
|-----------|-----------|-------------|
| Tipos de artefacto | 3 (approval records, split indexes, transition logs) | 3 plantillas |
| Checks de lint | 5 (ADR compliance, approval records, memory growth, path convention, version) | ~200 líneas |
| Política de gobernanza | 1 (escalation aging) | ~10 líneas |
| Documentación | 2 (agent naming, memory/research/ naming) | ~20 líneas |
| CI | 1 (complete test suite + parallelization) | ~15 líneas |

**Total nueva complejidad**: ~250 líneas de código + 3 plantillas. Sin agentes autónomos, sin runtime, sin orquestación.

**Roadmap de 5 Fases**:

| Fase | Enfoque | Duración | Criterio de Salida |
|------|---------|----------|-------------------|
| vNext-0 | Fundación (CI, paths, versión) | Semana 1 | CI corre 14 tests, todos los paths resuelven |
| vNext-1 | Hardening de gobernanza (approvals, escalation) | Semana 2 | Todos los cambios tienen approval records |
| vNext-2 | Reestructuración de memoria (split index) | Semana 3 | Split index operacional |
| vNext-3 | Optimización de workflows (tiering, audit scheduling) | Semana 4 | Workflows tiered, CI paralelizado |
| vNext-4 | Validación y cierre | Semana 5 | 16 lint checks pasan, review/audit completo |

**Rechazos Explícitos**: Agentes autónomos, motor de ejecución de workflows, bases de datos, orquestación runtime, gobernanza auto-modificable, sistemas distribuidos, sistema de plugins, aprobación automatizada, memoria embebida en agentes, revisión asistida por IA.

---

## Inconsistencias Pendientes

### Críticas (requieren acción inmediata)

| ID | Problema | Estado |
|----|----------|--------|
| CV-001 | CI no ejecuta tests de gobernanza root | Pendiente — requiere aprobación humana para cambio CI |
| CV-002 | ADR-001 sin aprobación humana | Pendiente — requiere decisión humana |
| CV-003 | OBJ-006 sin aprobación humana | Pendiente — requiere decisión humana |

### Medias

| ID | Problema | Estado |
|----|----------|--------|
| MR-001 | Designación de fase desalineada | Pendiente — requiere decisión humana |
| MR-002 | Versión inconsistente (v0.3 vs 0.1.0) | Pendiente — requiere decisión humana |
| MR-003 | 5 tareas IN_PROGRESS sin auditoría programada | Pendiente |
| MR-004 | `memory/research/` mal nombrado | Pendiente — requiere ADR para cambio estructural |
| MR-005 | CI usa wrapper de lint en vez de root | Pendiente |
| MR-006 | Sin mecanismo de enforcement de ADR | Pendiente — parte de vNext |

### Referencias Rotas Restantes (22)

Todas son problemas de prefijo de ruta: artefactos de aeos-core que referencian paths de root para archivos que existen bajo `aeos-core/`. El script de lint de aeos-core los resuelve en runtime mediante `_resolve_artifact_path()`, pero los paths literales en los archivos son incorrectos.

---

## Estado de Validación

### Lint AEOS

```
[PASS] Required Files (30/30)
[PASS] Memory Directories (9/9)
[PASS] Agent Registry (7 agents)
[PASS] Traceability References (all valid)
[PASS] Workflow Closure (all closed tasks valid)
[PASS] v0.3 Documents (5/5)
[PASS] Severity Labels (4/4)
[PASS] Traceability Integrity (no malformed IDs)
[PASS] Unresolved Lifecycle Continuity (all refs valid)
[PASS] Concurrent Objective Operations (3 ACTIVE objectives noted)
[PASS] Recovery Continuity (recovery handoff exists)
```

**Resultado**: ALL CHECKS PASSED (11/11)

### Tests

**Estado**: No ejecutables localmente (pytest no instalado).
**CI**: Configurado pero incompleto (solo ejecuta aeos-core/tests).
**Tests definidos**: 14 archivos (11 root + 3 aeos-core).

---

## Decisiones Humanas Pendientes

| Decisión | Contexto | Impacto |
|----------|----------|---------|
| Versión canónica (v0.3 o 0.1.0) | README dice v0.3, pyproject dice 0.1.0 | Afecta 3 archivos |
| Designación de fase (Phase 0 o avanzar) | Objetivos activos exceden scope de Phase 0 | Afecta gobernanza |
| Aprobación de ADR-001 | Estructura dual de directorios | Afecta path conventions |
| Aprobación de OBJ-006 | Objetivo de reconciliación | Afecta 9 tareas planificadas |
| Aprobación de diseño vNext | Roadmap de 5 fases | Afecta dirección del proyecto |

---

## Principios Preservados

| Principio | Estado |
|-----------|--------|
| Gobernanza primero | ✅ Mantenido |
| Humano en el bucle | ✅ Mantenido (pero no evidenciado) |
| Memoria explícita | ✅ Mantenido |
| Markdown-first | ✅ Mantenido |
| Repo-driven | ✅ Mantenido |
| Reproducibilidad | ✅ Mantenido |
| Auditabilidad | ✅ Mantenido |
| Sin estado oculto | ✅ Mantenido |
| Sin ejecución autónoma | ✅ Mantenido |
| Sin orquestación runtime | ✅ Mantenido |
| Sin auto-aprobación | ✅ Mantenido |
| Sin memoria oculta | ✅ Mantenido |

---

## Métricas del Repositorio (Actualizadas)

| Métrica | Valor |
|---------|-------|
| Archivos totales | ~170+ |
| Archivos de gobernanza | 7 canónicos + 1 experimental |
| Archivos de protocolos | 7 |
| Archivos de plantillas | 11 canónicas + 2 experimentales |
| Definiciones de agentes | 8 (1 registro + 7 agentes) |
| Archivos de flujos de trabajo | 6 |
| Directorios de memoria | 10 |
| Artefactos de memoria canónicos | 66 |
| Artefactos de memoria experimentales | 15 |
| Módulos de tests | 14 |
| Documentos de documentación | 17 |
| Scripts de validación | 2 |
| Checks de lint | 11 (todos pasando) |
| ADRs | 1 (PROPOSED) |
| Objetivos | 6 (2 CLOSED, 3 ACTIVE, 1 DRAFT) |
| Tareas | 11 (6 CLOSED, 5 IN_PROGRESS) |
| Incidentes activos | 2 |
| Escalaciones abiertas | 1 |
| Puntuación de gobernanza | 1.8 / 4.0 |
| Tasa de validación determinista | 89.8% |

---

## Próximos Pasos Recomendados

### Inmediatos (requieren aprobación humana)

1. Decidir versión canónica y alinear artefactos
2. Resolver designación de fase
3. Aprobar o rechazar ADR-001
4. Aprobar o rechazar OBJ-006
5. Actualizar CI para ejecutar tests root

### Corto plazo (vNext-0)

6. Corregir 22 referencias de ruta restantes
7. Añadir enforcement de ADR al lint
8. Crear plantilla de approval records
9. Documentar convención de nombres de agentes

### Mediano plazo (vNext-1 a vNext-3)

10. Crear registros de aprobación para cambios existentes
11. Implementar política de aging de escalaciones
12. Split del traceability index por objetivo
13. Paralelizar ejecución de CI
14. Añadir GitHub environment protection para cambios de gobernanza

---

## Conclusión

AEOS Core tiene un **marco de gobernanza fuerte** pero **enforcement débil**. Las reglas son comprehensivas y correctas, pero la brecha entre requisitos documentados y realidad operacional es significativa en tres áreas:

1. **CI no enforce validación de gobernanza** — el gap más crítico.
2. **No existen registros de aprobación humana** — la gobernanza humana está documentada pero no evidenciada.
3. **Artefactos de la sesión actual bypassaron entrada al ciclo de vida** — OBJ-006 y ADR-001 fueron creados sin autoridad humana documentada.

El diseño de MVP vNext aborda estos gaps con **complejidad mínima** (~250 líneas de código nuevo, 3 plantillas, 1 política). No añade agentes autónomos, runtime, orquestación, ni estado oculto. El resultado es un framework de gobernanza **enforcado, auditable y escalable** — sin sacrificar los principios que hacen efectivo a AEOS.
