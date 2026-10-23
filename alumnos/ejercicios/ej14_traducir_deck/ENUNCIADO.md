# 🟣 EJ 14 · Traducir una presentación sin romperla

> 📊 **Informes y presentaciones** · 🟣 Avanzado · ⏱ 20 min · 🛠️ opencode interactivo · Recomendado para: 💻

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

La misma charla se va a dar en una feria en Burdeos. Hay que traducirla al inglés sin romper tablas ni gráficos.

## 🎯 Objetivo

Traducir un pptx editando su XML (un pptx es un zip), sin reconstruirlo.

## 📦 Lo que tienes en esta carpeta

- `charla_taller_es.pptx`.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej14
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Traduce charla_taller_es.pptx al inglés editando el XML directamente (descomprime, edita el texto de ppt/slides/slideN.xml y vuelve a comprimir). Usa defusedxml o expresiones regulares sobre las etiquetas a:t, no xml.etree sin protección. Entrega charla_taller_en.pptx. No alteres imágenes, tablas ni gráficos.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej14
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `charla_taller_en.pptx` abre sin aviso de reparación, con el mismo número de diapositivas, tablas y gráficos.
- El texto está en inglés.

```bash
python taller.py comprobar ej14      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej14_traducir_deck/`](../../soluciones/ej14_traducir_deck/)

## 🔀 Siguiente paso

- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
