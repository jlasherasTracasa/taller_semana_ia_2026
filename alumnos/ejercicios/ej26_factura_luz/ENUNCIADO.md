# 🟢 EJ 26 · ¿Qué oferta de luz me sale más barata?

> 📬 **Correo y trámites** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📌 La situación

Han llegado tres ofertas de luz y una dice ser «la más barata del mercado». Con el consumo real del último año se puede saber cuál lo es de verdad.

## 🎯 Objetivo

Comparar ofertas con **cálculos hechos con los datos**, no con lo que dice la publicidad, y explicarlo en lenguaje llano.

## 📦 Lo que tienes en esta carpeta

- `consumo_2025.csv`: kWh de cada mes en punta, llano y valle.
- `ofertas.md`: tres ofertas (energía, potencia y cuotas) de comercializadoras ficticias.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej26
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Con consumo_2025.csv y ofertas.md, calcula con un script de Python lo que habría pagado en 2025 con cada oferta (energía según periodos, potencia de 4,6 kW los 365 días y cuotas fijas; sin IVA ni impuesto eléctrico). Escribe comparativa.md con una tabla del coste anual de cada oferta, cuál es la más barata y cuánto se ahorra frente a las otras, y una explicación sencilla de por qué. Comprueba si es verdad lo que dice cada folleto." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Costes anuales: A **704,14 €**, B **646,89 €**, C **711,51 €** (con un margen de un euro).
- Recomienda la **B** y explica que la C, pese a tener el kWh más barato, es la más cara por la cuota mensual.

```bash
python3 taller.py comprobar ej26      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- Los modelos suman mal de cabeza: por eso el encargo pide «un script de Python». Mira si lo ha usado.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Calculó con un script los tres costes exactos (704,14 / 646,89 / 711,51 €), recomendó la B y explicó que la C, con el kWh más barato, es la más cara por la cuota de 5 € al mes: el folleto mentía.

Prompt, salida real y ficheros: [`soluciones/ej26_factura_luz/`](../../soluciones/ej26_factura_luz/)

## 🔀 Siguiente paso

- **Entender una carta del agua** → [🟢 EJ 25 · Entender una carta de la Administración](../ej25_carta_explicada/ENUNCIADO.md)
- **Hacerlo cada mes sin pedírselo** → [🔵 EJ 16 · Informe semanal que se recalcula solo](../ej16_informe_semanal/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
