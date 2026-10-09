# 🟢 EJ 01 · La web de Pilar

> 🌐 **Puerta A · El escaparate** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭

## 📖 La escena

Pilar te da un papel con su biografía: «Quiero una página como las de la tele, pero sencilla».

## 🎯 Objetivo

Convertir un texto en bruto en una página web terminada, en un solo archivo.

## 📦 Lo que tienes en esta carpeta

- `bio_pilar.txt`: la biografía de Pilar.

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
python3 taller.py comprobar ej01      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **¿La publicamos en internet?** → [🔵 EJ 04 · Publicar la web (sin darle tus llaves)](../ej04_github_pages/ENUNCIADO.md)
- **¿Es accesible para gente mayor?** → [🔵 EJ 05 · Una web para el centro de mayores](../ej05_auditoria_web/ENUNCIADO.md)
- **Quiero una web que reciba datos** → [🟣 EJ 03 · El formulario que guarda en JSON (y el proceso ajeno)](../ej03_formulario_json/ENUNCIADO.md)
