import csv
from pptx import Presentation
from pptx.util import Inches, Pt

# --- leer CSV (nunca de memoria) ---
with open("datos/ventas_tienda.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

cats = ["hogar", "textil", "bazar"]
tot_cat = {c: sum(int(r[c]) for r in rows) for c in cats}
total = sum(tot_cat.values())
primero, ultimo = rows[0], rows[-1]
tot_prim = sum(int(primero[c]) for c in cats)
tot_ult = sum(int(ultimo[c]) for c in cats)
var_pct = (tot_ult - tot_prim) / tot_prim * 100

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank = prs.slide_layouts[6]

def add_text(slide, text, left, top, width, height, size=28, bold=False):
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; r = p.add_run(); r.text = text
    r.font.size = Pt(size); r.font.bold = bold
    return tb

# --- S1 Portada ---
s = prs.slides.add_slide(blank)
add_text(s, "Informe semanal de ventas", 1.0, 2.4, 11.3, 1.4, size=44, bold=True)
add_text(s, f"Último mes del CSV: {ultimo['mes']}", 1.0, 3.9, 11.3, 0.8, size=28)

# --- S2 Totales por categoría y total general ---
s = prs.slides.add_slide(blank)
add_text(s, "Total por categoría y total general", 0.7, 0.5, 11.9, 1.0, size=34, bold=True)
y = 2.0
for c in cats:
    add_text(s, f"{c}: {tot_cat[c]:,} €".replace(",", "."), 1.2, y, 10.5, 0.8, size=30)
    y += 1.0
add_text(s, f"TOTAL GENERAL: {total:,} €".replace(",", "."), 1.2, y + 0.3, 10.5, 1.0,
         size=34, bold=True)

# --- S3 Tendencia ---
s = prs.slides.add_slide(blank)
add_text(s, "Tendencia del total mensual", 0.7, 0.5, 11.9, 1.0, size=34, bold=True)
add_text(s, f"{primero['mes']} ({primero['mes']}): {tot_prim:,} €".replace(",", "."),
         1.2, 2.2, 10.9, 0.8, size=30)
add_text(s, f"{ultimo['mes']}: {tot_ult:,} €".replace(",", "."), 1.2, 3.1, 10.9, 0.8, size=30)
signo = "+" if var_pct >= 0 else ""
add_text(s, f"Variación: {signo}{var_pct:.1f} %", 1.2, 4.2, 10.9, 1.0, size=40, bold=True)

prs.save("informe_semanal.pptx")
print("guardado informe_semanal.pptx")

# --- verificación con python-pptx (criterio del enunciado) ---
chk = Presentation("informe_semanal.pptx")
n_slides = len(chk.slides.__iter__.__self__._sldIdLst)
print("diapositivas:", n_slides)

# releer valores y comprobar suma categorias == total general
def texts(slide):
    out = []
    for sh in slide.shapes:
        if sh.has_text_frame:
            out.append(sh.text_frame.text)
    return out

full = "\n".join(t for sl in chk.slides for t in texts(sl))
sum_cats = sum(tot_cat.values())
ok_slides = len(list(chk.slides)) == 3
ok_sum = sum_cats == total
print("suma categorias:", sum_cats, "| total general:", total, "| iguales:", ok_sum)
import re
m = re.search(r"TOTAL GENERAL: ([\d.]+) €", full)
ok_text = m is not None and int(m.group(1).replace(".", "")) == total
print("texto del total en el pptx coincide:", ok_text)

if not (ok_slides and ok_sum and ok_text):
    raise SystemExit("ERROR: la verificacion no cuadra, revisar antes de entregar")
print("VERIFICACION OK: 3 diapositivas y las cifras cuadran")
