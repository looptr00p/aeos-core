# Estado del Arte - AEOS Core v0

## Resumen Ejecutivo

AEOS Core v0 es un sistema de gobernanza para ingeniería de software asistida por IA. Proporciona un marco estructurado que mantiene la operación de IA asistida bajo control humano, auditable y reproducible.

**Versión**: 0.1.0
**Estado**: Phase 0 - Governance/Bootstrap
**Fecha**: 2026-05-18
**Repositorio**: aeos-core/

## Contexto y Motivación

### Problema

La ingeniería de software asistida por IA introduce riesgos que los flujos de trabajo tradicionales no abordan:

- Comportamiento autónomo sin responsabilidad.
- Estado oculto y memoria implícita.
- Expansión de alcance no controlada.
- Falta de trazas de auditoría.
- Resultados no reproducibles.

### Solución

AEOS Core proporciona un marco basado en gobernanza explícita, protocolos definidos, plantillas reutilizables y flujos de trabajo estructurados que mantienen la IA asistida bajo control humano.

## Arquitectura del Repositorio

```
aeos-core/
├── governance/          # Reglas, restricciones y políticas
│   ├── AGENTS.md              # Restricciones universales de agentes
│   ├── PHASE_POLICY.md        # Definición de fases y transiciones
│   ├── PERMISSION_MODEL.md    # Niveles de permisos
│   ├── REVIEW_REQUIREMENTS.md # Requisitos de revisión por categoría
│   ├── ESCALATION_POLICY.md   # Condiciones y proceso de escalación
│   └── SAFETY_RULES.md        # Reglas de seguridad innegociables
│
├── protocols/           # Cómo se realiza el trabajo
│   ├── TASK_PROTOCOL.md         # Definición y ciclo de vida de tareas
│   ├── REVIEW_PROTOCOL.md       # Tipos y proceso de revisión
│   ├── CONTEXT_PROTOCOL.md      # Requisitos de contexto explícito
│   ├── MEMORY_PROTOCOL.md       # Gestión de memoria explícita
│   ├── HANDOFF_PROTOCOL.md      # Requisitos de informe de entrega
│   ├── INCIDENT_PROTOCOL.md     # Categorización y respuesta a incidentes
│   └── ADR_PROTOCOL.md          # Proceso de registros de decisión arquitectónica
│
├── templates/           # Plantillas de artefactos reutilizables
│   ├── objective_template.md    # Definición de objetivos
│   ├── adr_template.md          # Registro de decisión arquitectónica
│   ├── task_template.md         # Definición de tareas
│   ├── review_template.md       # Informe de revisión
│   ├── audit_template.md        # Informe de auditoría
│   ├── handoff_template.md      # Informe de entrega
│   └── incident_template.md     # Informe de incidentes
│
├── agents/              # Definiciones de agentes y registro
│   ├── agent_registry.yaml      # Registro central de agentes
│   ├── director/                # Agente de dirección y gobernanza
│   ├── architect/               # Agente de arquitectura
│   ├── implementer/             # Agente de implementación
│   ├── reviewer/                # Agente de revisión
│   ├── auditor/                 # Agente de auditoría
│   ├── qa/                      # Agente de calidad
│   └── documentation/           # Agente de documentación
│
├── workflows/           # Definiciones de procesos end-to-end
│   ├── feature_workflow.md              # Implementación de nuevas funcionalidades
│   ├── bugfix_workflow.md               # Identificación y corrección de bugs
│   ├── architecture_change_workflow.md  # Proceso de cambio arquitectónico
│   ├── audit_workflow.md                # Proceso de auditoría de gobernanza
│   ├── incident_workflow.md             # Proceso de respuesta a incidentes
│   └── research_workflow.md             # Proceso de investigación y análisis
│
├── memory/              # Memoria institucional explícita
│   ├── objectives/      # Objetivos activos y completados
│   ├── decisions/       # ADRs y decisiones de gobernanza
│   ├── tasks/           # Definiciones y estado de tareas
│   ├── handoffs/        # Informes de entrega
│   ├── audits/          # Registros de revisión y auditoría
│   ├── incidents/       # Informes de incidentes
│   ├── architecture/    # Documentación de arquitectura
│   └── research/        # Hallazgos de investigación
│
├── tests/               # Validación de estructura del repositorio
│   ├── governance/      # Tests de archivos de gobernanza
│   ├── protocols/       # Tests de archivos de protocolos
│   ├── templates/       # Tests de archivos de plantillas
│   ├── agents/          # Tests de registro y definición de agentes
│   └── workflows/       # Tests de archivos de flujos de trabajo
│
├── docs/                # Documentación operativa
│   ├── AEOS_OVERVIEW.md       # Visión general de AEOS
│   ├── OPERATING_MODEL.md     # Modelo operativo
│   └── MVP_SCOPE.md           # Alcance del MVP
│
├── README.md            # Documentación principal del repositorio
└── pyproject.toml       # Configuración del proyecto Python
```

