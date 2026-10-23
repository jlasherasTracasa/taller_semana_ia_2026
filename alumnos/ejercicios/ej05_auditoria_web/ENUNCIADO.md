# 🔵 EJ 05 · Auditoría de accesibilidad de una web

> 🌐 **Webs** · 🔵 Medio · ⏱ 20 min · 🛠️ opencode interactivo · Recomendado para: 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

La web de un centro de mayores tiene letra pequeña y poco contraste: sus usuarios no la pueden leer. Hay que auditarla y corregirla.

## 🎯 Objetivo

Detectar y corregir fallos de accesibilidad y adaptación al móvil de una página real.

## 📦 Lo que tienes en esta carpeta

- `web_centro_mayores.html`: la página original.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej05
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Audita web_centro_mayores.html: contraste de color, tamaño de letra, adaptación al móvil, atributo lang, textos alternativos de las imágenes y navegación con teclado. Entrega dos ficheros nuevos y no toques el original: (1) incidencias.md, con una lista de cada fallo y su corrección; (2) web_corregida.html, la página ya corregida. No me hagas preguntas: si algo es ambiguo, decide tú y explícalo en incidencias.md. Al final comprueba que existen los dos ficheros.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej05
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `incidencias.md` con cada fallo y su corrección.
- `web_corregida.html` con `lang="es"`, letra de 14 px o más, media queries y `alt` en todas las imágenes.
- El original sigue intacto.

```bash
python taller.py comprobar ej05      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej05_auditoria_web/`](../../soluciones/ej05_auditoria_web/)

## 🔀 Siguiente paso

- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
- **Área de correo y trámites** → [🟢 EJ 06 · Resumen diario de la bandeja de entrada](../ej06_resumen_diario/ENUNCIADO.md)
