# Componentes — Texto y Overlays

## Texto (`src/components/text/`)

### AnimatedTitle
Texto con animaciones enter-hold-exit.
```tsx
<AnimatedTitle
  text="Título"
  fontSize={64}
  fontFamily="Inter"
  fontWeight={700}
  color="#ffffff"
  textAlign="center"
  enterAnimation="slideUp"   // fade | slideUp | slideDown | slideLeft | slideRight | scale | typewriter | blur
  exitAnimation="fade"
  enterDuration={20}
  holdDuration={60}
  exitDuration={15}
  letterSpacing={2}
  maxWidth="80%"
/>
```

### CaptionOverlay
Subtítulos palabra-por-palabra con resaltado.
```tsx
<CaptionOverlay
  captionsSource={staticFile("captions.json")}
  preset="bold"     // "classic" | "bold" | "outline" | "glow" | "box"
  position="bottom" // "top" | "center" | "bottom"
  fontSize={64}
  highlightColor="#f43f5e"
  textColor="#ffffff"
  combineTokensWithinMs={1200}
  offsetMs={0}
/>
```

### LowerThird
Gráfico lower-third profesional.
```tsx
<LowerThird
  name="Juan García"
  title="Director de Marketing"
  accentColor="#8b5cf6"
  position="bottomLeft"   // "bottomLeft" | "bottomRight" | "bottomCenter"
  enterDuration={20}
  holdDuration={90}
  exitDuration={15}
/>
```

### TypewriterText
Texto carácter por carácter con cursor.
```tsx
<TypewriterText
  text="Hola, mundo"
  fontSize={48}
  fontFamily="JetBrains Mono"
  color="#ffffff"
  cursorColor="#8b5cf6"
  showCursor={true}
  typingSpeed={2}   // chars/frame
  startDelay={10}
/>
```

### WordByWordCaption
Captions con ventana de 5 palabras y resaltado.
```tsx
<WordByWordCaption
  words={[{startFrame: 0, endFrame: 20, text: "Hola"}, ...]}
  fontSize={48}
  highlightColor="#f43f5e"
  backgroundColor="rgba(0,0,0,0.7)"
  position="bottom"
/>
```

### TextStyles (presets)
```typescript
import {TEXT_STYLES} from './components/text/TextStyles';
// heading, subheading, body, caption, quote, code, display
<div style={TEXT_STYLES.heading}>Título</div>
```

---

## Overlays (`src/components/overlays/`)

### CallToAction
```tsx
<CallToAction
  text="Sígueme en Instagram"
  subtext="@micuenta"
  backgroundColor="rgba(139, 92, 246, 0.9)"
  position="bottom"   // "top" | "center" | "bottom"
  enterDelay={60}
/>
```

### ProgressBar
```tsx
<ProgressBar
  color="#8b5cf6"
  height={4}
  position="bottom"   // "top" | "bottom"
  borderRadius={2}
/>
```

### Watermark
```tsx
// Logo
<Watermark src={staticFile("assets/logo.png")} corner="bottomRight" opacity={0.5} size={80} />
// Texto
<Watermark text="@micuenta" corner="bottomRight" opacity={0.5} color="#ffffff" fontSize={16} />
```

### CountdownTimer
```tsx
<CountdownTimer
  startFrom={10}
  fontSize={120}
  color="#ffffff"
  accentColor="#8b5cf6"
  showLabel={true}
  label="Empieza en"
/>
```
