# 🔵 EJ 17 · Resumir varios PDF en una tabla

> 🗂️ **Documentos y tareas repetitivas** · 🔵 Medio · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Un centro de mayores tiene tres guías en PDF que nadie se ha leído. Se necesita una tabla con lo esencial de cada una.

## 🎯 Objetivo

Resumir varios PDF en una tabla, con puntos sacados del texto real.

## 📦 Lo que tienes en esta carpeta

- `apuntes/`: tres PDF (gimnasia, excursiones, taller de memoria).

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej17
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee los PDF de apuntes/ uno a uno con pdfplumber y crea resumen_apuntes.md: una tabla Markdown con el título, el tema y tres puntos clave de cada documento, sacados del texto (no inventes nada).
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej17
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- La tabla cubre los tres PDF.
- Los puntos se pueden encontrar en los originales (compruébalo con uno).

```bash
python taller.py comprobar ej17      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Tabla con los tres PDF y puntos sacados del texto.

Prompt, salida real y ficheros: [`soluciones/ej17_resumir_pdfs/`](../../soluciones/ej17_resumir_pdfs/)

## 🔀 Siguiente paso

- **Facturas a Excel** → [🔵 EJ 18 · Facturas en PDF a Excel](../ej18_facturas_excel/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
