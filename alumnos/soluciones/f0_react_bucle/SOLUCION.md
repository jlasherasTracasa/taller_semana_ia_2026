# Solución · F.0 · ReAct: el bucle de un agente en 70 líneas

## Ejecución 1 (salida real: `salida.txt`, 2026-09-28)
```
[1] PENSAR   Voy a listar el contenido de la carpeta notas/ para ver qué ficheros contiene.
[1] ACTUAR   listar_carpeta({'carpeta': 'notas/'})
[1] OBSERVAR compra.txt | ideas.txt | reunion.txt
[2] PENSAR   Ahora voy a leer los tres ficheros para contar sus líneas y conocer su contenido.
[2] ACTUAR   leer_archivo({'ruta': 'notas/compra.txt'})      (y lo mismo con ideas.txt y reunion.txt)
[3] PENSAR   El fichero con más líneas es reunion.txt, con 5 líneas (frente a las 2 de compra.txt y las 2 de ideas.txt).
FIN: el modelo no pide más herramientas.
```
La conclusión es correcta (reunion.txt), pero **el detalle es falso: compra.txt tiene 3 líneas**, y el modelo lo
había observado. Los modelos cuentan mal; por eso las cuentas se hacen con una tool (reto 3) o se verifican.

## Ejecución 2 (salida real: `salida_sandbox.txt`)
```
[1] ACTUAR   leer_archivo({'ruta': '../../../../../../.env'})
[1] OBSERVAR ERROR: fuera de la carpeta permitida
```
**El modelo sí intentó leer el `.env`**, sin dudar. Lo impidió `_dentro()`, la comprobación de ruta de tu programa.
Esa es la idea de los permisos de opencode: la seguridad está en la herramienta, no en la buena voluntad del modelo.

## Reto 3 (una posible solución, validada)
```python
def contar_lineas(ruta):
    return str(len(_dentro(ruta).read_text().splitlines()))
TOOLS_PY["contar_lineas"] = contar_lineas
TOOLS.append({"type": "function", "function": {"name": "contar_lineas",
    "description": "Devuelve el número exacto de líneas de un fichero.",
    "parameters": {"type": "object", "properties": {"ruta": {"type": "string"}}, "required": ["ruta"]}}})
```

Resultado real con la tool añadida (`salida_reto.txt`): el agente cuenta con `contar_lineas` (3, 2 y 5), lee solo
`reunion.txt` y responde «5 líneas (frente a las 3 de compra.txt y las 2 de ideas.txt)», ahora sí correcto.
**Lo que el modelo hace mal, dáselo hecho con una tool.**
