# 🟣 EJ 14 · Traducir un pptx por dentro

> 📊 **Puerta C · La bodega** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 💻

## 📖 La escena

La charla va a una feria en Burdeos. Hay que traducirla sin romper tablas ni gráficos.

## 🎯 Objetivo

Traducir un pptx editando su XML (un pptx es un zip), sin reconstruirlo.

## 📦 Lo que tienes en esta carpeta

- `charla_taller_es.pptx`.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej14
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Traduce charla_taller_es.pptx al inglés editando el XML directamente (descomprime, edita el texto de ppt/slides/slideN.xml y vuelve a comprimir). Usa defusedxml o expresiones regulares sobre las etiquetas a:t, no xml.etree sin protección. Entrega charla_taller_en.pptx. No alteres imágenes, tablas ni gráficos." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `charla_taller_en.pptx` abre sin aviso de reparación, con el mismo número de diapositivas, tablas y gráficos.
- El texto está en inglés.

```bash
python3 taller.py comprobar ej14      # el agente no puede darte el sello: solo el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Mismas diapositivas, tablas, gráficos e imágenes; texto en inglés.

Prompt, salida real y ficheros: [`soluciones/ej14_traducir_deck/`](../../soluciones/ej14_traducir_deck/)

## 🔀 ¿Y ahora qué?

- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
