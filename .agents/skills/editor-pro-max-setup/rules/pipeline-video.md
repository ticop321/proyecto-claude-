# Pipeline de video — editor-pro-max

## Flujo completo de edición

```
[Video de entrada]
       ↓
analyze-video.ts     → public/video-metadata.json
       ↓
detect-silence.ts    → public/silence.json
       ↓
generate-captions.ts → public/captions.json
       ↓
[Editar composición en src/compositions/]
       ↓
render.sh            → out/<composicion>_<plataforma>_<timestamp>.mp4
```

---

## 1. Analizar video (`scripts/analyze-video.ts`)

Extrae metadatos del video de entrada usando `ffprobe`.

**Uso:**
```bash
npx tsx scripts/analyze-video.ts public/assets/video.mp4
```

**Salida:** `public/video-metadata.json`
```json
{
  "duration": 120.5,
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "videoCodec": "h264",
  "audioCodec": "aac",
  "bitrate": 5000000,
  "fileSize": 75000000,
  "hasAudio": true
}
```

**Cuándo usarlo:** Siempre antes de crear una composición, para saber la duración y dimensiones del video fuente.

---

## 2. Detectar silencios (`scripts/detect-silence.ts`)

Detecta segmentos de silencio y habla en el audio del video usando FFmpeg `silencedetect`.

**Uso:**
```bash
npx tsx scripts/detect-silence.ts public/assets/video.mp4 [noise-db] [min-duration]

# Ejemplos:
npx tsx scripts/detect-silence.ts public/assets/video.mp4            # defaults: -30dB, 0.5s
npx tsx scripts/detect-silence.ts public/assets/video.mp4 -40dB 1.0  # más estricto
```

**Parámetros:**
- `noise-db` — umbral de silencio (default: `-30dB`). Más negativo = más estricto
- `min-duration` — duración mínima de silencio en segundos (default: `0.5`)

**Salida:** `public/silence.json`
```json
{
  "silenceSegments": [{"start": 5.2, "end": 7.8}, ...],
  "speechSegments": [{"start": 0, "end": 5.2}, {"start": 7.8, "end": 15.0}, ...],
  "totalDuration": 120.5,
  "speechDuration": 95.3,
  "silenceDuration": 25.2
}
```

**Cuándo usarlo:** Para identificar pausas y silencios antes de cortar o acelerar el video.

---

## 3. Renderizar (`scripts/render.sh`)

Renderiza una composición de Remotion en MP4, con dimensiones ajustadas por plataforma.

**Uso:**
```bash
./scripts/render.sh <composition-id> [platform]
```

**Composiciones disponibles** (definidas en `src/Root.tsx`):
- `Showcase` — composición de demostración
- `TikTok` — video vertical corto
- `Presentation` — video tipo presentación

**Plataformas disponibles:**

| Platform | Resolución |
|----------|-----------|
| `tiktok`, `instagram_reel`, `instagram_story`, `youtube_short` | 1080×1920 (vertical) |
| `instagram_post`, `twitter`, `facebook`, `square` | 1080×1080 (cuadrado) |
| `youtube`, `linkedin`, `landscape` | 1920×1080 (horizontal) |
| `cinematic` | 1920×800 (cinemático) |
| (sin plataforma) | Resolución por defecto de la composición |

**Ejemplos:**
```bash
./scripts/render.sh Showcase                    # resolución por defecto
./scripts/render.sh TikTok tiktok               # 1080×1920
./scripts/render.sh Presentation youtube        # 1920×1080
./scripts/render.sh Showcase instagram_post     # 1080×1080
```

**Salida:** `out/<composicion>_<plataforma>_<timestamp>.mp4`

---

## 4. Generar subtítulos (`scripts/generate-captions.ts`)

Transcribe el audio del video usando el modelo Whisper (vía `onnxruntime-node`).

**Uso:**
```bash
npx tsx scripts/generate-captions.ts public/assets/video.mp4
```

**Salida:** `public/captions.json` con timestamps de cada palabra/segmento.

**Nota:** Requiere que `onnxruntime-node` esté instalado correctamente (binarios CPU disponibles sin configuración adicional).

---

## 5. Previsualización en tiempo real

Para ver los cambios en tiempo real en el Remotion Studio:

```bash
npx remotion preview
# o
./scripts/preview.sh
```

Acceder en `http://localhost:3000`. Permite navegar por frames, editar props y ver el resultado antes de renderizar.

---

## Añadir assets al proyecto

Colocar archivos de video, imagen o audio en `public/assets/`:

```bash
cp mi-video.mp4 public/assets/video.mp4
cp mi-logo.png public/assets/logo.png
cp mi-musica.mp3 public/assets/music.mp3
```

En las composiciones, referenciar con `staticFile()` de Remotion:
```typescript
import {staticFile} from 'remotion';
const videoSrc = staticFile('assets/video.mp4');
```
