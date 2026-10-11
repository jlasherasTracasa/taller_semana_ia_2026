#!/usr/bin/env python3
"""Genera certificados en PDF a partir de nombres.csv usando reportlab."""

import csv
import os
from datetime import date

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

CSV_FILE = "nombres.csv"
OUT_DIR = "certificados"


def dibujar_certificado(nombre: str, curso: str, horas: str, ruta: str) -> None:
    c = canvas.Canvas(ruta, pagesize=A4)
    ancho, alto = A4

    # Marco doble sobrio
    c.setStrokeColorRGB(0.15, 0.15, 0.15)
    c.setLineWidth(2)
    c.rect(1.2 * cm, 1.2 * cm, ancho - 2.4 * cm, alto - 2.4 * cm)
    c.setLineWidth(0.7)
    c.rect(1.45 * cm, 1.45 * cm, ancho - 2.9 * cm, alto - 2.9 * cm)

    # Titulo
    c.setFont("Times-Bold", 32)
    c.drawCentredString(ancho / 2, alto - 5.5 * cm, "CERTIFICADO")
    c.setFont("Times-Roman", 14)
    c.drawCentredString(ancho / 2, alto - 6.6 * cm, "DE ASISTENCIA")

    c.setLineWidth(0.8)
    c.line(5 * cm, alto - 7.3 * cm, ancho - 5 * cm, alto - 7.3 * cm)

    # Cuerpo
    c.setFont("Times-Italic", 13)
    c.drawCentredString(ancho / 2, alto - 10.5 * cm, "Se certifica que")

    c.setFont("Times-Bold", 26)
    c.drawCentredString(ancho / 2, alto - 12.2 * cm, nombre)

    c.setFont("Times-Roman", 12)
    c.drawCentredString(
        ancho / 2, alto - 13.8 * cm, "ha completado el curso"
    )

    c.setFont("Times-Bold", 16)
    c.drawCentredString(ancho / 2, alto - 15.0 * cm, curso)

    c.setFont("Times-Roman", 12)
    c.drawCentredString(
        ancho / 2, alto - 16.2 * cm,
        f"con una duracion de {horas} horas",
    )

    # Pie: fecha de emision
    c.setFont("Times-Roman", 10)
    c.drawCentredString(
        ancho / 2, 3.2 * cm,
        f"Expedido el {date.today().strftime('%d/%m/%Y')}",
    )

    c.showPage()
    c.save()


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)

    personas = []
    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            nombre = fila["nombre"].strip()
            personas.append((nombre, fila["curso"].strip(), fila["horas"].strip()))
            ruta = os.path.join(OUT_DIR, f"certificado_{nombre}.pdf")
            dibujar_certificado(nombre, fila["curso"].strip(), fila["horas"].strip(), ruta)
            print(f"Generado: {ruta}")

    # Verificacion: un PDF por fila y cada uno con su nombre
    pdfs = sorted(p for p in os.listdir(OUT_DIR) if p.endswith(".pdf"))
    esperados = sorted(f"certificado_{n}.pdf" for n, _, _ in personas)
    assert len(personas) == len(set(n for n, _, _ in personas)), "Nombres duplicados en el CSV"
    assert pdfs == esperados, f"Desajuste de ficheros:\n{pdfs}\nvs\n{esperados}"

    from pypdf import PdfReader  # verificacion de contenido

    for nombre, _, _ in personas:
        reader = PdfReader(os.path.join(OUT_DIR, f"certificado_{nombre}.pdf"))
        texto = "".join(page.extract_text() or "" for page in reader.pages)
        assert nombre in texto, f"'{nombre}' no aparece en su certificado"

    print(f"\nOK: {len(personas)} PDFs generados en '{OUT_DIR}/', uno por fila del CSV, todos con su nombre.")


if __name__ == "__main__":
    main()
