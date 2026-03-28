---
name: editor-pro-max-setup
description: Configuración, seguridad y pipeline de video del editor editor-pro-max con Remotion
metadata:
  tags: remotion, video, editor, setup, seguridad, pipeline, npm, scripts
---

## Cuándo usar esta skill

Usa esta skill en cualquiera de estas situaciones:

- **Cuando configures el proyecto editor-pro-max** — instalación de dependencias, hooks de sesión, módulos nativos
- **Al instalar dependencias o módulos nativos** — npm, onnxruntime-node, sharp, fluent-ffmpeg
- **Para verificar o corregir seguridad en scripts** — eval(), inyección de comandos, validación de inputs
- **Cuando uses los scripts del pipeline de video** — analizar, detectar silencios, renderizar
- **Al renderizar, analizar o editar videos con Remotion** — composiciones, plataformas, resoluciones

## Configuración del entorno

Al configurar el proyecto por primera vez o instalar dependencias, carga el archivo de reglas:

[./rules/configuracion-entorno.md](./rules/configuracion-entorno.md)

## Seguridad en scripts

Cuando revises, escribas o modifiques scripts de video (TypeScript o shell), consulta las prácticas de seguridad:

[./rules/seguridad.md](./rules/seguridad.md)

## Pipeline de video

Para usar los scripts del pipeline (analizar video, detectar silencios, renderizar), carga:

[./rules/pipeline-video.md](./rules/pipeline-video.md)

## Resumen del proyecto

`editor-pro-max` es un editor de video basado en **Remotion** (React + TypeScript). Estructura principal:

```
src/
  compositions/   # Composiciones de Remotion (Showcase, TikTok, Presentation, etc.)
  components/     # Componentes reutilizables (TextOverlay, AudioWave, Captions, etc.)
  templates/      # Plantillas predefinidas
  hooks/          # Custom hooks de React
  schemas/        # Esquemas Zod para props
  utils/          # Utilidades (cálculos de tiempo, colores, etc.)

scripts/
  analyze-video.ts      # Extrae metadatos de video con ffprobe
  detect-silence.ts     # Detecta silencios con FFmpeg silencedetect
  generate-captions.ts  # Genera subtítulos con Whisper
  render.sh             # Renderiza composiciones para múltiples plataformas
  preview.sh            # Inicia el servidor de preview de Remotion

public/
  assets/         # Videos, imágenes, audio de entrada

.claude/
  hooks/session-start.sh  # Hook de inicio de sesión (instala deps automáticamente)
```
