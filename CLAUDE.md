# Asistente Legal Penal Español - Claude Code Project

## Resumen del Proyecto

Sistema experto de asistencia jurídica en Derecho Penal Español, basado en inteligencia artificial, que simula un abogado penalista senior con 20+ años de experiencia.

**Versión:** 1.0.0
**Lenguaje:** Python 3.8+
**Tipo:** Aplicación CLI educativa

## Estructura del Proyecto

```
proyecto-claude-/
├── main.py                    # Punto de entrada CLI principal
├── knowledge/                 # Base de conocimiento legal
│   ├── codigo_penal.py       # Código Penal español completo
│   ├── lecrim.py             # Ley de Enjuiciamiento Criminal
│   └── jurisprudencia.py     # Jurisprudencia del TS y TC
├── analysis/                  # Módulos de análisis jurídico
│   ├── case_analyzer.py      # Análisis de casos penales
│   └── legal_reasoning.py    # Razonamiento legal y calificación
├── drafting/                  # Generación de documentos legales
│   └── document_generator.py # Querellas, denuncias, recursos
├── emotional/                 # Inteligencia emocional
│   └── emotional_detector.py # Detección de estado emocional
├── learning/                  # Aprendizaje adaptativo
│   └── user_profiles.py      # Perfiles de usuario y preferencias
├── sources/                   # Verificación de fuentes
│   └── source_validator.py   # Validación de citas legales
├── .claude/                   # Configuración de Claude Code
│   └── skills/
│       └── superpowers/      # Skills de Superpowers
├── requirements.txt           # Dependencias Python
└── README.md                  # Documentación principal
```

## Funcionalidades Principales

### 1. Análisis de Casos Penales
- Identificación automática de tipos penales
- Análisis de elementos objetivos y subjetivos del delito
- Detección de circunstancias modificativas (atenuantes/agravantes/eximentes)
- Cálculo estimado de penas según el Código Penal
- Verificación de prescripción

### 2. Redacción de Documentos Legales
- Querellas criminales
- Denuncias
- Recursos de apelación y casación
- Escritos de defensa
- Informes jurídicos

### 3. Base de Conocimiento Legal
- Código Penal completo (LO 10/1995 actualizado 2024)
- LECrim (procedimientos, recursos, plazos)
- Jurisprudencia del Tribunal Supremo y Constitucional

### 4. Inteligencia Emocional
- Detección automática de estado emocional del usuario
- Adaptación del tono de respuesta
- Derivación a recursos de emergencia (024, 016, 112)

## Instalación y Configuración

### Dependencias

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar la aplicación

```bash
python main.py
```

## Superpowers Skills Instalados

Este proyecto tiene **Superpowers** instalado, lo que proporciona un workflow completo de desarrollo:

### Skills Disponibles

- **brainstorming** - Refinamiento de diseño mediante preguntas socráticas
- **test-driven-development** - Ciclo RED-GREEN-REFACTOR para TDD
- **systematic-debugging** - Proceso de depuración sistemática en 4 fases
- **writing-plans** - Planes de implementación detallados
- **executing-plans** - Ejecución de planes en lotes con checkpoints
- **subagent-driven-development** - Desarrollo con subagentes autónomos
- **using-git-worktrees** - Desarrollo paralelo con ramas aisladas
- **requesting-code-review** - Checklist pre-revisión de código
- **receiving-code-review** - Respuesta a feedback de revisión
- **finishing-a-development-branch** - Workflow de merge/PR
- **verification-before-completion** - Verificación antes de completar
- **writing-skills** - Crear nuevos skills siguiendo mejores prácticas

### Comandos de Superpowers

- `/superpowers:brainstorm` - Refinamiento de diseño interactivo
- `/superpowers:write-plan` - Crear plan de implementación
- `/superpowers:execute-plan` - Ejecutar plan en lotes

## Workflow de Desarrollo Recomendado

1. **Brainstorming**: Usar `/superpowers:brainstorm` para refinar ideas antes de codificar
2. **Planificación**: Usar `/superpowers:write-plan` para crear un plan detallado
3. **TDD**: Escribir tests primero, luego implementar (skill se activa automáticamente)
4. **Ejecución**: Usar `/superpowers:execute-plan` para implementar en lotes
5. **Revisión**: El sistema realiza revisión automática de código
6. **Merge**: Usar el workflow de finalización para merge/PR

## Stack Tecnológico

- **Lenguaje**: Python 3.8+
- **Framework**: CLI personalizado con `rich` para interfaz de usuario
- **Base de Datos**: Archivos JSON para historial
- **Testing**: pytest (recomendado para nuevas features)
- **Versionado**: Git con desarrollo en ramas

## Testing

Actualmente el proyecto no tiene suite de tests automatizados. Para nuevas features, se recomienda:

1. Usar el skill `test-driven-development` de Superpowers
2. Escribir tests con pytest
3. Seguir el ciclo RED-GREEN-REFACTOR

```bash
# Instalar pytest
pip install pytest

# Ejecutar tests (cuando existan)
pytest tests/
```

## Limitaciones Importantes

### Disclaimer Legal

**⚠️ IMPORTANTE:**

- Este sistema es una herramienta de asesoramiento orientativo basada en IA
- **NO sustituye el asesoramiento de un abogado colegiado**
- La información es orientativa, no constituye asesoramiento legal oficial
- Para casos reales, consultar siempre con un profesional del derecho
- Los documentos generados son plantillas que deben ser revisadas por un letrado

### Recursos de Emergencia

- **024** - Atención conducta suicida
- **016** - Violencia de género
- **112** - Emergencias generales
- **Turno de oficio**: Colegio de Abogados local

## Filosofía de Desarrollo

Siguiendo los principios de Superpowers:

- **Test-Driven Development** - Escribir tests primero, siempre
- **Sistemático sobre ad-hoc** - Proceso sobre adivinación
- **Reducción de complejidad** - Simplicidad como objetivo principal
- **Evidencia sobre afirmaciones** - Verificar antes de declarar éxito

## Contribución

Para contribuir al proyecto:

1. Crear una rama con prefijo `claude/`
2. Usar Superpowers para planificar e implementar
3. Seguir TDD estricto
4. Crear PR con revisión de código
5. Asegurar que todos los tests pasen

## Licencia

Proyecto educativo de código abierto.

**Uso permitido:** Fines educativos, investigación académica, desarrollo personal
**Restricciones:** No usar como único asesoramiento en casos reales sin validación legal profesional

## Fuentes Oficiales

- **BOE**: https://www.boe.es
- **CENDOJ**: https://www.poderjudicial.es
- **Tribunal Constitucional**: https://www.tribunalconstitucional.es

## Contacto y Soporte

Para issues y mejoras, usar el sistema de issues de GitHub del proyecto.

---

**Última actualización**: 2026-01-15
**Superpowers instalado**: ✅ Sí
**Skills activos**: 14
