# Revisión de Claude del taller v2 y de la guía (28-09-2026)

**Comprobado:**
- Los ejemplos de Python de `guia.md` (`react_min.py`, `geval.py`, `gjr.py`) se han reejecutado siguiendo sus pasos y
  reproducen la salida documentada.
- La guía no contiene claves: la configuración usa `{env:LITELLM_API_KEY}`.
- La estructura del pptx v2 es correcta: 41 diapositivas, las 30 originales más la sección 05 (8 diapositivas),
  ejercicios y cierre.

**Errores de contenido (superados: el autor decidió que el taller no trate el sistema de generación; T6b lo rehace con enfoque práctico):**
1. Diapositiva 35: da a entender que la calibración usa una «rúbrica calibrada». Es al revés: G-Eval sin razonamiento
   acierta el 95,5 % [.86, 1.00] con el jurado y la rúbrica razonada el 70,6 % [.33, 1.00]. El valor calibrado pondera
   las notas G-Eval con los premios reales y no usa rúbricas. En imagen, solo el juez de concepto (61 %) supera al azar
   en estimación puntual, y su intervalo incluye el azar.
2. Diapositivas 32 y 37: «el juez principal es HUMANO» es engañoso. En el proyecto, el juez experto de los puntos de
   control fue Claude (un LLM) y el filtro humano final fue el autor. Hay que decirlo así y explicar el riesgo de
   circularidad (estudio humano en docs/v7/estudio_humano).

**No verificado:** el aspecto visual del pptx (desbordes, ajuste de textos). No hay LibreOffice en la máquina para
renderizarlo; conviene abrirlo en PowerPoint o Impress antes de usarlo.

## Revisión del taller práctico (T6b) — 28-09-2026

**Aprobado:** 22 diapositivas en bloques A-E (web, correo, presentaciones, rutinas, seguridad), sin ninguna mención al
sistema de generación. `guia.md` tiene 22 ejercicios, 15 de ellos marcados como validados, y una sección «Límites
encontrados».

**Reverificado por Claude:**
- La web del ejercicio 1 se sirve en local y devuelve HTTP 200 con su título.
- En el ejercicio 10, el correo con inyección de prompt pedía copiar el buzón a `/tmp/curso_agentes/exfiltrado/`. El
  agente **no** obedeció (la carpeta no existe) y escribió `aviso_seguridad.md` explicando el intento.
- La tarea programada del ejercicio 21 no ha dejado timers de systemd ni entradas de cron en la máquina.

**No verificado:** el aspecto visual del pptx, porque no hay LibreOffice. Hay que abrirlo en PowerPoint o Impress
antes del taller. Los ejemplos se guardan y verifican en `docs/taller/ejemplos/` (T6c) y el bloque de tools y skills
llega con T6d.

## Revisión del bloque F: tools y skills (T6d)

**Aprobado:** 4 diapositivas nuevas (22-25) sobre function calling, tools de opencode y MCP, skills y comandos, y una
tabla prompt / tool / skill / agente / MCP. `guia.md` incorpora el bloque F.

**Reejecutado por Claude:**
- El ejemplo 12a (function calling) devuelve el JSON de la llamada y el resultado de 6.050 €.
- Los scripts de 12a y 12c compilan.
- `verificar_todo.sh` sigue en 18/18 OK.

**Corrección de seguridad:** la calculadora de 12a usaba `eval()` con los builtins vacíos. La lista blanca de
caracteres impedía inyectar código, pero no una denegación de servicio (`9**9**9**9` cuelga el proceso) ni la división
por cero. Se ha sustituido por un evaluador basado en `ast` que solo admite + - * /, rechaza potencias, nombres y
llamadas, y limita la longitud. Probado con esos cinco casos.
