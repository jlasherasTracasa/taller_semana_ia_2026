# Function calling mínimo con LiteLLM + GLM-5.3-Flash.
# El modelo NO ejecuta nada: pide una herramienta con argumentos JSON
# y es nuestro programa quien decide si la ejecuta.
import json
import os
import litellm

# En LiteLLM el prefijo del proveedor va en el nombre del modelo.
# "openai/..." = cualquier API compatible con OpenAI (aquí, LiteLLM local).
MODEL = "openai/GLM-5.3-Flash"
API_BASE = os.environ["LITELLM_API_BASE"] + "/v1"
API_KEY = os.environ["LITELLM_API_KEY"]

KW = {"api_base": API_BASE, "api_key": API_KEY}

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

messages = [
    {"role": "system", "content": "Eres preciso con las cuentas. Usa la herramienta calculadora; nunca calculas mentalmente."},
    {"role": "user", "content": "Un pedido suma 1250 € de producto y 3750 € de portes. ¿Cuál es el total CON el IVA del 21 % ya aplicado? Da una sola cifra final."},
]

# 2) Primera llamada: el modelo responde con un tool_call (JSON), no con texto.
r1 = litellm.completion(model=MODEL, messages=messages, tools=tools, **KW)
msg = r1.choices[0].message
print("== RESPUESTA 1 DEL MODELO ==")
print("content:", repr(msg.content))
print("tool_calls (JSON crudo devuelto por el modelo):")
print(json.dumps([tc.to_json() for tc in (msg.tool_calls or [])], indent=2, ensure_ascii=False))

if not msg.tool_calls:
    raise SystemExit("El modelo no pidió ninguna herramienta; relanza la demo.")

for tc in msg.tool_calls:
    # 3) NUESTRO programa decide ejecutarla (aquí podría pedir permiso o negarse).
    args = json.loads(tc.function.arguments)
    resultado = calculadora(**args)
    print(f"\n== EJECUCIÓN LOCAL (nuestro código) ==\ncalculadora({args}) = {resultado}")
    messages.append({"role": "assistant", "content": None, "tool_calls": [tc.to_json()]})
    messages.append({"role": "tool", "tool_call_id": tc.id, "content": resultado})

# 4) Devolvemos el resultado al modelo para que redacte la respuesta final.
r2 = litellm.completion(model=MODEL, messages=messages, tools=tools, **KW)
print("\n== RESPUESTA 2 DEL MODELO ==")
print(r2.choices[0].message.content)
