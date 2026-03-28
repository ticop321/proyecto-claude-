# Componentes — Media

## `src/components/media/`

### AudioTrack
Audio de fondo con fade in/out y ducking automático.
```tsx
<AudioTrack
  src={staticFile("assets/music.mp3")}
  volume={0.3}
  fadeInDurationSeconds={1}
  fadeOutDurationSeconds={2}
  duckDuringSegments={[{startSeconds: 5, endSeconds: 15}]}
  duckVolume={0.1}
  loop={true}
  trimStartSeconds={10}
/>
```

### FitVideo
Video responsivo con control de fit.
```tsx
<FitVideo
  src={staticFile("assets/video.mp4")}
  fit="cover"   // "cover" | "contain" | "fill"
  volume={0.3}
  playbackRate={1}
  muted={false}
/>
```

### FitImage
Imagen responsiva con efecto Ken Burns.
```tsx
<FitImage
  src={staticFile("assets/photo.jpg")}
  fit="cover"
  kenBurns="zoomIn"   // "zoomIn" | "zoomOut" | "panLeft" | "panRight" | "panUp" | "panDown"
  kenBurnsIntensity={0.1}
/>
```

### VideoClip
Video con trimming por segundos.
```tsx
<VideoClip
  src={staticFile("assets/video.mp4")}
  trimStartSeconds={5}
  trimEndSeconds={25}
  fit="cover"
  volume={1}
/>
```

### ImageOverlay
Imagen superpuesta con enter/exit animations.
```tsx
<ImageOverlay
  src={staticFile("assets/logo.png")}
  enterAnimation="fade"   // "fade" | "scale" | "slideUp" | "slideDown"
  exitAnimation="fade"
  enterDuration={15}
  exitDuration={10}
  opacity={1}
/>
```

### JumpCut
Compila segmentos de vídeo (silence removal).
```tsx
import {JumpCut, calculateJumpCutDuration} from './components/media/JumpCut';

const duration = calculateJumpCutDuration(speechSegments, fps, 0.1);

<JumpCut
  src={staticFile("assets/video.mp4")}
  segments={speechSegments}   // Array de {startSeconds, endSeconds}
  paddingSeconds={0.1}
  volume={1}
  fit="cover"
/>
```

### Slideshow
Rotación automática de imágenes con Ken Burns.
```tsx
<Slideshow
  images={[staticFile("img1.jpg"), staticFile("img2.jpg")]}
  transitionDuration={15}
  fit="cover"
  kenBurns={true}
/>
```
