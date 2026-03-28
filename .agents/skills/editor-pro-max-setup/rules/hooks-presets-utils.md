# Hooks, Presets y Utilidades

---

## Hooks (`src/hooks/`)

### useAnimation — Enter-hold-exit
```typescript
const anim = useAnimation({enterDuration: 20, holdDuration: 60, exitDuration: 15, type: "spring"});
// Retorna: opacity, enterProgress, exitProgress, isEntering, isHolding, isExiting, isVisible
```

### useCaptions — Captions ms → frames
```typescript
const words = captionsToWords(captions, fps);
// words = [{text, startFrame, endFrame}]
const activeCaption = useCurrentCaption(words); // string | null
```

### useColorScheme — Paleta de colores
```typescript
const palette = useColorScheme("dark");
// Paletas: dark | light | vibrant | warm | cool | neon | brand
// palette = {bg, surface, text, textMuted, accent, accentAlt}
```

### useSilenceSegments — Cargar silence.json
```typescript
const data = useSilenceSegments(); // Carga public/silence.json
// {silenceSegments, speechSegments, totalDuration, speechDuration, silenceDuration} | null
```

### useTranscription — Cargar captions
```typescript
const {captions, pages, isLoading} = useTranscription("captions.json", 1200);
```

### useVideoMetadata — Cargar metadata
```typescript
const meta = useVideoMetadata("video-metadata.json");
// {duration, width, height, fps, videoCodec, audioCodec, hasAudio} | null
```

---

## Presets (`src/presets/`)

### colors.ts
```typescript
import {PALETTES, GRADIENTS} from '../presets/colors';
// PALETTES: dark, light, vibrant, warm, cool, neon, brand
// GRADIENTS: sunset, ocean, forest, purple, fire, midnight, aurora, rainbow
```

### dimensions.ts
```typescript
import {PLATFORMS, secondsToFrames, framesToSeconds} from '../presets/dimensions';
// PLATFORMS: tiktok(1080x1920), youtube(1920x1080), instagram_post(1080x1080)...
secondToFrames(5, 30) // → 150
```

### fonts.ts
```typescript
import {FONT_FAMILIES, loadDefaultFonts} from '../presets/fonts';
// heading: Inter, display: Poppins, mono: JetBrains Mono, elegant: Playfair Display
await loadDefaultFonts();
```

### easings.ts
```typescript
import {EASINGS} from '../presets/easings';
// linear, easeIn/Out/InOut, bounceIn/Out, elastic, backIn/Out, sharp, smooth, snappy
interpolate(frame, [0, 30], [0, 1], {easing: EASINGS.bounceOut});
```

### brand.ts
```typescript
import {BRAND} from '../presets/brand';
// BRAND.name, BRAND.handle, BRAND.colors.primary (#8b5cf6), BRAND.colors.secondary (#6366f1)
```

---

## Utilidades (`src/utils/`)

### editing.ts
```typescript
buildCutList(speechSegments, {paddingSeconds: 0.1, minDurationSeconds: 0.3})
mergeSegments(segments, 0.5)    // Fusiona si gap < 0.5s
calculateTotalDuration(segments) // → segundos totales
offsetCaptions(captions, clipStartSeconds * 1000)
```

### math.ts
```typescript
clamp(1.5, 0, 1)     // → 1
lerp(0, 100, 0.5)    // → 50
remap(frame, 0, 30, 0, 1)
fadeIn(frame, 0, 15)            // 0→1
fadeOut(frame, 60, 15)          // 1→0
slideIn(frame, 0, 20, 50, fps)  // spring desde y=50 a y=0
enterHoldExit(frame, 20, 60, 15) // patrón completo
```
