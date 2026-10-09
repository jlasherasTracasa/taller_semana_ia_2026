# F.1 · Tools: function calling — el modelo no ejecuta nada

## Objetivo
Ver con tus propios ojos que el modelo NO ejecuta herramientas: pide usarlas con un JSON y tu código decide.

## Datos de partida
- `fc_calculadora.py` — script autónomo con LiteLLM: declara el esquema de una tool «calculadora», imprime el tool_call JSON del modelo, ejecuta la función real (sin eval) y devuelve el resultado al modelo.

## Prompt sugerido
```bash
(NO es un encargo al agente: script autónomo de function calling con LiteLLM + GLM)

$ set -a; . ./.env; set +a
$ python fc_calculadora.py      # o .venv/bin/python si usas el entorno del kit

El modelo recibe el esquema de la tool «calculadora» y responde con un tool_call
JSON; NUESTRO programa ejecuta la función y devuelve el resultado al modelo.
```

## Criterio de éxito
El script imprime: (1) el tool_call con la expresión `(1250+3750)*1.21`, (2) el resultado local 6050.0, (3) la respuesta final «6.050 €». Experimenta: cambia la expresión del mensaje y observa cómo cambia el JSON pedido.

## Tiempo estimado
≈ 15 min

## Dificultad
Media
