# 🔵 EJ 13 · Revisar la presentación de otro

> 📊 **Puerta C · La bodega** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

El deck de ferias tiene faltas, mayúsculas locas y espacios dobles. Hay que corregirlo sin cambiar el contenido.

## 🎯 Objetivo

Corregir ortografía y consistencia de un pptx sin tocar el original.

## 📦 Lo que tienes en esta carpeta

- `deck_ferias.pptx`.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej13
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Revisa deck_ferias.pptx y entrégame primero informe_incidencias.md con cada error (ortografía, mayúsculas, espacios, tildes) y después una copia corregida como deck_ferias_corregido.pptx. No toques el original. Comprueba al final que el original no ha cambiado." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `informe_incidencias.md` y `deck_ferias_corregido.pptx` (mismo número de diapositivas).
- El original, intacto.

```bash
python3 taller.py comprobar ej13      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Traducirlo** → [🟣 EJ 14 · Traducir un pptx por dentro](../ej14_traducir_deck/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
