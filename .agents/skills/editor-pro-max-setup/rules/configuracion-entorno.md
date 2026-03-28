# Configuración del entorno editor-pro-max

## Instalación de dependencias

Usa siempre `--ignore-scripts` para evitar que módulos nativos intenten descargar binarios CUDA de GPU (que fallan en entornos sin GPU):

```bash
npm install --ignore-scripts
```

Los binarios CPU de `onnxruntime-node` vienen empaquetados en el módulo y funcionan sin descarga adicional. El flag `--ignore-scripts` solo omite la descarga opcional de binarios CUDA.

## Hook de sesión automático

El proyecto incluye un hook de sesión en `.claude/hooks/session-start.sh` que instala dependencias automáticamente en Claude Code remoto:

```bash
#!/bin/bash
set -euo pipefail
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi
cd "$CLAUDE_PROJECT_DIR"
if [ -f "package.json" ]; then
  npm install --ignore-scripts
fi
```

El hook está registrado en `.claude/settings.json`:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session-start.sh"
          }
        ]
      }
    ]
  }
}
```

Este hook solo corre en entornos remotos (`CLAUDE_CODE_REMOTE=true`). En local no hace nada.

## Módulos nativos incluidos

El proyecto usa tres módulos con binarios nativos:

| Módulo | Uso | Estado |
|--------|-----|--------|
| `onnxruntime-node` | Inferencia de modelos AI (Whisper, etc.) | Binarios CPU incluidos |
| `sharp` | Procesamiento de imágenes | Binarios precompilados incluidos |
| `fluent-ffmpeg` | Wrapper de FFmpeg para Node.js | Pure JS (no requiere binarios) |

### Verificar que funcionan correctamente

```bash
node -e "require('onnxruntime-node'); console.log('onnxruntime-node OK')"
node -e "require('sharp'); console.log('sharp OK')"
node -e "require('fluent-ffmpeg'); console.log('fluent-ffmpeg OK')"
```

## Verificar FFmpeg disponible

Los scripts usan `npx remotion ffmpeg` y `npx remotion ffprobe` (FFmpeg bundled con Remotion):

```bash
npx remotion ffmpeg -version
npx remotion ffprobe -version
```

## TypeScript — verificar que compila

```bash
npx tsc --noEmit
```

Debe completar sin errores. Si hay errores de tipos en scripts, revisar los imports y las anotaciones de tipo.

## Iniciar el servidor de preview

```bash
npx remotion preview
# o
./scripts/preview.sh
```

Abre el estudio de Remotion en `http://localhost:3000`.
