# Estructura original de `docs/taller/taller-agentes-ia-v1.pptx` (antes `docs/taller-agentes-ia.pptx`)

Análisis realizado con python-pptx (T6, taller de agentes). 32 diapositivas, formato 16:9
(13,33 × 7,5 in), layout único «DEFAULT». Estilo: fondos blancos en diapositivas de contenido y
oscuro (`#15161A`) en portada, separadores de bloque y cierre; títulos Arial bold, cuerpo Calibri,
bloques de código en Courier New sobre tarjeta oscura (verde `#00B865` para comandos, naranja
`#E8940F` para destacados, gris `#9AA0AC` para comentarios); pie «Semana de la IA · UPNA · 23 oct 2026»
con número de página; todas las diapositivas llevan notas del ponente.

## Bloques

| # | Diapositivas | Contenido |
|---|---|---|
| Portada | 1 | «Agentes de IA: deja de chatear y ponla a trabajar». Terminal simulada de opencode. |
| Intro | 2–3 | Qué te llevas (criterio, agente funcionando, algo hecho); plan horario (2–4 h, núcleo en verde). |
| **01 · Qué es un agente** | 4–13 | Definición clásica (sensores/actuadores, 1995); hitos 1956–2026; por qué ahora (instrucciones, razonamiento, herramientas); chatbot vs agente; bucle ReAct (objetivo→plan→acción→observación); el modelo nunca ejecuta (pide herramientas en texto, el programa ejecuta y pide permiso); ventana de contexto finita; las 4 piezas (modelo, herramientas, contexto, permisos); familias de tareas (documentos, datos, código, rutina). |
| **02 · Montamos el terreno** | 14–19 | Mapa de herramientas (OpenCode elegida, abierta y por terminal); instalación en 4 pasos (`npm i -g opencode-ai`, `opencode auth login`, modelo, carpeta vacía) con plan B web; costes orientativos de GLM 5.3 Flash (~0,02 €/tarea, ~0,30 €/persona); librerías para documentos (`python-docx`, `python-pptx`, `openpyxl`, `pdfplumber`); carpeta preparada (`opencode.json`, `AGENTS.md`, `entrada/`, `salida/`, comandos). |
| **03 · Manos a la obra** | 20–25 | Práctica 1 «agente de oficina» (informe comparativo desde material desordenado; explorar→encargar→revisar→corregir); cómo pedir bien (CONTEXTO-OBJETIVO-ENTREGA-LÍMITES-CRITERIO); comandos con barra (`.opencode/commands/informe.md`, `$ARGUMENTS`, `@archivo`, `!comando`); práctica 2 «de la idea al prototipo» (describir, que lo pruebe, iteración corta, publicar). |
| **04 · Que funcione de verdad** | 26–30 | `AGENTS.md` (quién eres, cómo quieres las cosas, qué no tocar); subagentes y conectores MCP; dónde se rompe (alucina con aplomo, bucles, no sabe lo que no le has dicho, «funciona ≠ bien»); cinco reglas de seguridad (carpeta aislada, versiones, claves en variables de entorno, datos personales, leer antes de aceptar). |
| Cierre | 31–32 | «Qué hacer el lunes» (elige tarea, escríbela como encargo, déjasela y revisa) y gracias. |

## Errores detectados (corregidos en la v2)

1. **Ruta de comandos errónea** (diapositivas 19 y 24): opencode usa `.opencode/command/`
   (en singular), no `.opencode/commands/`.
2. **Ventana de contexto inflada** (diapositiva 16): se afirma «1,3 millones de contexto» para
   `glm-5.3-flash`; el valor coherente con el montaje real del repositorio (`opencode.json`) es
   262 144 tokens (256 K). Además la diapositiva 11 dice «un millón y pico», inconsistente con ambas.
3. **Proveedor**: la presentación instala vía OpenRouter, pero el montaje real y validado del
   repositorio usa un LiteLLM propio con la clave en variable de entorno (`{env:LITELLM_API_KEY}`);
   en la v2 se menciona como alternativa real y se remite a `docs/taller/guia.md`.
4. **Notas sin acentuar** en varias diapositivas (cosmético; no afectan a la proyección).

## Hueco detectado (motiva la ampliación)

La versión original explica *qué es* un agente y *cómo usarlo*, pero no recoge lo aprendido al
construir un sistema real multiagente en este repositorio: ReAct con estado persistente, búsqueda
LATS, calidad-diversidad (QDAIF/MAP-Elites), jueces calibrados con datos reales, G-Eval con
logprobs, verificadores objetivos, explorar ideas antes que refinar, humano en el bucle y opencode
como agente de código de uso diario. Tampoco incluye ejercicios «avanzados». La v2 añade un bloque
05 con esos contenidos y tres ejercicios prácticos ligados a la guía validada.
