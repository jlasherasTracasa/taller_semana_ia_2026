#!/usr/bin/env python3
"""Valida que un acta sigue el formato de la skill acta-reunion. Uso: python3 validar_acta.py actas/AAAA-MM-DD_acta.md"""
import os, re, sys

ruta = sys.argv[1] if len(sys.argv) > 1 else ""
errores = []
if not re.search(r"actas/\d{4}-\d{2}-\d{2}_acta\.md$", ruta.replace("\\", "/")):
    errores.append("el fichero debe llamarse actas/AAAA-MM-DD_acta.md")
texto = open(ruta, encoding="utf-8").read() if os.path.exists(ruta) else ""
if not texto:
    errores.append(f"no encuentro {ruta!r}")
for seccion in ("## Orden del día", "## Acuerdos", "## Próxima reunión"):
    if seccion not in texto:
        errores.append(f"falta la sección «{seccion}»")
for campo in ("**Lugar y hora:**", "**Asistentes:**", "**Ausencias excusadas:**", "Firmado:"):
    if campo not in texto:
        errores.append(f"falta «{campo}»")
cab = "| N.º | Acuerdo | Votación | Responsable | Fecha límite |"
if cab not in texto:
    errores.append("la tabla de acuerdos no tiene las columnas exactas: " + cab)
filas = [l for l in texto.splitlines() if re.match(r"\|\s*\d+\s*\|", l)]
if len(filas) < 3:
    errores.append(f"hay {len(filas)} acuerdos en la tabla; revisa la transcripción, seguro que hay más")
if re.search(r"\b\d{1,2}/\d{1,2}/\d{2}\b(?!\d)", texto):
    errores.append("usa fechas con el año completo (dd/mm/aaaa)")
print("ACTA VÁLIDA" if not errores else "ERRORES:\n- " + "\n- ".join(errores))
sys.exit(1 if errores else 0)
