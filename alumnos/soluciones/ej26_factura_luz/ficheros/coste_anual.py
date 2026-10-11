#!/usr/bin/env python3
"""Compara el coste anual de tres ofertas de luz con el consumo real de 2025."""
import csv

POTENCIA_KW = 4.6
DIAS = 365
MESES = 12

with open("consumo_2025.csv", newline="", encoding="utf-8") as f:
    filas = list(csv.DictReader(f))

punta = sum(int(r["punta_kwh"]) for r in filas)
llano = sum(int(r["llano_kwh"]) for r in filas)
valle = sum(int(r["valle_kwh"]) for r in filas)
total_kwh = punta + llano + valle

def coste(energia_punta, energia_llano, energia_valle, precio_pot_dia, cuota_mes):
    e = punta * energia_punta + llano * energia_llano + valle * energia_valle
    p = POTENCIA_KW * precio_pot_dia * DIAS
    c = cuota_mes * MESES
    return e, p, c, e + p + c

ofertas = {
    "A · Luz Plana (Ebro Energía)": coste(0.145, 0.145, 0.145, 0.090, 0),
    "B · Tres Periodos (Arga Luz)": coste(0.210, 0.140, 0.085, 0.080, 0),
    "C · Ahorro Club (Bidasoa Eléctrica)": coste(0.129, 0.129, 0.129, 0.095, 5.0),
}

print(f"Consumo anual: punta {punta} kWh, llano {llano} kWh, valle {valle} kWh (total {total_kwh} kWh)\n")
print(f"{'Oferta':38s} {'Energía':>9s} {'Potencia':>9s} {'Cuotas':>7s} {'Total':>9s}")
for nombre, (e, p, c, t) in ofertas.items():
    print(f"{nombre:38s} {e:9.2f} {p:9.2f} {c:7.2f} {t:9.2f} €")

mejor = min(ofertas.items(), key=lambda kv: kv[1][3])
print(f"\nMás barata: {mejor[0]} -> {mejor[1][3]:.2f} €")
for nombre, (_, _, _, t) in ofertas.items():
    if nombre != mejor[0]:
        print(f"Ahorro frente a {nombre}: {t - mejor[1][3]:.2f} €")
