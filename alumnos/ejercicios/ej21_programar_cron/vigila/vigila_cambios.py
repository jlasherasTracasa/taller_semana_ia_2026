#!/usr/bin/env python3
"""Comprueba si https://example.com ha cambiado y lo apunta en log/vigilancia.log (script del EJ 20).

Funciona igual en Windows, macOS y Linux, y se lance desde donde se lance: las rutas salen de la ubicación del script.
"""
import datetime, hashlib, os, urllib.request

URL = "https://example.com"
AQUI = os.path.dirname(os.path.abspath(__file__))
HASH = os.path.join(AQUI, "hash.txt")
LOG = os.path.join(AQUI, "log", "vigilancia.log")

os.makedirs(os.path.dirname(LOG), exist_ok=True)
ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
try:
    with urllib.request.urlopen(URL, timeout=30) as r:
        nuevo = hashlib.sha256(r.read()).hexdigest()
except OSError as e:
    estado, nuevo = f"ERROR al descargar: {e}", None
else:
    viejo = open(HASH, encoding="utf-8").read().strip() if os.path.exists(HASH) else None
    estado = "inicio" if viejo is None else ("sin cambios" if viejo == nuevo else "CAMBIO DETECTADO")
    open(HASH, "w", encoding="utf-8").write(nuevo)
with open(LOG, "a", encoding="utf-8") as f:
    f.write(f"{ahora} {estado} {URL}\n")
print(f"{ahora} {estado}")
