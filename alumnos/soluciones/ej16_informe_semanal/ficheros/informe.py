import csv
import os


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, "ventas_tienda.csv")
    output_path = os.path.join(base_dir, "informe_semanal.txt")

    # Leer los datos del CSV
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        categories = [name for name in reader.fieldnames if name != "mes"]
        rows = list(reader)

    if not rows:
        raise ValueError("El CSV no contiene datos.")

    # Total por categoría
    totals_by_category = {
        cat: sum(int(row[cat]) for row in rows) for cat in categories
    }

    # Total por mes (para hallar el mes con más ventas)
    totals_by_month = {
        row["mes"]: sum(int(row[cat]) for cat in categories) for row in rows
    }

    best_month = max(totals_by_month, key=totals_by_month.get)

    # Tendencia de enero a junio (variación porcentual del total)
    first_month_total = totals_by_month[rows[0]["mes"]]
    last_month_total = totals_by_month[rows[-1]["mes"]]
    trend_pct = (
        (last_month_total - first_month_total) / first_month_total * 100
    )

    # Escribir el informe
    lines = []
    lines.append("INFORME SEMANAL DE VENTAS")
    lines.append("")
    lines.append("Total por categoria:")
    for cat in categories:
        lines.append(f"  {cat}: {totals_by_category[cat]}")
    lines.append("")
    lines.append(f"Mes con mas ventas: {best_month} ({totals_by_month[best_month]})")
    lines.append(
        f"Tendencia de enero a junio: {trend_pct:+.2f}% "
        f"({first_month_total} -> {last_month_total})"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"Informe generado en {output_path}")
    print()
    print("\n".join(lines))


if __name__ == "__main__":
    main()
