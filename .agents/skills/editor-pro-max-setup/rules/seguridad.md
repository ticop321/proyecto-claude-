# Seguridad en scripts de editor-pro-max

## Reglas fundamentales

### 1. Nunca usar `eval()`

`eval()` ejecuta código arbitrario y es un vector de inyección de código.

**MAL — vulnerable:**
```typescript
// Nunca hagas esto con datos externos
const fps = eval(videoStream.r_frame_rate); // inyección de código si r_frame_rate es malicioso
```

**BIEN — seguro:**
```typescript
// Parsear manualmente fracciones como "30/1" o "60000/1001"
const fps = videoStream?.r_frame_rate
  ? (() => {
      const parts = videoStream.r_frame_rate.split("/");
      return parts.length === 2
        ? parseFloat(parts[0]) / parseFloat(parts[1])
        : parseFloat(parts[0]);
    })()
  : 30;
```

Este patrón fue aplicado en `scripts/analyze-video.ts`.

### 2. Validar parámetros CLI antes de interpolación en shell

Cuando parámetros de línea de comandos se usan en strings que se pasan a `execSync()`, validar con regex estricto primero:

**MAL — vulnerable a inyección de comandos:**
```typescript
const noiseDb = process.argv[3] || "-30dB";
const cmd = `ffmpeg -af "silencedetect=noise=${noiseDb}"`;
// Si noiseDb = '"; rm -rf /; echo "' → desastre
execSync(cmd);
```

**BIEN — validado primero:**
```typescript
const noiseDb = process.argv[3] || "-30dB";

// Validar que tenga exactamente el formato esperado
if (!/^-?\d+(\.\d+)?dB$/.test(noiseDb)) {
  console.error(`Valor inválido: "${noiseDb}". Formato esperado: -30dB`);
  process.exit(1);
}

// Ahora es seguro interpolar
const cmd = `ffmpeg -af "silencedetect=noise=${noiseDb}"`;
```

Patrones de validación usados en `scripts/detect-silence.ts`:
```typescript
// Para threshold de dB: acepta -30dB, -45.5dB, 0dB
if (!/^-?\d+(\.\d+)?dB$/.test(noiseDb)) { ... }

// Para duración en segundos: acepta 0.5, 1, 2.5
if (!/^\d+(\.\d+)?$/.test(minDuration)) { ... }
```

### 3. No usar `eval $CMD` en bash

**MAL — vulnerable:**
```bash
CMD="npx remotion render ${COMP_ID} ${OUTPUT_FILE}"
eval $CMD  # eval expande y ejecuta código arbitrario
```

**BIEN — llamada directa con comillas:**
```bash
npx remotion render "${COMP_ID}" "${OUTPUT_FILE}"
```

Este patrón fue aplicado en `scripts/render.sh`.

### 4. Siempre citar variables en bash

Las variables en shell sin comillas permiten word splitting y globbing:

```bash
# MAL
npx remotion render $COMP_ID $OUTPUT_FILE

# BIEN
npx remotion render "${COMP_ID}" "${OUTPUT_FILE}"
```

### 5. Rutas de archivos como argumentos, no interpolados en strings

```typescript
// MAL — si inputPath tiene espacios o caracteres especiales
const cmd = `ffprobe -i ${inputPath}`;

// BIEN — con comillas en el string del comando
const cmd = `ffprobe -v quiet -print_format json -show_format -show_streams "${inputPath}"`;
// (o mejor aún, usar spawn() con array de args para evitar shell totalmente)
```

## Resumen de vulnerabilidades corregidas en este proyecto

| Archivo | Vulnerabilidad | Fix aplicado |
|---------|---------------|--------------|
| `scripts/analyze-video.ts` | `eval(videoStream.r_frame_rate)` — ejecución de código arbitrario | Reemplazado por parseo manual de fracción |
| `scripts/render.sh` | `eval $CMD` — inyección de comandos shell | Reemplazado por llamada directa con args citados |
| `scripts/detect-silence.ts` | Interpolación directa de args CLI en comando FFmpeg | Añadida validación regex antes de interpolación |

## Dependencias con vulnerabilidades conocidas

`loader-utils` (transitivo vía `@remotion/cli`) tiene vulnerabilidades de seguridad conocidas. Mantener `@remotion/cli` actualizado a la última versión para obtener el fix:

```bash
npm update @remotion/cli
```
