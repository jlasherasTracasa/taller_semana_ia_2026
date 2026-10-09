#!/usr/bin/env python3
"""Genera ventas.pptx a partir de ventas_tienda.csv.

Los totales se calculan SIEMPRE leyendo el CSV, nunca a mano.
"""

import csv

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches, Pt

CSV_FILE = "ventas_tienda.csv"
CHART_FILE = "grafico_ventas.png"
PPTX_FILE = "ventas.pptx"

# ---------- 1. Leer el CSV y calcular totales ----------

with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    filas = list(reader)

meses = [fila["mes"].capitalize() for fila in filas]
categorias = [c for c in filas[0] if c != "mes"]

datos = {cat: [int(fila[cat]) for fila in filas] for cat in categorias}

totales = {cat: sum(valores) for cat, valores in datos.items()}
total_general = sum(totales.values())

print("Totales calculados desde el CSV:")
for cat in categorias:
    print(f"  {cat}: {totales[cat]:,} €".replace(",", "."))
print(f"  TOTAL: {total_general:,} €".replace(",", "."))

# ---------- 2. Gráfico de líneas con matplotlib ----------

fig, ax = plt.subplots(figsize=(9, 5), dpi=150)

for cat in categorias:
    ax.plot(meses, datos[cat], marker="o", linewidth=2, label=cat.capitalize())

ax.set_title("Ventas mensuales por categoría (enero–junio)", fontsize=14)
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas (€)")
ax.legend(title="Categoría")
ax.grid(True, linestyle="--", alpha=0.4)
fig.tight_layout()
fig.savefig(CHART_FILE)
plt.close(fig)
print(f"Gráfico guardado en {CHART_FILE}")

# ---------- 3. Presentación con python-pptx ----------

prs = Presentation()

# Diapositiva 1: portada
diapo = prs.slides.add_slide(prs.slide_layouts[0])
diapo.shapes.title.text = "Ventas de la tienda"
diapo.placeholders[1].text = "Enero – Junio · Hogar, Textil y Bazar"

# Diapositiva 2: gráfico como imagen
diapo = prs.slides.add_slide(prs.slide_layouts[5])  # título + contenido
diapo.shapes.title.text = "Evolución mensual por categoría"
diapo.shapes.add_picture(CHART_FILE, Inches(1.5), Inches(1.4), width=Inches(7))

# Diapositiva 3: tabla de totales (calculados, no memorizados)
diapo = prs.slides.add_slide(prs.slide_layouts[5])
diapo.shapes.title.text = "Totales por categoría"

n_filas = len(categorias) + 2  # cabecera + categorías + total general
tabla_shape = diapo.shapes.add_table(n_filas, 2, Inches(2.5), Inches(1.6), Inches(5), Inches(0.8 * n_filas))
tabla = tabla_shape.table

tabla.cell(0, 0).text = "Categoría"
tabla.cell(0, 1).text = "Total (€)"

for i, cat in enumerate(categorias, start=1):
    tabla.cell(i, 0).text = cat.capitalize()
    tabla.cell(i, 1).text = f"{totales[cat]:,}".replace(",", ".")

tabla.cell(n_filas - 1, 0).text = "TOTAL GENERAL"
tabla.cell(n_filas - 1, 1).text = f"{total_general:,}".replace(",", ".")

for celda in tabla.cell(n_filas - 1, 0), tabla.cell(n_filas - 1, 1):
    for parrafo in celda.text_frame.paragraphs:
        for run in parrafo.runs:
            run.font.bold = True

prs.save(PPTX_FILE)
print(f"Presentación guardada en {PPTX_FILE}")
