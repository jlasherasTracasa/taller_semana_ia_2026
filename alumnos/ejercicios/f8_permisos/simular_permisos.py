#!/usr/bin/env python3
"""Simula cómo decidiría opencode cada orden de comandos_prueba.txt con un opencode.json dado.
Regla de opencode: los patrones usan * (cualquier cosa) y ? (un carácter) y GANA LA ÚLTIMA REGLA QUE COINCIDE.
Uso: python3 simular_permisos.py opencode_inseguro.json        (o tu opencode_seguro.json)
"""
import json, re, sys

cfg = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "opencode_inseguro.json", encoding="utf-8"))
reglas = cfg.get("permission", {}).get("bash", "ask")
if isinstance(reglas, str):
    reglas = {"*": reglas}


def coincide(orden, patron):
    """Comodines de opencode: * = cualquier cosa (también vacío), ? = un carácter. Nada más."""
    rx = "".join(".*" if c == "*" else "." if c == "?" else re.escape(c) for c in patron)
    return re.fullmatch(rx, orden, re.S) is not None


def decide(orden):
    decision = "ask"  # si ninguna regla coincide
    for patron, accion in reglas.items():  # en orden: la última que coincide gana
        if coincide(orden, patron):
            decision = accion
    return decision


aciertos = total = 0
for linea in open("comandos_prueba.txt", encoding="utf-8"):
    if not linea.strip() or linea.startswith("#"):
        continue
    esperado, orden = [x.strip() for x in linea.split("|", 1)]
    real = decide(orden)
    bien = real == esperado
    aciertos += bien
    total += 1
    print(f"{'✅' if bien else '❌'} {real:5} (esperado {esperado:5})  {orden}")
print(f"\n{aciertos}/{total} órdenes con la decisión esperada")
otros = {k: v for k, v in cfg.get("permission", {}).items() if k != "bash"}
print("Otros permisos:", otros)
if re.search(r'"apiKey"\s*:\s*"(?!\{env:)', json.dumps(cfg)):
    print("⚠️  Hay una apiKey escrita en el fichero: debería ser {env:NOMBRE_VARIABLE}")
sys.exit(0 if aciertos == total else 1)
