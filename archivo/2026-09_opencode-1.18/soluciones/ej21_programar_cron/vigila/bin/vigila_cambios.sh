#!/usr/bin/env bash
set -euo pipefail

# Raíz del proyecto vigila/: el directorio padre de bin/
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

HASH_FILE="$RAIZ/hash.txt"
LOG_DIR="$RAIZ/log"
LOG_FILE="$LOG_DIR/vigilancia.log"

URL="https://example.com"
FECHA="$(date '+%Y-%m-%d %H:%M:%S')"

mkdir -p "$LOG_DIR"

NUEVO_HASH="$(curl -fsSL "$URL" | sha256sum | cut -d' ' -f1)"

if [[ ! -f "$HASH_FILE" ]]; then
    echo "[$FECHA] Inicio de vigilancia. Hash guardado: $NUEVO_HASH" >> "$LOG_FILE"
    echo "$NUEVO_HASH" > "$HASH_FILE"
elif [[ "$(cat "$HASH_FILE")" == "$NUEVO_HASH" ]]; then
    echo "[$FECHA] Sin cambios en $URL (hash $NUEVO_HASH)" >> "$LOG_FILE"
else
    ANTERIOR="$(cat "$HASH_FILE")"
    echo "[$FECHA] CAMBIO DETECTADO en $URL. Anterior: $ANTERIOR, nuevo: $NUEVO_HASH" >> "$LOG_FILE"
    echo "$NUEVO_HASH" > "$HASH_FILE"
fi
