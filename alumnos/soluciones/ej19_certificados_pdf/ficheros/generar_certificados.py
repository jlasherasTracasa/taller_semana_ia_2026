"""EJ 19 - Genera un PDF de certificado por persona a partir de nombres.csv."""
import csv
import os

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas

ANCHO, ALTO = A4


def generar_certificado(nombre, curso, horas, ruta):
    c = canvas.Canvas(ruta, pagesize=A4)

    # Borde sobrio (doble marco)
    c.setStrokeColorRGB(0.25, 0.25, 0.25)
    c.setLineWidth(2)
    c.rect(1.5 * cm, 1.5 * cm, ANCHO - 3 * cm, ALTO - 3 * cm)
    c.setLineWidth(0.75)
    c.rect(1.7 * cm, 1.7 * cm, ANCHO - 3.4 * cm, ALTO - 3.4 * cm)

    # Encabezado
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(ANCHO / 2, ALTO - 4 * cm, "CERTIFICADO DE ASISTENCIA")
    c.setFont("Helvetica", 12)
    c.drawCentredString(ANCHO / 2, ALTO - 5.2 * cm,
                        "Centro de Mayores · Fin de curso")

    # Línea separadora
    c.setLineWidth(1)
    c.line(6 * cm, ALTO - 6 * cm, ANCHO - 6 * cm, ALTO - 6 * cm)

    # Cuerpo
    y = ALTO / 2 + 1.5 * cm
    c.setFont("Helvetica", 12)
    c.drawCentredString(ANCHO / 2, y + 1.8 * cm, "Se certifica que")
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(ANCHO / 2, y, nombre)
    c.setFont("Helvetica", 12)
    c.drawCentredString(ANCHO / 2, y - 1.2 * cm, "ha participado en la actividad:")

    c.setFont("Helvetica-BoldOblique", 16)
    c.drawCentredString(ANCHO / 2, y - 2.6 * cm, f"«{curso}»")

    # Horas, al pie
    c.setFont("Helvetica", 12)
    c.drawCentredString(ANCHO / 2, 4.5 * cm,
                        f"Duración del curso: {horas} horas")

    # Firma
    c.setFont("Helvetica-Oblique", 11)
    c.drawRightString(ANCHO - 3 * cm, 3 * cm, "La Dirección")

    c.showPage()
    c.save()


def main():
    with open("nombres.csv", newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))

    os.makedirs("certificados", exist_ok=True)

    for fila in filas:
        nombre = fila["nombre"].strip()
        nombre_fichero = nombre.replace(" ", "_")
        ruta = os.path.join("certificados", f"certificado_{nombre_fichero}.pdf")
        generar_certificado(nombre, fila["curso"].strip(), fila["horas"].strip(), ruta)
        print(f"Generado: {ruta}")

    # Verificación: un PDF por fila, sin duplicados
    esperados = {f"certificado_{f['nombre'].strip().replace(' ', '_')}.pdf"
                 for f in filas}
    generados = set(os.listdir("certificados"))
    pdfs = {x for x in generados if x.endswith(".pdf")}

    print(f"\nFilas del CSV: {len(filas)} | PDFs generados: {len(pdfs)}")
    if pdfs == esperados and len(pdfs) == len(filas):
        print("✔ Verificación correcta: un PDF por fila, cada uno con su nombre.")
    else:
        print("✘ Fallos:", esperados ^ pdfs)


if __name__ == "__main__":
    main()
