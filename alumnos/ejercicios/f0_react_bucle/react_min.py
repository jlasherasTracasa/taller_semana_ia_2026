# Agente ReAct mínimo: el bucle «pensar → actuar → observar» en ~70 líneas, con LiteLLM + GLM-5.3-Flash.
# El modelo nunca toca el disco: PIDE una tool y este programa decide si la ejecuta y le devuelve lo observado.
# Uso:  set -a; . ./.env; set +a;  python react_min.py ["objetivo"]
import json
import os
import sys
from pathlib import Path

import litellm

# Con el LiteLLM del taller: "openai/<modelo>" + su URL. Con OpenRouter: "openrouter/z-ai/glm-5.3-flash".
if os.environ.get("LITELLM_API_KEY"):
    MODEL = os.environ.get("TALLER_MODELO", "openai/GLM-5.3-Flash")
    KW = {"api_base": os.environ["LITELLM_API_BASE"] + "/v1", "api_key": os.environ["LITELLM_API_KEY"]}
else:
    MODEL = os.environ.get("TALLER_MODELO", "openrouter/z-ai/glm-5.3-flash")
    KW = {"api_key": os.environ["OPENROUTER_API_KEY"]}
RAIZ = Path(__file__).resolve().parent  # el agente solo puede ver esta carpeta
MAX_PASOS = 8                            # freno de seguridad: un agente sin límite puede dar vueltas sin fin


def _dentro(ruta):
    p = (RAIZ / ruta).resolve()
    if not p.is_relative_to(RAIZ):
        raise PermissionError("fuera de la carpeta permitida")
    return p


def listar_carpeta(carpeta="."):
    return "\n".join(sorted(f.name for f in _dentro(carpeta).iterdir()))


def leer_archivo(ruta):
    return _dentro(ruta).read_text()[:2000]


TOOLS_PY = {"listar_carpeta": listar_carpeta, "leer_archivo": leer_archivo}
TOOLS = [
    {"type": "function", "function": {"name": "listar_carpeta", "description": "Lista los ficheros de una carpeta.",
     "parameters": {"type": "object", "properties": {"carpeta": {"type": "string"}}, "required": ["carpeta"]}}},
    {"type": "function", "function": {"name": "leer_archivo", "description": "Devuelve el contenido de un fichero de texto.",
     "parameters": {"type": "object", "properties": {"ruta": {"type": "string"}}, "required": ["ruta"]}}},
]

objetivo = sys.argv[1] if len(sys.argv) > 1 else \
    "¿Cuál de los ficheros de la carpeta notas/ tiene más líneas y de qué trata?"
mensajes = [
    {"role": "system", "content": "Eres un agente. Antes de cada acción explica en una frase qué vas a hacer y por qué. "
                                  "Usa las herramientas; no inventes el contenido de los ficheros."},
    {"role": "user", "content": objetivo},
]
print(f"OBJETIVO: {objetivo}\n")

for paso in range(1, MAX_PASOS + 1):
    msg = litellm.completion(model=MODEL, messages=mensajes, tools=TOOLS, **KW).choices[0].message
    if msg.content:
        print(f"[{paso}] PENSAR   {msg.content.strip()}")
    if not msg.tool_calls:                      # sin acciones pendientes: el agente da la tarea por terminada
        print("\nFIN: el modelo no pide más herramientas.")
        break
    mensajes.append({"role": "assistant", "content": msg.content, "tool_calls": [tc.model_dump() for tc in msg.tool_calls]})
    for tc in msg.tool_calls:
        args = json.loads(tc.function.arguments or "{}")
        print(f"[{paso}] ACTUAR   {tc.function.name}({args})")
        try:                                    # AQUÍ decide tu programa: ejecutar, negarse, pedir permiso…
            obs = TOOLS_PY[tc.function.name](**args)
        except Exception as e:                  # los errores también son observaciones útiles para el modelo
            obs = f"ERROR: {e}"
        print(f"[{paso}] OBSERVAR {obs[:120].replace(chr(10), ' | ')}")
        mensajes.append({"role": "tool", "tool_call_id": tc.id, "content": obs})
else:
    print(f"\nFIN: alcanzado el límite de {MAX_PASOS} pasos.")
