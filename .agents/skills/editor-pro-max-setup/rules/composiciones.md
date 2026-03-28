# Composiciones de editor-pro-max

Archivo principal: `src/Root.tsx` — registra 10 composiciones en 5 carpetas.

## Folder "Examples"

### Showcase
- **Dimensiones:** 1920×1080, 30fps, 300 frames (10s)
- **Props:** ninguna (demo)
- **Descripción:** Composición de demostración con GradientBackground animado, ParticleField, 4 secuencias de AnimatedTitle y un Watermark.

## Folder "Social"

### TikTok
- **Dimensiones:** 1080×1920, 30fps, 270 frames (9s)
- **Props:** `hook` (string), `body` (string), `cta` (string)
- **Template:** `src/templates/social/TikTokVideo.tsx`

### InstagramReel
- **Dimensiones:** 1080×1920, 30fps, 240 frames (8s)
- **Props:** `headline` (string), `subtext` (string), `brandName` (string)
- **Template:** `src/templates/social/InstagramReel.tsx`

### YouTubeShort
- **Dimensiones:** 1080×1920, 30fps, 300 frames (10s)
- **Props:** `title` (string), `subtitle` (string)
- **Template:** `src/templates/social/YouTubeShort.tsx`

## Folder "Content"

### Presentation
- **Dimensiones:** 1920×1080, 30fps, 450 frames (15s)
- **Props:** `slides[]` (array de `{title, body}`)
- **Template:** `src/templates/content/Presentation.tsx`

### Testimonial
- **Dimensiones:** 1920×1080, 30fps, 180 frames (6s)
- **Props:** `quote` (string), `author` (string), `role` (string)
- **Template:** `src/templates/content/Testimonial.tsx`

## Folder "Promo"

### Announcement
- **Dimensiones:** 1920×1080, 30fps, 300 frames (10s)
- **Props:** `preTitle` (string), `title` (string), `subtitle` (string), `cta` (string)
- **Template:** `src/templates/promo/Announcement.tsx`

### BeforeAfter
- **Dimensiones:** 1920×1080, 30fps, 180 frames (6s)
- **Props:** ninguna (demo)
- **Template:** `src/templates/promo/BeforeAfter.tsx`

## Folder "Editing"

### TalkingHeadEdit
- **Dimensiones:** 1920×1080, 30fps, 900 frames (30s)
- **Props:** `videoSrc`, `showCaptions`, `captionPreset`, `removeSilence`, `speakerName`, `speakerTitle`, `ctaText`, `backgroundMusic`, `musicVolume`, `accentColor`
- **Template:** `src/templates/editing/TalkingHeadEdit.tsx`

### PodcastClip
- **Dimensiones:** 1080×1920, 30fps, 900 frames (30s)
- **Props:** `videoSrc`, `clipStartSeconds`, `clipEndSeconds`, `showCaptions`, `captionPreset`
- **Template:** `src/templates/editing/PodcastClip.tsx`

---

## Cómo renderizar

```bash
./scripts/render.sh InstagramReel instagram_reel
./scripts/render.sh TikTok tiktok
./scripts/render.sh TalkingHeadEdit youtube
./scripts/batch-render.sh TalkingHeadEdit youtube tiktok instagram_reel

# Con props:
npx remotion render InstagramReel out/reel.mp4 --props='{"headline":"Mi Título","subtext":"Descripción","brandName":"@micuenta"}'
```
