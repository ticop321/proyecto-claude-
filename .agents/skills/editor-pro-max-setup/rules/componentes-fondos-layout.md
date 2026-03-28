# Componentes — Fondos y Layout

## Fondos (`src/components/backgrounds/`)

### ColorWash
```tsx
<ColorWash color="#0a0a0a" toColor="#1a1a2e" opacity={0.9} />
```

### GradientBackground
```tsx
import {GRADIENTS} from './presets/colors';
<GradientBackground
  colors={GRADIENTS.purple}  // o array: ["#8b5cf6", "#6366f1"]
  angle={135}
  animateAngle={true}
  animateSpeed={0.5}
  type="linear"  // "linear" | "radial"
/>
```

### GridPattern
```tsx
<GridPattern
  type="dots"     // "dots" | "lines" | "crosses"
  spacing={40}
  size={2}
  color="#ffffff"
  opacity={0.1}
  animate={true}
/>
```

### ParticleField
```tsx
<ParticleField
  count={50}
  color="#8b5cf6"
  speed={1}
  direction="up"   // "up" | "down" | "left" | "right"
/>
```
Usa seeded random — resultados determinísticos por frame.

---

## Layout (`src/components/layout/`)

### SafeArea
```tsx
<SafeArea paddingHorizontal={60} paddingVertical={60}>
  {/* contenido */}
</SafeArea>
```

### SplitScreen
```tsx
// 2 paneles
<SplitScreen direction="horizontal" ratio={0.6} gap={4}>
  <div>60%</div>
  <div>40%</div>
</SplitScreen>
// 4 paneles (grid automático con 4 children)
```

### PictureInPicture
```tsx
<PictureInPicture
  main={<FitVideo src={staticFile("main.mp4")} />}
  pip={<FitVideo src={staticFile("cam.mp4")} />}
  corner="bottomRight"   // "topLeft" | "topRight" | "bottomLeft" | "bottomRight"
  pipWidth={360}
  pipHeight={240}
  margin={24}
  borderRadius={12}
  shadow={true}
/>
```
