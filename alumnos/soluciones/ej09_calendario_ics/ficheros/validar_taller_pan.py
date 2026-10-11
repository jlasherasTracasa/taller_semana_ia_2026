"""Valida taller_pan.ics leyendolo con la biblioteca icalendar de Python.

Uso: python3 validar_taller_pan.py
Requiere: pip install icalendar
"""
import sys

from icalendar import Calendar

FICHERO = "taller_pan.ics"

with open(FICHERO, "rb") as f:
    cal = Calendar.from_ical(f.read())

errores = []

# --- Comprobaciones del VCALENDAR ---
if cal.get("VERSION") != "2.0":
    errores.append("VERSION debe ser 2.0")
if cal.get("PRODID") is None:
    errores.append("Falta PRODID")

zonas = [c for c in cal.walk("VTIMEZONE")]
eventos = [c for c in cal.walk("VEVENT")]

if len(zonas) != 1 or zonas[0]["TZID"] != "Europe/Madrid":
    errores.append("Se esperaba un VTIMEZONE con TZID=Europe/Madrid")

if len(eventos) != 1:
    errores.append(f"Se esperaba 1 VEVENT y hay {len(eventos)}")
else:
    ev = eventos[0]
    inicio = ev.decoded("DTSTART")   # datetime con tzinfo Europe/Madrid (CET, +0100)
    fin = ev.decoded("DTEND")

    print("Resumen      :", ev["SUMMARY"])
    print("Inicio (DTSTART):", inicio, "| tz:", inicio.tzinfo)
    print("Fin    (DTEND)  :", fin, "| tz:", fin.tzinfo)
    print("Lugar        :", ev["LOCATION"])

    # Fecha y hora extraidas del correo (sabado 28 -> ano/mes de la cabecera Date: Nov 2026)
    if (inicio.year, inicio.month, inicio.day, inicio.hour, inicio.minute) != (2026, 11, 28, 10, 0):
        errores.append(f"DTSTART inesperado: {inicio}")
    if (fin.year, fin.month, fin.day, fin.hour, fin.minute) != (2026, 11, 28, 12, 30):
        errores.append(f"DTEND inesperado: {fin}")
    if fin - inicio != __import__("datetime").timedelta(hours=2, minutes=30):
        errores.append("La duracion no es de 2 horas y 30 minutos")
    if inicio.utcoffset() != __import__("datetime").timedelta(hours=1):
        errores.append("El 28/11/2026 en Europe/Madrid deberia ser CET (+01:00)")

if errores:
    print("\nERRORES:")
    for e in errores:
        print(" -", e)
    sys.exit(1)

print("\nOK: taller_pan.ics es valido (icalendar lo ha parseado y cumple los datos del correo)")
