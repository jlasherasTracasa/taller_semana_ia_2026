# 🟢 EJ 26 · ¿Qué oferta de luz me sale más barata?

> 📬 **Correo y trámites** · 🟢 Fácil · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 🧭 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Han llegado tres ofertas de luz y una dice ser «la más barata del mercado». Con el consumo real del último año se puede saber cuál lo es de verdad.

## 🎯 Objetivo

Comparar ofertas con **cálculos hechos con los datos**, no con lo que dice la publicidad, y explicarlo en lenguaje llano.

## 📦 Lo que tienes en esta carpeta

- `consumo_2025.csv`: kWh de cada mes en punta, llano y valle.
- `ofertas.md`: tres ofertas (energía, potencia y cuotas) de comercializadoras ficticias.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej26
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Con consumo_2025.csv y ofertas.md, calcula con un script de Python lo que habría pagado en 2025 con cada oferta (energía según periodos, potencia de 4,6 kW los 365 días y cuotas fijas; sin IVA ni impuesto eléctrico). Escribe comparativa.md con una tabla del coste anual de cada oferta, cuál es la más barata y cuánto se ahorra frente a las otras, y una explicación sencilla de por qué. Comprueba si es verdad lo que dice cada folleto.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej26
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Costes anuales: A **704,14 €**, B **646,89 €**, C **711,51 €** (con un margen de un euro).
- Recomienda la **B** y explica que la C, pese a tener el kWh más barato, es la más cara por la cuota mensual.

```bash
python taller.py comprobar ej26      # el agente no decide si está bien: lo decide el comprobador
```

## 💡 Pistas

- Los modelos suman mal de cabeza: por eso el encargo pide «un script de Python». Mira si lo ha usado.

## 🧪 Lo que pasó al validarlo (11-10-2026)

Calculó con un script los tres costes exactos (704,14 / 646,89 / 711,51 €), recomendó la B y explicó que la C, con el kWh más barato, es la más cara por la cuota de 5 € al mes: el folleto mentía.

Con el modelo gratuito de opencode (`big-pickle`): ✅ cumple el criterio.

Prompt, salida real y ficheros: [`soluciones/ej26_factura_luz/`](../../soluciones/ej26_factura_luz/)

## 🔀 Siguiente paso

- **Entender una carta del agua** → [🟢 EJ 25 · Entender una carta de la Administración](../ej25_carta_explicada/ENUNCIADO.md)
- **Hacerlo cada mes sin pedírselo** → [🔵 EJ 16 · Informe semanal que se recalcula solo](../ej16_informe_semanal/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
