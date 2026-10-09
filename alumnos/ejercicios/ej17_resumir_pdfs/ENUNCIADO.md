# 🔵 EJ 17 · Tres PDF en una tabla

> 🗂️ **Puerta D · El ayuntamiento** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

El centro de mayores tiene tres guías en PDF. Nadie se las ha leído. Una tabla con lo esencial, por favor.

## 🎯 Objetivo

Resumir varios PDF en una tabla, con puntos sacados del texto real.

## 📦 Lo que tienes en esta carpeta

- `apuntes/`: tres PDF (gimnasia, excursiones, taller de memoria).

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej17
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee los PDF de apuntes/ uno a uno con pdfplumber y crea resumen_apuntes.md: una tabla Markdown con el título, el tema y tres puntos clave de cada documento, sacados del texto (no inventes nada)." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- La tabla cubre los tres PDF.
- Los puntos se pueden encontrar en los originales (compruébalo con uno).

```bash
python3 taller.py comprobar ej17      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Facturas a Excel** → [🔵 EJ 18 · Facturas en PDF a Excel](../ej18_facturas_excel/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
