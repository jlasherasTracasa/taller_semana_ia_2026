#!/usr/bin/env bash
# Vigila cambios en una web y registra el resultado en un log
URL="https://example.com"
ETIQUETA=$(curl -s "$URL" | md5sum | cut -d' ' -f1)
ANTERIOR="$(cat /tmp/curso_agentes/rutina/vigila/hash.txt 2>/dev/null || echo '')"
FECHA=$(date '+%Y-%m-%d %H:%M:%S')
if [ "$ANTERIOR" = "" ]; then
  echo "$FECHA inicio vigilancia hash=$ETIQUETA" >> /tmp/curso_agentes/rutina/vigila/log/vigilancia.log
elif [ "$ANTERIOR" = "$ETIQUETA" ]; then
  echo "$FECHA sin cambios ($ETIQUETA)" >> /tmp/curso_agentes/rutina/vigila/log/vigilancia.log
else
  echo "$FECHA CAMBIO DETECTADO $ANTERIOR → $ETIQUETA" >> /tmp/curso_agentes/rutina/vigila/log/vigilancia.log
fi
echo "$ETIQUETA" > /tmp/curso_agentes/rutina/vigila/hash.txt
