# Function calling mínimo con LiteLLM (GLM-5.3-Flash con OpenRouter; o Groq/Gemini gratis).
# El modelo NO ejecuta nada: pide una herramienta con argumentos JSON
# y es nuestro programa quien decide si la ejecuta.
import json
import os, sys
import time
import litellm

# Con el LiteLLM del taller: "openai/<modelo>" + su URL. Con OpenRouter: "openrouter/z-ai/glm-5.3-flash".
# Sin OpenRouter: una clave GRATUITA y personal de Groq ("groq/…", recomendada) o de Google AI Studio ("gemini/…").
# Los modelos gratuitos de opencode solo funcionan DENTRO de opencode: este programa necesita una de esas claves
OTRO = os.environ.get("TALLER_MODELO", "")
OTRO = "" if OTRO.startswith("opencode/") else OTRO
OTRO = os.environ.get("TALLER_MODELO_PY") or OTRO   # solo para estos programas, no para opencode
if os.environ.get("LITELLM_API_KEY"):
    MODEL = OTRO or "openai/GLM-5.3-Flash"
    KW = {"api_base": os.environ["LITELLM_API_BASE"] + "/v1", "api_key": os.environ["LITELLM_API_KEY"]}
elif os.environ.get("OPENROUTER_API_KEY"):
    MODEL = OTRO or "openrouter/z-ai/glm-5.3-flash"
    KW = {"api_key": os.environ["OPENROUTER_API_KEY"]}
elif os.environ.get("GROQ_API_KEY"):             # gratuita y recomendada (wiki: Modelos); los gratuitos cambian: comprueba el nombre
    MODEL = OTRO or "groq/openai/gpt-oss-120b"
    KW = {"api_key": os.environ["GROQ_API_KEY"]}
elif os.environ.get("GEMINI_API_KEY"):
    MODEL = OTRO or "gemini/gemini-flash-latest"
    KW = {"api_key": os.environ["GEMINI_API_KEY"]}
elif sys.argv[1:2] == ["--sin-modelo"]:
    MODEL, KW = None, {}
else:
    sys.exit("Este programa llama al modelo directamente y necesita una clave en el .env del kit:\n"
             "OPENROUTER_API_KEY, o una gratuita de Groq (GROQ_API_KEY) o de Google AI Studio (GEMINI_API_KEY).\n"
             "Los modelos gratuitos de opencode solo funcionan dentro de opencode (wiki: Modelos).")

def preguntar(**datos):
    """Llama al modelo. Si una clave gratuita llega a su límite por minuto, espera y lo reintenta."""
    for espera in (10, 20, 30, 40, 0):
        try:
            return litellm.completion(model=MODEL, **datos, **KW).choices[0].message
        except litellm.RateLimitError:
            if not espera:
                sys.exit("El proveedor sigue diciendo que has llegado a tu límite: espera un minuto y repite.")
            print(f"   (límite de uso por minuto del proveedor: espero {espera} s y lo intento otra vez)")
            time.sleep(espera)


# 1) El ESQUEMA de la tool: nombre, descripción y JSON Schema de los parámetros.
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculadora",
            "description": "Evalúa una expresión aritmética simple (+ - * / y paréntesis). Úsala siempre que necesites calcular algo.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expresion": {"type": "string", "description": "Expresión aritmética, p. ej. '(1250+3750)*0.21'"}
                },
                "required": ["expresion"],
            },
        },
    }
]

import ast
import operator

_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul, ast.Div: operator.truediv,
        ast.USub: operator.neg, ast.UAdd: operator.pos}


def _calc(nodo):
    """Recorre el árbol sintáctico y admite SOLO números y + - * /. Nada de eval()."""
    if isinstance(nodo, ast.Expression):
        return _calc(nodo.body)
    if isinstance(nodo, ast.Constant) and isinstance(nodo.value, (int, float)):
        return nodo.value
    if isinstance(nodo, ast.BinOp) and type(nodo.op) in _OPS:
        return _OPS[type(nodo.op)](_calc(nodo.left), _calc(nodo.right))
    if isinstance(nodo, ast.UnaryOp) and type(nodo.op) in _OPS:
        return _OPS[type(nodo.op)](_calc(nodo.operand))
    raise ValueError("operación no permitida")


