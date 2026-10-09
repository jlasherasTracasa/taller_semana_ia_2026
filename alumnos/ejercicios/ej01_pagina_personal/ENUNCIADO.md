# 🟢 EJ 01 · Una web personal en un solo archivo

> 🌐 **Webs** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭

## 📌 La situación

Una panadera jubilada que da talleres de pan quiere una web sencilla para que la encuentren. Tiene su biografía en un texto.

## 🎯 Objetivo

Convertir un texto en bruto en una página web terminada, en un solo archivo.

## 📦 Lo que tienes en esta carpeta

- `bio_pilar.txt`: su biografía, tal cual la escribió.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej01
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Lee bio_pilar.txt y crea una página personal en un único archivo index.html: HTML y CSS dentro del mismo archivo, adaptada al móvil, en castellano (lang=es), sin dependencias externas ni frameworks, con enlaces mailto y tel para contactar. Corrige las erratas del texto original." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `index.html` único, sin CSS ni JS externos, con `lang="es"` y meta viewport.
- Enlaces `mailto:` y `tel:` que funcionan.
- Ábrela en el navegador y estrecha la ventana: nada se corta. (Hay una errata en la bio: ¿la corrigió?)

```bash
python3 taller.py comprobar ej01      # el agente no decide si está bien: lo decide el comprobador
```

## 🧪 Lo que pasó al validarlo (09-10-2026)

Una sola página con `lang="es"`, viewport, media queries, `mailto:` y `tel:`, y corrigió la errata «elsenderismo».

Prompt, salida real y ficheros: [`soluciones/ej01_pagina_personal/`](../../soluciones/ej01_pagina_personal/)

## 🔀 Siguiente paso

- **¿La publicamos en internet?** → [🔵 EJ 04 · Publicar una web en GitHub Pages (sin darle tus credenciales)](../ej04_github_pages/ENUNCIADO.md)
- **¿Es accesible para gente mayor?** → [🔵 EJ 05 · Auditoría de accesibilidad de una web](../ej05_auditoria_web/ENUNCIADO.md)
- **Quiero una web que reciba datos** → [🟣 EJ 03 · Formulario web que guarda los envíos (sin matar procesos ajenos)](../ej03_formulario_json/ENUNCIADO.md)
