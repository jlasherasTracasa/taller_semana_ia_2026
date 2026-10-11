#!/usr/bin/env python3
"""Genera deck_ferias_corregido.pptx copiando el original y aplicando
solo correcciones de texto ortotipográficas. El original no se modifica.
"""
import shutil
import zipfile

SRC = "deck_ferias.pptx"
DST = "deck_ferias_corregido.pptx"

# (fichero dentro del zip, texto original, texto corregido)
FIXES = {
    "ppt/slides/slide1.xml": [
        ("El certamen de artesaNIA de Tafalla",
         "El certamen de artesanía de Tafalla"),
    ],
    "ppt/slides/slide2.xml": [
        ("Del 12 al 15 de SEPTIEMBRE", "Del 12 al 15 de septiembre"),
        ("entrada gratuita", "Entrada gratuita"),
    ],
    "ppt/slides/slide3.xml": [
        ("taller de cesteria (sabado 10:00)",
         "Taller de cestería (sábado 10:00)"),
        ("CONCIERTO de txistu , domingo", "Concierto de txistu, domingo"),
        ("Degustación de quesos con D.O. Roncal  ",
         "Degustación de quesos con D.O. Roncal"),
    ],
    "ppt/slides/slide4.xml": [
        ("Organizacion", "Organización"),
        ("Telefono 948 70 00 00  (extension 3)",
         "Teléfono 948 70 00 00 (extensión 3)"),
    ],
}


def main():
    with zipfile.ZipFile(SRC) as zin:
        names = zin.namelist()
        data = {n: zin.read(n) for n in names}
        infos = {i.filename: i for i in zin.infolist()}

        applied = []
        for name, fixes in FIXES.items():
            xml = data[name].decode("utf-8")
            for old, new in fixes:
                count = xml.count(old)
                if count != 1:
                    raise SystemExit(
                        f"ERROR: {name}: {count} coincidencias de {old!r}")
                xml = xml.replace(old, new)
                applied.append((name, old, new))
            data[name] = xml.encode("utf-8")

        with zipfile.ZipFile(DST, "w", zipfile.ZIP_DEFLATED) as zout:
            for n in names:
                info = infos[n]
                out = zipfile.ZipInfo(n, date_time=info.date_time)
                out.compress_type = zipfile.ZIP_DEFLATED
                out.external_attr = info.external_attr
                zout.writestr(out, data[n])

    for name, old, new in applied:
        print(f"[ok] {name}: {old!r} -> {new!r}")
    print(f"\nEscrito {DST} con {len(applied)} correcciones.")


if __name__ == "__main__":
    main()
