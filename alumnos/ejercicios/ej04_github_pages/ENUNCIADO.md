# 🔵 EJ 04 · Publicar la web (sin darle tus llaves)

> 🌐 **Puerta A · El escaparate** · 🔵 Medio · ⏱ 20 min · 🛠️ `opencode run` · Recomendado para: 📚 💻

## 📖 La escena

Pilar quiere un enlace para WhatsApp. Lo publicas gratis en GitHub Pages… pero el último paso lo das tú.

## 🎯 Objetivo

Preparar el repositorio y una guía de publicación; el `git push` y la URL los haces tú.

## 📦 Lo que tienes en esta carpeta

- `index.html`: la página que vas a publicar.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej04
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Voy a publicar index.html en GitHub Pages. Inicializa aquí un repositorio git con un primer commit, escribe un README.md breve y PASOS.md con los pasos numerados para crear el repositorio en GitHub, activar Pages y subir los cambios. Todo en castellano. NO hagas git push ni pidas credenciales: ese paso lo haré yo." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Hay repositorio git local con un commit, `README.md` y `PASOS.md` en castellano.
- El agente no ha hecho `push` ni ha pedido tokens. La URL pública la compruebas tú.

```bash
python3 taller.py comprobar ej04      # el agente no puede darte el sello: solo el comprobador
```

## 💡 Pistas

- Usa un token de GitHub con permisos mínimos y caducidad corta. Nunca lo pegues en un chat.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Repositorio con commit, `README.md` y `PASOS.md` en castellano, sin `push` ni credenciales. En septiembre, sin «todo en castellano», respondió en inglés.

Prompt, salida real y ficheros: [`soluciones/ej04_github_pages/`](../../soluciones/ej04_github_pages/)

## 🔀 ¿Y ahora qué?

- **¿Es accesible?** → [🔵 EJ 05 · Una web para el centro de mayores](../ej05_auditoria_web/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
