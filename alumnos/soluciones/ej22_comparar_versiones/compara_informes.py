import difflib
from docx import Document


def texto(path):
    doc = Document(path)
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]


a = texto("informe_v1.docx")
b = texto("informe_v2.docx")

sm = difflib.SequenceMatcher(None, a, b)
print(f"v1: {len(a)} parrafos | v2: {len(b)} parrafos | ratio: {sm.ratio():.3f}")
print("=" * 70)

for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        continue
    viejos = a[i1:i2]
    nuevos = b[j1:j2]
    print(f"\n--- {tag.upper()} ---")
    for p in viejos:
        print(f"  VIEJO: {p}")
    for p in nuevos:
        print(f"  NUEVO: {p}")
