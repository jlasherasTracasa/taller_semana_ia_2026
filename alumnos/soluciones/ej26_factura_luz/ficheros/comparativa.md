# Comparativa de ofertas de luz · 2025

Cálculos hechos con el consumo real de `consumo_2025.csv` y los precios de `ofertas.md`
(mediante el script `coste_anual.py`). Sin IVA ni impuesto eléctrico, como pide el enunciado.

**Datos de partida:** consumo anual de 3.814 kWh (punta 998 · llano 1.157 · valle 1.659),
potencia contratada de 4,6 kW los 365 días.

## Coste anual por oferta

| Oferta | Energía | Potencia | Cuotas fijas | **Total anual** |
|---|---:|---:|---:|---:|
| A · «Luz Plana» (Ebro Energía) | 553,03 € | 151,11 € | 0,00 € | **704,14 €** |
| B · «Tres Periodos» (Arga Luz) | 512,58 € | 134,32 € | 0,00 € | **646,89 €** |
| C · «Ahorro Club» (Bidasoa Eléctrica) | 492,01 € | 159,50 € | 60,00 € | **711,51 €** |

**La más barata es la Oferta B (Arga Luz), con 646,89 € al año.**

- Ahorro frente a la A: **57,25 €**
- Ahorro frente a la C: **64,62 €**

## ¿Es verdad lo que dice cada folleto?

- **Oferta C dice «¡La más barata del mercado!»**: **FALSO.** Es precisamente la más cara
  (711,51 €). Su precio por kWh es el más bajo (0,129 €/kWh), pero la cuota fija de 5 €/mes
  (60 € al año) y la potencia algo más cara se lo comen.
- **Oferta A («Luz Plana»)**: no hace promesas de precio, y su coste queda en el término
  medio (704,14 €). Coherente, aunque no destaca en nada.
- **Oferta B («Tres Periodos»)**: tampoco promete ser la más barata, pero **de hecho lo es**
  gracias al precio bajo en valle (0,085 €/kWh), que es donde más se consume en esta casa.

## Explicación sencilla

Esta casa consume más en valle (noche/madrugada) que en punta: 1.659 kWh frente a 998 kWh.
La oferta B cobra muy barato ese valle, así que gana aunque su precio en punta (0,210 €/kWh)
sea el más alto de los tres. La oferta C tiene el cartel más llamativo —y el kWh más barato—,
pero con una cuota de 5 € cada mes pagas 60 € al año antes de encender una sola bombilla.
Moraleja: lo que importa no es el precio del kWh del folleto, sino el total con tu consumo real.
