# Templates listos para usar

Ubicación: `src/templates/`

---

## Social

### TikTokVideo (`src/templates/social/TikTokVideo.tsx`)
```tsx
<TikTokVideo
  hook="¿Sabías que puedes..."
  body="Aquí te explico cómo..."
  cta="Sígueme para más contenido"
  backgroundColors={["#0a0a0a", "#1a0a2e"]}
  accentColor="#f43f5e"
  textColor="#ffffff"
/>
// Timing: 0-60f hook (scale), 60-180f body (slideUp), 180-270f CTA (bottom)
```

### InstagramReel (`src/templates/social/InstagramReel.tsx`)
```tsx
<InstagramReel
  headline="Gran Título"
  subtext="Descripción breve"
  brandName="@micuenta"
  backgroundColors={["#667eea", "#764ba2"]}
  accentColor="#f093fb"
/>
```

### YouTubeShort (`src/templates/social/YouTubeShort.tsx`)
```tsx
<YouTubeShort
  title="Título del Short"
  subtitle="Subtítulo opcional"
  backgroundColors={["#0a0a0a", "#1a1a2e"]}
  accentColor="#ff0000"
/>
```

---

## Content

### Presentation
```tsx
<Presentation
  slides={[
    {title: "Slide 1", body: "Contenido 1"},
    {title: "Slide 2", body: "Contenido 2"},
  ]}
  framesPerSlide={150}  // 5s por slide a 30fps
  accentColor="#8b5cf6"
/>
```

### Testimonial
```tsx
<Testimonial
  quote="Este producto cambió mi workflow."
  author="María López"
  role="CEO, Empresa XYZ"
  avatarSrc={staticFile("assets/avatar.jpg")}
  accentColor="#8b5cf6"
/>
```

---

## Editing — Los más potentes

### TalkingHeadEdit — Template completo para presentadores
```tsx
<TalkingHeadEdit
  videoSrc={staticFile("assets/video.mp4")}
  captionsPath="captions.json"
  silencePath="silence.json"
  removeSilence={true}        // JumpCut automático con speechSegments
  showCaptions={true}
  captionPreset="bold"         // classic | bold | outline | glow | box
  title="Mi Tutorial"
  titleDuration={90}           // 3s de título
  speakerName="Juan García"
  speakerTitle="Full Stack Dev"
  ctaText="Sígueme @juangarcia"
  ctaDuration={90}
  backgroundMusic={staticFile("assets/music.mp3")}
  musicVolume={0.15}
  accentColor="#8b5cf6"
/>
// Incluye: silence removal, captions, lower-third, CTA, música, progress bar
```

### PodcastClip — Extraer clip de video largo
```tsx
<PodcastClip
  videoSrc={staticFile("assets/podcast.mp4")}
  clipStartSeconds={120}   // Inicio en segundos
  clipEndSeconds={150}     // Fin en segundos (30s de clip)
  captionsPath="captions.json"
  showCaptions={true}
  captionPreset="bold"
  title="El mejor momento"
  accentColor="#f43f5e"
/>
// Los captions se desplazan: offsetMs = clipStartSeconds * 1000
```

---

## Promo

### Announcement
```tsx
<Announcement
  preTitle="Presentamos"
  title="Editor Pro Max"
  subtitle="Crea videos con IA"
  cta="Disponible ahora"
  ctaSubtext="Gratis para siempre"
  backgroundColors={["#0a0a0a", "#1a0a2e"]}
  accentColor="#8b5cf6"
/>
// Timing: 0-60f preTitle, 60-150f title (scale), 150-210f subtitle, 210-300f CTA
```

### BeforeAfter
```tsx
<BeforeAfter beforeLabel="Sin editar" afterLabel="Editado" accentColor="#8b5cf6">
  <FitVideo src={staticFile("original.mp4")} muted />
  <FitVideo src={staticFile("edited.mp4")} muted />
</BeforeAfter>
// Transición wipe en el frame 90 de 180
```