## Gobernanza Implementada

### Reglas Universales

| Regla | Descripción |
|-------|-------------|
| No auto-aprobación | Ningún agente puede aprobar su propio trabajo |
| Alcance definido | Los agentes operan dentro de límites explícitos |
| Sin memoria oculta | Toda memoria es explícita y trazable |
| Aprobación humana | Cambios críticos requieren aprobación humana |
| Trazas de auditoría | El historial de auditoría nunca se elimina |
| Sin permisos irrestrictos | Todos los permisos están definidos y limitados |

### Modelo de Permisos

| Nivel | Descripción | Agentes |
|-------|-------------|---------|
| READ_ONLY | Solo lectura | Por defecto |
| DOCS_ONLY | Lectura + documentación | documentation-agent |
| TESTS_ONLY | Lectura + tests | qa-agent |
| LIMITED_IMPLEMENTATION | Lectura + implementación acotada | implementer-agent (por tarea) |
| CRITICAL_SYSTEM_CHANGE | Requiere aprobación humana | Ningún agente directamente |

### Agentes Registrados

| Agente | Rol | Permisos | Puede auto-aprobar |
|--------|-----|----------|-------------------|
| director-agent | Dirección de gobernanza | READ_ALL, GOVERNANCE_REVIEW, APPROVAL_AUTHORITY | No |
| architect-agent | Propuestas de arquitectura | READ_ALL, DOCS_ONLY, LIMITED_IMPLEMENTATION | No |
| implementer-agent | Implementación acotada | READ_ALL, LIMITED_IMPLEMENTATION | No |
| reviewer-agent | Validación y revisión | READ_ALL, DOCS_ONLY | No |
| auditor-agent | Auditoría de gobernanza | READ_ALL, DOCS_ONLY | No |
| qa-agent | Validación de tests | READ_ALL, TESTS_ONLY | No |
| documentation-agent | Actualización de documentación | READ_ALL, DOCS_ONLY | No |

## Protocolos Implementados

| Protocolo | Propósito |
|-----------|-----------|
| TASK_PROTOCOL | Define estructura y ciclo de vida de tareas con ID, objetivo, contexto, alcance, criterios de aceptación |
| REVIEW_PROTOCOL | Define 6 tipos de revisión: scope, architecture, implementation, governance, validation, handoff |
| CONTEXT_PROTOCOL | Requiere fuentes canónicas, restricciones, alcance permitido y prohibido, condiciones de parada |
| MEMORY_PROTOCOL | Memoria explícita en markdown, versionada, sin mutación contextual oculta |
| HANDOFF_PROTOCOL | Informes obligatorios con resumen, archivos cambiados, decisiones, validaciones, riesgos, próximos pasos |
| INCIDENT_PROTOCOL | Categorización de incidentes, severidad, proceso de respuesta y resolución |
| ADR_PROTOCOL | Registros de decisión arquitectónica con contexto, decisión, alternativas, consecuencias |

## Flujos de Trabajo Implementados

