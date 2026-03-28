---
name: editor-pro-max-setup
description: Editor de video completo con Remotion — composiciones, componentes, templates, pipeline y seguridad
metadata:
  tags: remotion, video, editor, setup, seguridad, pipeline, npm, scripts, tiktok, instagram, youtube, captions, animaciones
---

## Cuándo usar esta skill

Usa esta skill en cualquiera de estas situaciones:

- **Cuando configures el proyecto editor-pro-max** — instalación, hooks de sesión, módulos nativos
- **Al instalar dependencias o módulos nativos** — npm, onnxruntime-node, sharp, fluent-ffmpeg
- **Para verificar o corregir seguridad en scripts** — eval(), inyección de comandos, validación de inputs
- **Cuando uses los scripts del pipeline de video** — analizar, detectar silencios, transcribir, renderizar
- **Al renderizar, analizar o editar videos con Remotion** — composiciones, plataformas, resoluciones
- **Cuando crees o edites composiciones de Remotion** — TikTok, Instagram, YouTube, Presentation, etc.
- **Al usar componentes de texto, fondo, media u overlays** — AnimatedTitle, CaptionOverlay, GradientBackground, etc.
- **Cuando apliques templates de edición de video** — TalkingHeadEdit, PodcastClip, Testimonial, etc.
- **Al trabajar con captions, silencios o metadata** — hooks y utilidades del proyecto
- **Para renderizar en múltiples plataformas** — presets de dimensiones y colores

---

## Configuración del entorno

Al configurar el proyecto por primera vez o instalar dependencias:

[./rules/configuracion-entorno.md](./rules/configuracion-entorno.md)

## Seguridad en scripts

Cuando revises, escribas o modifiques scripts (TypeScript o shell):

[./rules/seguridad.md](./rules/seguridad.md)

## Composiciones registradas

Para crear o modificar composiciones (TikTok, Instagram, YouTube, Presentation, etc.):

[./rules/composiciones.md](./rules/composiciones.md)

## Componentes — Fondos y Layout

Para usar GradientBackground, ParticleField, GridPattern, SafeArea, SplitScreen, PictureInPicture:

[./rules/componentes-fondos-layout.md](./rules/componentes-fondos-layout.md)

## Componentes — Media

Para usar FitVideo, FitImage, VideoClip, AudioTrack, JumpCut, Slideshow, ImageOverlay:

[./rules/componentes-media.md](./rules/componentes-media.md)

## Componentes — Texto y Overlays

Para usar AnimatedTitle, CaptionOverlay, LowerThird, TypewriterText, WordByWordCaption, CallToAction, Watermark, ProgressBar:

[./rules/componentes-texto-overlays.md](./rules/componentes-texto-overlays.md)

## Templates listos para usar

Para aplicar templates completos (TalkingHeadEdit, PodcastClip, TikTok, Instagram, Announcement, Presentation, Testimonial, BeforeAfter):

[./rules/templates.md](./rules/templates.md)

## Hooks, presets y utilidades

Para usar hooks custom (useAnimation, useCaptions, useColorScheme), presets de colores/fuentes/dimensiones, y utilidades (editing, math):

[./rules/hooks-presets-utils.md](./rules/hooks-presets-utils.md)

## Pipeline de video (scripts)

Para usar los scripts del pipeline (analyze-video, detect-silence, extract-audio, remove-bg, transcribe, render, batch-render):

[./rules/pipeline-video.md](./rules/pipeline-video.md)

---

## Estructura del proyecto

```
src/
  Root.tsx                    # Registra las 10 composiciones
  index.ts                    # Punto de entrada (registerRoot)
  compositions/               # Composiciones de demostración
  components/
    backgrounds/              # ColorWash, GradientBackground, GridPattern, ParticleField
    layout/                   # SafeArea, SplitScreen, PictureInPicture
    media/                    # AudioTrack, FitVideo, FitImage, VideoClip, ImageOverlay, JumpCut, Slideshow
    overlays/                 # CallToAction, CountdownTimer, ProgressBar, Watermark
    text/                     # AnimatedTitle, CaptionOverlay, LowerThird, TypewriterText, WordByWordCaption, TextStyles
  templates/
    content/                  # Presentation, Testimonial
    editing/                  # TalkingHeadEdit, PodcastClip
    promo/                    # Announcement, BeforeAfter
    social/                   # TikTokVideo, InstagramReel, YouTubeShort
  hooks/                      # useAnimation, useCaptions, useColorScheme, useSilenceSegments, useTranscription, useVideoMetadata
  schemas/                    # Esquemas Zod para todas las props
  presets/                    # brand, colors (PALETTES/GRADIENTS), dimensions (PLATFORMS), easings, fonts
  utils/                      # editing (buildCutList, mergeSegments), math (clamp, lerp, fadeIn, slideIn...)

scripts/
  analyze-video.ts            # Metadatos ffprobe → public/video-metadata.json
  detect-silence.ts           # FFmpeg silencedetect → public/silence.json
  extract-audio.ts            # Extrae WAV 16kHz mono → public/assets/audio.wav
  remove-bg.ts                # Remueve fondo con IA (@imgly/background-removal-node)
  transcribe.ts               # Whisper.cpp → public/captions.json
  render.sh                   # Renderiza composición para una plataforma
  batch-render.sh             # Renderiza para múltiples plataformas en batch

public/
  assets/                     # Videos, imágenes, audio de entrada
  video-metadata.json         # Generado por analyze-video.ts
  silence.json                # Generado por detect-silence.ts
  captions.json               # Generado por transcribe.ts

.claude/
  hooks/session-start.sh      # Instala deps automáticamente en Claude Code remoto
```
