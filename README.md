# Editor Pro Max

AI-powered video editor built with [Remotion](https://www.remotion.dev/) and Claude Code — by [@soyenriquerocha](https://github.com/soyenriquerocha).

---

## Requisitos

- Node.js 18+
- npm

## Instalación

```bash
# Instalar dependencias
npm install --ignore-scripts
```

> `--ignore-scripts` evita que módulos nativos intenten descargar binarios CUDA, que fallan en entornos sin GPU.

## Uso

```bash
# Iniciar Remotion Studio (preview en tiempo real)
npm run dev
# → http://localhost:3000

# Verificar TypeScript
npm run typecheck

# Renderizar un video
npx remotion render <composition-id> out/video.mp4

# Renderizar para una plataforma
./scripts/render.sh TikTok tiktok
./scripts/render.sh Presentation youtube

# Renderizar para múltiples plataformas
./scripts/batch-render.sh TalkingHeadEdit youtube tiktok instagram_reel
```

## Composiciones disponibles

| ID | Dimensiones | Descripción |
|----|-------------|-------------|
| `Showcase` | 1920×1080 | Demo de componentes |
| `TikTok` | 1080×1920 | Video vertical corto |
| `InstagramReel` | 1080×1920 | Reel de Instagram |
| `YouTubeShort` | 1080×1920 | YouTube Short |
| `Presentation` | 1920×1080 | Presentación con slides |
| `Testimonial` | 1920×1080 | Cita con autor |
| `Announcement` | 1920×1080 | Video de anuncio |
| `BeforeAfter` | 1920×1080 | Comparativa antes/después |
| `TalkingHeadEdit` | 1920×1080 | Talking head con captions y silence removal |
| `PodcastClip` | 1080×1920 | Clip vertical de podcast |

## Pipeline de edición de video

```bash
# 1. Analizar video (extrae metadata)
npx tsx scripts/analyze-video.ts public/assets/video.mp4

# 2. Detectar silencios
npx tsx scripts/detect-silence.ts public/assets/video.mp4

# 3. Extraer audio para transcripción
npx tsx scripts/extract-audio.ts public/assets/video.mp4

# 4. Transcribir con Whisper.cpp
npx tsx scripts/transcribe.ts

# 5. Eliminar fondo de imagen con IA
npx tsx scripts/remove-bg.ts public/assets/photo.jpg
```

## Estructura del proyecto

```
src/
  Root.tsx                    # Registra las 10 composiciones
  compositions/               # Composiciones de demostración
  components/
    backgrounds/              # GradientBackground, ParticleField, GridPattern
    layout/                   # SafeArea, SplitScreen, PictureInPicture
    media/                    # FitVideo, FitImage, VideoClip, JumpCut, Slideshow
    overlays/                 # CallToAction, ProgressBar, Watermark, CountdownTimer
    text/                     # AnimatedTitle, CaptionOverlay, LowerThird, TypewriterText
  templates/
    social/                   # TikTokVideo, InstagramReel, YouTubeShort
    content/                  # Presentation, Testimonial
    promo/                    # Announcement, BeforeAfter
    editing/                  # TalkingHeadEdit, PodcastClip
  hooks/                      # useAnimation, useCaptions, useColorScheme...
  presets/                    # colors, dimensions, fonts, easings, brand
  utils/                      # editing, math

scripts/
  analyze-video.ts            # Metadata ffprobe → public/video-metadata.json
  detect-silence.ts           # Silencedetect → public/silence.json
  extract-audio.ts            # Extrae WAV 16kHz → public/assets/audio.wav
  transcribe.ts               # Whisper.cpp → public/captions.json
  remove-bg.ts                # Elimina fondo con IA
  render.sh                   # Renderiza para una plataforma
  batch-render.sh             # Renderiza para múltiples plataformas
```

## Licencia

MIT — Copyright (c) 2026 Enrique Rocha (@soyenriquerocha)
