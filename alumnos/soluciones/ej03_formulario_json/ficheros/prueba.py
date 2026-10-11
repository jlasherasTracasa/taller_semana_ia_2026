"""Envío de prueba con urllib (sin curl).

Lee el puerto real desde puerto.txt (el servidor lo escribe al arrancar).
"""

import json
import os
import urllib.request
import urllib.parse

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, "puerto.txt")) as f:
    puerto = int(f.read().strip())

datos = urllib.parse.urlencode({
    "nombre": "Ada Lovelace",
    "correo": "ada@example.com",
    "mensaje": "Envío de prueba del formulario.",
}).encode("utf-8")

peticion = urllib.request.Request(
    f"http://127.0.0.1:{puerto}/enviar",
    data=datos,
    method="POST",
)
with urllib.request.urlopen(peticion, timeout=10) as respuesta:
    print("Estado:", respuesta.status)
    print("Respuesta:", respuesta.read().decode("utf-8"))
