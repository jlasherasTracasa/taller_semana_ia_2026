import csv
import re
import unicodedata

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

PAGE_W, PAGE_H = landscape(A4)
BORDER = 1.2 * cm


def slug(nombre: str) -> str:
    texto = unicodedata.normalize("NFKD", nombre)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = re.sub(r"[^A-Za-z0-9]+", "_", texto).strip("_")
    return texto.lower()


def draw(c, nombre, curso, horas):
    # Marco doble sobrio
    c.setStrokeColorRGB(0.25, 0.25, 0.25)
    c.setLineWidth(3)
    c.rect(BORDER, BORDER, PAGE_W - 2 * BORDER, PAGE_H - 2 * BORDER)
    c.setLineWidth(1)
    c.rect(BORDER + 0.25 * cm, BORDER + 0.25 * cm,
           PAGE_W - 2 * BORDER - 0.5 * cm, PAGE_H - 2 * BORDER - 0.5 * cm)

    cx = PAGE_W / 2
    y = PAGE_H - 4.5 * cm

    c.setFont("Times-Roman", 34)
    c.drawCentredString(cx, y, "CERTIFICADO DE ASISTENCIA")

    c.setFont("Times-Roman", 14)
    y -= 2.2 * cm
    c.drawCentredString(cx, y, "Se certifica que")

    c.setFont("Times-Bold", 30)
    y -= 2.6 * cm
    c.drawCentredString(cx, y, nombre)
    c.setLineWidth(1)
    half = max(c.stringWidth(nombre, "Times-Bold", 30) / 2 + 1 * cm, 9 * cm)
    c.line(cx - half, y - 0.35 * cm, cx + half, y - 0.35 * cm)

    c.setFont("Times-Roman", 16)
    y -= 2.4 * cm
    c.drawCentredString(cx, y, "ha asistido al curso")

    c.setFont("Times-Bold", 20)
    y -= 1.8 * cm
    c.drawCentredString(cx, y, f"«{curso}»")

    c.setFont("Times-Roman", 16)
    y -= 1.6 * cm
    c.drawCentredString(cx, y, f"con una duración total de {horas} horas.")

    c.setFont("Times-Roman", 12)
    y = BORDER + 2.2 * cm
    c.drawRightString(PAGE_W - 3.5 * cm, y, "Fdo.: La Dirección del curso")
    c.line(PAGE_W - 8.5 * cm, y + 0.5 * cm, PAGE_W - 2.5 * cm, y + 0.5 * cm)

    c.showPage()


with open("nombres.csv", newline="", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

for fila in filas:
    archivo = f"certificado_asistencia_{slug(fila['nombre'])}.pdf"
    c = canvas.Canvas(archivo, pagesize=landscape(A4))
    c.setTitle(f"Certificado de asistencia - {fila['nombre']}")
    draw(c, fila["nombre"], fila["curso"], fila["horas"])
    c.save()
    print("Generado:", archivo)
