"""Genera ejercicios.json (datos de las tarjetas de ejercicios del deck) a partir del kit del alumno.

Título, tiempo y dificultad salen de ejercicios/<id>/ENUNCIADO.md; «validado» es True cuando
soluciones/<id>/salida.txt contiene una ejecución real (y no terminó con código de error).
Uso: python3 extraer_ejercicios.py   (desde cualquier carpeta)
"""
import json
import pathlib
import re

AQUI = pathlib.Path(__file__).resolve().parent
KIT = AQUI.parents[1] / "alumnos"


def seccion(texto, nombre):
    m = re.search(rf"^## {nombre}\s*\n+(.+?)\s*$", texto, re.M | re.I)
    return m.group(1).strip() if m else ""


def validado(sol):
    f = sol / "salida.txt"
    if not f.exists() or not f.read_text().strip():
        return False
    cab = f.read_text().splitlines()[0]
    return not re.search(r"código [1-9]", cab)


filas = []
for d in sorted((KIT / "ejercicios").iterdir()):
    t = (d / "ENUNCIADO.md").read_text()
    filas.append({
        "id": d.name,
        "titulo": t.splitlines()[0].lstrip("# ").strip(),
        "tiempo": seccion(t, "Tiempo estimado"),
        "dificultad": seccion(t, "Dificultad"),
        "validado": validado(KIT / "soluciones" / d.name),
    })

(AQUI / "ejercicios.json").write_text(json.dumps(filas, ensure_ascii=False, indent=1) + "\n")
print(f"{len(filas)} ejercicios · {sum(f['validado'] for f in filas)} validados · sin validar: "
      + ", ".join(f["id"] for f in filas if not f["validado"]))
