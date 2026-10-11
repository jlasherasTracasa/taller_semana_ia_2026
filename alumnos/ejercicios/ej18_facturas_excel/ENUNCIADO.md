# 🔵 EJ 18 · Facturas en PDF a Excel

> 🗂️ **Documentos y tareas repetitivas** · 🔵 Medio · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

La gestoría pide las facturas del mes en una hoja de cálculo. Están en PDF.

## 🎯 Objetivo

Extraer datos económicos de facturas PDF y volcarlos en una hoja de cálculo que cuadre.

## 📦 Lo que tienes en esta carpeta

- `facturas/`: dos facturas en PDF.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej18
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Extrae de los PDF de facturas/ el emisor, la fecha, la base imponible, el IVA y el total, y genera facturas.xlsx con openpyxl. Añade una fila final con la suma de totales escrita como número (no como fórmula) y comprueba que cuadra con la suma de los totales de los PDF.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej18
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `facturas.xlsx` legible con los dos totales (454,48 y 1.212,90).
- Fila final 1.667,38.

```bash
python taller.py comprobar ej18      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Totales 454,48 y 1.212,90 y suma 1.667,38. En la ronda 1 puso la suma como fórmula `=SUM()`, que no se ve sin abrir el Excel: ahora el encargo pide el número.

Prompt, salida real y ficheros: [`soluciones/ej18_facturas_excel/`](../../soluciones/ej18_facturas_excel/)

## 🔀 Siguiente paso

- **Certificados en lote** → [🟢 EJ 19 · Certificados personalizados en lote](../ej19_certificados_pdf/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
