# 🟢 EJ 19 · Certificados personalizados en lote

> 🗂️ **Documentos y tareas repetitivas** · 🟢 Fácil · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 🧭 📚

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Termina un curso y cada participante necesita su certificado de asistencia con su nombre, curso y horas.

## 🎯 Objetivo

Generar en lote un documento personalizado por persona a partir de una lista.

## 📦 Lo que tienes en esta carpeta

- `nombres.csv`: nombre, curso y horas.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej19
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee nombres.csv y genera en la carpeta certificados/ un PDF por persona llamado certificado_NOMBRE.pdf, con una plantilla sobria hecha con reportlab: nombre, curso y horas. Verifica al final que hay un PDF por fila del CSV y que cada uno lleva su nombre.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej19
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Un PDF por fila del CSV, cada uno con su nombre, ninguno repetido.

```bash
python taller.py comprobar ej19      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej19_certificados_pdf/`](../../soluciones/ej19_certificados_pdf/)

## 🔀 Siguiente paso

- **Exámenes por corregir** → [🔵 EJ 23 · Corregir respuestas con una rúbrica](../ej23_corregir_rubrica/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
