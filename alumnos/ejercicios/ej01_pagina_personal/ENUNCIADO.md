# 🟢 EJ 01 · Una web personal en un solo archivo

> 🌐 **Webs** · 🟢 Fácil · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 🧭

> 🎥 **Demo en directo**: lo hace el profesor en el proyector; tú lo miras y lo repites después si quieres.

## 📌 La situación

Una panadera jubilada que da talleres de pan quiere una web sencilla para que la encuentren. Tiene su biografía en un texto.

## 🎯 Objetivo

Convertir un texto en bruto en una página web terminada, en un solo archivo.

## 📦 Lo que tienes en esta carpeta

- `bio_pilar.txt`: su biografía, tal cual la escribió.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej01
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Lee bio_pilar.txt y crea una página personal en un único archivo index.html: HTML y CSS dentro del mismo archivo, adaptada al móvil, en castellano (lang=es), sin dependencias externas ni frameworks, con enlaces mailto y tel para contactar. Corrige las erratas del texto original.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej01
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `index.html` único, sin CSS ni JS externos, con `lang="es"` y meta viewport.
- Enlaces `mailto:` y `tel:` que funcionan.
- Ábrela en el navegador y estrecha la ventana: nada se corta. (Hay una errata en la bio: ¿la corrigió?)

```bash
python taller.py comprobar ej01      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej01_pagina_personal/`](../../soluciones/ej01_pagina_personal/)

## 🔀 Siguiente paso

- **¿La publicamos en internet?** → [🔵 EJ 04 · Publicar una web en GitHub Pages (sin darle tus credenciales)](../ej04_github_pages/ENUNCIADO.md)
- **¿Es accesible para gente mayor?** → [🔵 EJ 05 · Auditoría de accesibilidad de una web](../ej05_auditoria_web/ENUNCIADO.md)
- **Quiero una web que reciba datos** → [🟣 EJ 03 · Formulario web que guarda los envíos (sin matar procesos ajenos)](../ej03_formulario_json/ENUNCIADO.md)
