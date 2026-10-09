# Solución · EJ 04 · Publicar en GitHub Pages

## Prompt exacto usado
Ver `prompt.txt` (el del ENUNCIADO).

## Resultado (parte del agente: validada el 2026-09-28, 8 s)
- `README.md` breve para el repositorio (en esta carpeta).
- Pasos numerados en la respuesta (`salida.txt`): crear repo público → subir `index.html` (web o `git push`) →
  Settings → Pages → *Deploy from a branch*, `main`, `/ (root)` → esperar 1–2 min → URL
  `https://<tu-usuario>.github.io/<repo>/`. Incluye qué hacer si sale 404.
- El agente **no** hizo push ni pidió credenciales, como exige el enunciado.

## Parte que haces tú (no validable por el docente)
El `git push` y la comprobación de la URL pública necesitan **tu** cuenta de GitHub. En el `opencode.json` del
kit, `git push *` está en `ask`: si el agente lo intenta, te pedirá permiso y deberías decir que no.
Usa un *token de acceso personal* de permisos mínimos y revócalo al terminar el taller.

## Lección
En el primer intento el prompt no decía el idioma y el agente respondió en inglés. Añadir «Todo en castellano»
lo arregló: **lo que no pides explícitamente, lo decide el modelo**.
