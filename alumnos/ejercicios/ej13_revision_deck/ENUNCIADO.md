# 🔵 EJ 13 · Revisar y corregir una presentación ajena

> 📊 **Informes y presentaciones** · 🔵 Medio · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Una presentación para una feria tiene faltas, mayúsculas inconsistentes y espacios dobles. Hay que corregirla sin cambiar el contenido.

## 🎯 Objetivo

Corregir ortografía y consistencia de un pptx sin tocar el original.

## 📦 Lo que tienes en esta carpeta

- `deck_ferias.pptx`.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej13
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Revisa deck_ferias.pptx y entrégame primero informe_incidencias.md con cada error (ortografía, mayúsculas, espacios, tildes) y después una copia corregida como deck_ferias_corregido.pptx. No toques el original. Comprueba al final que el original no ha cambiado.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej13
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `informe_incidencias.md` y `deck_ferias_corregido.pptx` (mismo número de diapositivas).
- El original, intacto.

```bash
python taller.py comprobar ej13      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Informe y copia corregida, original intacto. Repetido con un HOME limpio porque en la primera pasada el agente usó una skill `pptx` global de la máquina del docente: sin ella, también pasa.

Prompt, salida real y ficheros: [`soluciones/ej13_revision_deck/`](../../soluciones/ej13_revision_deck/)

## 🔀 Siguiente paso

- **Traducirlo** → [🟣 EJ 14 · Traducir una presentación sin romperla](../ej14_traducir_deck/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
