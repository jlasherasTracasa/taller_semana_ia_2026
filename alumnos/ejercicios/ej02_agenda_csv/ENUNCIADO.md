# 🔵 EJ 02 · El programa de fiestas

> 🌐 **Puerta A · El escaparate** · 🔵 Medio · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 📚

## 📖 La escena

La comisión de fiestas tiene el programa en una hoja de cálculo. Lo quieren en el móvil de todo el pueblo.

## 🎯 Objetivo

Convertir una tabla (CSV) en una página de agenda agrupada por franjas.

## 📦 Lo que tienes en esta carpeta

- `programa.csv`: hora, título, lugar y tipo de cada acto.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej02
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee programa.csv y crea agenda.html: una sola columna, agrupada en Mañana y Tarde, diseño festivo, adaptada al móvil y sin dependencias externas. Incluye TODOS los actos del CSV y comprueba al final, contándolos, que no falta ninguno." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `agenda.html` con todos los actos del CSV, agrupados en mañana y tarde.
- Sin dependencias externas.

```bash
python3 taller.py comprobar ej02      # el agente no puede darte el sello: solo el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Los 6 actos, agrupados en mañana y tarde, y los contó al final.

Prompt, salida real y ficheros: [`soluciones/ej02_agenda_csv/`](../../soluciones/ej02_agenda_csv/)

## 🔀 ¿Y ahora qué?

- **Ahora, que la gente pueda apuntarse** → [🟣 EJ 03 · El formulario que guarda en JSON (y el proceso ajeno)](../ej03_formulario_json/ENUNCIADO.md)
- **Publicarla** → [🔵 EJ 04 · Publicar la web (sin darle tus llaves)](../ej04_github_pages/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
