# 🟢 EJ 19 · Certificados personalizados en lote

> 🗂️ **Documentos y tareas repetitivas** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚

## 📌 La situación

Termina un curso y cada participante necesita su certificado de asistencia con su nombre, curso y horas.

## 🎯 Objetivo

Generar en lote un documento personalizado por persona a partir de una lista.

## 📦 Lo que tienes en esta carpeta

- `nombres.csv`: nombre, curso y horas.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej19
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee nombres.csv y genera en la carpeta certificados/ un PDF por persona llamado certificado_NOMBRE.pdf, con una plantilla sobria hecha con reportlab: nombre, curso y horas. Verifica al final que hay un PDF por fila del CSV y que cada uno lleva su nombre." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Un PDF por fila del CSV, cada uno con su nombre, ninguno repetido.

```bash
python3 taller.py comprobar ej19      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Un PDF por persona, cada uno con su nombre.

Prompt, salida real y ficheros: [`soluciones/ej19_certificados_pdf/`](../../soluciones/ej19_certificados_pdf/)

## 🔀 Siguiente paso

- **Exámenes por corregir** → [🔵 EJ 23 · Corregir respuestas con una rúbrica](../ej23_corregir_rubrica/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
