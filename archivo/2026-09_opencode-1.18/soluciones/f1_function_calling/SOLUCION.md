# Solución · F.1 · Tools: function calling

## Prompt exacto usado
```bash
(NO es un encargo al agente: script autónomo de function calling con LiteLLM + GLM)

$ set -a; . ./.env; set +a
$ python fc_calculadora.py      # o .venv/bin/python si usas el entorno del kit

El modelo recibe el esquema de la tool «calculadora» y responde con un tool_call
JSON; NUESTRO programa ejecuta la función y devuelve el resultado al modelo.
```

## Resultado
El modelo devolvió el tool_call {name: calculadora, expresion: (1250+3750)*1.21}; nuestro programa calculó 6050.0 y el modelo redactó «El total con IVA del 21 % aplicado es 6.050 €».

## Salida real (extracto validado 2026-09-28)
```
== RESPUESTA 1 DEL MODELO ==
content: ''
tool_calls (JSON crudo devuelto por el modelo):
[
  "{\n  \"index\": 0,\n  \"function\": {\n    \"arguments\": \"{\\\"expresion\\\": \\\"(1250+3750)*1.21\\\"}\",\n    \"name\": \"calculadora\"\n  },\n  \"id\": \"call_23abb25e20e3408ca19085eb\",\n  \"type\": \"function\"\n}"
]

== EJECUCIÓN LOCAL (nuestro código) ==
calculadora({'expresion': '(1250+3750)*1.21'}) = 6050.0

== RESPUESTA 2 DEL MODELO ==
El total con IVA del 21 % aplicado es **6.050 €**.

[exit 0]
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
