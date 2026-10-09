import csv
import os

RUTA_CSV = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ventas_tienda.csv")
RUTA_SALIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "informe_semanal.txt")


def formatear_miles(n):
    """Formatea un número con puntos como separador de miles (29.800)."""
    return f"{n:,}".replace(",", ".")


def cargar_datos(ruta):
    """Lee el CSV y devuelve (categorias, filas). Cada fila es {categoria: valor}."""
    with open(ruta, newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        categorias = lector.fieldnames[1:]
        filas = [
            {"mes": fila["mes"], **{cat: int(fila[cat]) for cat in categorias}}
            for fila in lector
        ]
    return categorias, filas


def main():
    categorias, filas = cargar_datos(RUTA_CSV)

    lineas = ["INFORME SEMANAL DE VENTAS", "=" * 30, ""]

    # Total por categoría (calculado desde el CSV)
    lineas.append("Total por categoría:")
    for cat in categorias:
        total = sum(fila[cat] for fila in filas)
        lineas.append(f"  {cat}: {formatear_miles(total)}")
    lineas.append("")

    # Mes con más ventas (suma de todas las categorías)
    totales_mes = {
        fila["mes"]: sum(fila[cat] for cat in categorias) for fila in filas
    }
    mejor_mes = max(totales_mes, key=totales_mes.get)
    lineas.append(
        f"Mes con más ventas: {mejor_mes} ({formatear_miles(totales_mes[mejor_mes])})"
    )
    lineas.append("")

    # Tendencia del primer al último mes en porcentaje
    meses = list(totales_mes)
    primero = totales_mes[meses[0]]
    ultimo = totales_mes[meses[-1]]
    tendencia = (ultimo - primero) / primero * 100
    lineas.append(
        f"Tendencia {meses[0]} → {meses[-1]}: {tendencia:+.1f} %"
    )

    with open(RUTA_SALIDA, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas) + "\n")

    print("\n".join(lineas))
    print(f"\nInforme guardado en: {RUTA_SALIDA}")


if __name__ == "__main__":
    main()