def calculadora(expresion: str) -> str:
    """Implementación REAL en Python. Lección de seguridad: los argumentos los escribe el modelo (y quizá un atacante
    vía inyección de prompt), así que nunca se ejecutan con eval(). Se admite solo aritmética básica: sin potencias
    (9**9**9 colgaría el programa), sin nombres ni llamadas."""
    if len(expresion) > 200:
        return "ERROR: expresión demasiado larga"
    try:
        return str(_calc(ast.parse(expresion, mode="eval")))
    except (ValueError, SyntaxError, ZeroDivisionError) as e:
        return f"ERROR: {e}"

# Probar la calculadora a mano, sin el modelo y sin clave:
#   python taller.py ejecutar f1 fc_calculadora.py --sin-modelo "9**9**9"
if sys.argv[1:2] == ["--sin-modelo"]:
    expresion = " ".join(sys.argv[2:]) or "9**9**9"
    print(f"calculadora({expresion!r}) = {calculadora(expresion)}")
    sys.exit()

# La pregunta: la de la demo o la que escribas detrás del nombre del programa, entre comillas:
#   python taller.py ejecutar f1 fc_calculadora.py "¿Cuánto es 9**9**9?"
PREGUNTA = " ".join(sys.argv[1:]) or ("Un pedido suma 1250 € de producto y 3750 € de portes. "
                                      "¿Cuál es el total CON el IVA del 21 % ya aplicado? Da una sola cifra final.")
print("== PREGUNTA ==\n" + PREGUNTA + "\n")

messages = [
    {"role": "system", "content": "Eres preciso con las cuentas. Usa la herramienta calculadora; nunca calculas mentalmente."},
    {"role": "user", "content": PREGUNTA},
]

# 2) Le pasamos la pregunta y el esquema. Si quiere calcular, el modelo NO responde con texto:
#    devuelve un tool_call (un JSON con el nombre de la tool y sus argumentos).
# 3) NUESTRO programa decide si la ejecuta y le devuelve el resultado. Se repite hasta que el modelo
#    responde con texto (como mucho 5 rondas, para que nunca se quede dando vueltas).
for ronda in range(1, 6):
    msg = preguntar(messages=messages, tools=tools)
    print(f"== RESPUESTA {ronda} DEL MODELO ==")
    if not msg.tool_calls and not (msg.content or "").strip():   # a veces un modelo gratuito responde en blanco
        print("(el modelo no ha dicho nada: le pido que siga)\n")
        messages.append({"role": "user", "content": "Sigue hasta dar la respuesta final."})
        continue
    if not msg.tool_calls:
        print(msg.content)
        break
    print("content:", repr(msg.content))
    print("tool_calls (JSON crudo devuelto por el modelo):")
    print(json.dumps([tc.model_dump() for tc in msg.tool_calls], indent=2, ensure_ascii=False))
    messages.append({"role": "assistant", "content": msg.content, "tool_calls": [tc.model_dump() for tc in msg.tool_calls]})
    for tc in msg.tool_calls:
        # Aquí nuestro programa podría pedir permiso, o negarse
        try:
            args = json.loads(tc.function.arguments or "{}")
            resultado = calculadora(**args)
        except (TypeError, ValueError) as e:
            args, resultado = tc.function.arguments, f"ERROR: argumentos no válidos ({e})"
        print(f"\n== EJECUCIÓN LOCAL (nuestro código) ==\ncalculadora({args}) = {resultado}\n")
        messages.append({"role": "tool", "tool_call_id": tc.id, "content": resultado})
else:
    print("\nEl modelo ha seguido pidiendo la calculadora 5 veces: lo paro aquí.")