| Flujo | Propósito | Etapas |
|-------|-----------|--------|
| feature_workflow | Implementación de nuevas funcionalidades | 12 etapas desde definición de objetivo hasta cierre |
| bugfix_workflow | Identificación y corrección de bugs | 12 etapas desde identificación hasta cierre |
| architecture_change_workflow | Cambios arquitectónicos | 13 etapas incluyendo ADR y revisión de arquitectura |
| audit_workflow | Auditorías de gobernanza | 12 etapas desde planificación hasta cierre |
| incident_workflow | Respuesta a incidentes | 12 etapas desde identificación hasta lecciones aprendidas |
| research_workflow | Investigación y análisis | 9 etapas desde definición hasta entrega |

## Ciclo de Vida Oficial

```
Objective → ADR → Task Definition → Agent Assignment → Implementation → Review → Audit → CI Validation → Handoff → Memory Update → Close
```

Cada etapa produce artefactos explícitos. Ninguna etapa puede omitirse.

## Validación y Tests

### Suite de Tests

| Módulo | Tests | Propósito |
|--------|-------|-----------|
| test_required_governance_files.py | 7 | Valida existencia de 6 archivos de gobernanza |
| test_required_protocol_files.py | 8 | Valida existencia de 7 archivos de protocolos |
| test_required_template_files.py | 8 | Valida existencia de 7 archivos de plantillas |
| test_agent_registry.py | 12 | Valida registro, campos requeridos, no auto-aprobación, permisos |
| test_required_workflows.py | 7 | Valida existencia de 6 archivos de flujos de trabajo |

### Resultados

```
42 passed in 0.15s
0 failed
```

## No-Objetivos Explícitos

AEOS Core v0 **NO** es:

- Un sistema de ejecución autónoma
- Un sistema de memoria oculta
- Un sistema de agentes auto-modificables
- Un runtime de orquestación no controlado
- Un sistema de aprobaciones autónomas
- Una plataforma SaaS
- Una plataforma de chatbots
- Un motor de ejecución de flujos de trabajo
- Una plataforma cloud
- Un runtime distribuido
- Un sistema de agentes runtime

AEOS Core v0 **NO** ejecuta flujos de trabajo autónomos.

## Fase Actual

**Phase 0: Governance/Bootstrap**

- Propósito: Establecer gobernanza, protocolos, plantillas y estructura base.
- Permitido: Crear documentos de gobernanza, protocolos, plantillas, definiciones de agentes, flujos de trabajo.
- Prohibido: Cargas de producción, integraciones externas, operaciones autónomas.
- Criterio de salida: Todos los archivos de gobernanza creados, todos los protocolos definidos, todas las plantillas listas, tests pasando.

## Métricas del Repositorio

| Métrica | Valor |
|---------|-------|
| Archivos totales | 52 |
| Archivos de gobernanza | 6 |
| Archivos de protocolos | 7 |
| Archivos de plantillas | 7 |
| Definiciones de agentes | 8 (1 registro + 7 agentes) |
| Archivos de flujos de trabajo | 6 |
| Directorios de memoria | 8 |
| Módulos de tests | 5 |
| Casos de test | 42 |
| Tests passing | 42 |
| Tests failing | 0 |
| Documentación operativa | 3 |
| Dependencias de runtime | 0 |
| Dependencias de desarrollo | 2 (pytest, pyyaml) |

## Trazabilidad

Todos los artefactos en AEOS Core son trazables mediante IDs inmutables:

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Objetivo | OBJ-XXX | OBJ-001 |
| Decisión arquitectónica | ADR-XXX | ADR-001 |
| Tarea | TASK-XXX | TASK-001 |
| Revisión | REV-XXX | REV-001 |
| Auditoría | AUD-XXX | AUD-001 |
| Entrega | HND-XXX | HND-001 |
| Incidente | INC-XXX | INC-001 |

## Principios de Diseño

| Principio | Descripción |
|-----------|-------------|
| Gobernanza primero | La gobernanza precede a la implementación |
| Flujo de trabajo primero | Todo trabajo sigue flujos definidos |
| Humano en el bucle | Ningún agente se auto-aprueba |
| Memoria explícita | Toda memoria es markdown, versionada y trazable |
| Reproducibilidad | Todos los resultados son reproducibles desde git |
| Auditabilidad | Todas las operaciones son trazables y preservadas |
| Minimalismo | Preferir simplicidad sobre extensibilidad |
| Determinismo | Sin estado oculto, sin comportamiento implícito |
