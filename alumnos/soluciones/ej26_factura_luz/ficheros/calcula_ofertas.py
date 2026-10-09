"""Calcula el coste anual 2025 de cada oferta de luz (sin IVA ni impuesto eléctrico)."""
import csv

# --- consumo mensual ---
consumo = []
with open("consumo_2025.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        consumo.append({
            "mes": row["mes"],
            "punta": float(row["punta_kwh"]),
            "llano": float(row["llano_kwh"]),
            "valle": float(row["valle_kwh"]),
        })

POTENCIA_KW = 4.6
DIAS = 365

tot_punta = sum(c["punta"] for c in consumo)
tot_llano = sum(c["llano"] for c in consumo)
tot_valle = sum(c["valle"] for c in consumo)
total_kwh = tot_punta + tot_llano + tot_valle

coste_potencia_a = POTENCIA_KW * 0.090 * DIAS
coste_potencia_b = POTENCIA_KW * 0.080 * DIAS
coste_potencia_c = POTENCIA_KW * 0.095 * DIAS

energia_a = total_kwh * 0.145
energia_b = tot_punta * 0.210 + tot_llano * 0.140 + tot_valle * 0.085
energia_c = total_kwh * 0.129

cuota_c = 5.00 * 12

total_a = energia_a + coste_potencia_a
total_b = energia_b + coste_potencia_b
total_c = energia_c + coste_potencia_c + cuota_c

print(f"Consumo anual: punta={tot_punta:.0f} llano={tot_llano:.0f} valle={tot_valle:.0f} kWh (total {total_kwh:.0f})")
print(f"Coste potencia (4.6 kW x 365 dias): A={coste_potencia_a:.2f}  B={coste_potencia_b:.2f}  C={coste_potencia_c:.2f}")
print(f"Cuotas fijas: C={cuota_c:.2f}")
print()
print(f"Oferta A: energia={energia_a:8.2f}  total={total_a:8.2f} eur")
print(f"Oferta B: energia={energia_b:8.2f}  total={total_b:8.2f} eur")
print(f"Oferta C: energia={energia_c:8.2f} + cuota {cuota_c:.2f}  total={total_c:8.2f} eur")

precios = {"A": total_a, "B": total_b, "C": total_c}
mejor = min(precios, key=precios.get)
print()
print(f"MAS BARATA: Oferta {mejor}")
for k in sorted(precios):
    if k != mejor:
        print(f"  Ahorro frente a {k}: {precios[k] - precios[mejor]:.2f} eur/año")
