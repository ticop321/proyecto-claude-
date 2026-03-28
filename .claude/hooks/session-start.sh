#!/bin/bash
set -euo pipefail

# Solo ejecutar en entornos remotos (Claude Code en la web)
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

# Instalar dependencias npm
# Se usa --ignore-scripts para evitar la descarga de binarios nativos
# de onnxruntime-node que requiere acceso a GitHub en el entorno remoto
if [ -f "package.json" ]; then
  npm install --ignore-scripts
fi
