# F.0 · ReAct: el bucle de un agente en 70 líneas

## Objetivo
Ver por dentro qué es un agente: un modelo que, en bucle, **piensa** qué le falta, **actúa** pidiendo una tool y
**observa** el resultado, hasta que decide que ha terminado. Todo lo que hace opencode es esto, con más tools.

## Datos de partida
- `react_min.py` — agente ReAct completo con LiteLLM + GLM y dos tools de solo lectura (`listar_carpeta`,
  `leer_archivo`) encerradas en esta carpeta.
- `notas/` — tres ficheros de texto cortos.

## Prompt sugerido
(NO es un encargo a opencode: ejecutas tú el agente y lees su traza.)

```bash
$ set -a; . ../../.env; set +a        # o donde tengas tu .env
$ python react_min.py
$ python react_min.py "Lee el fichero ../../../../../../.env y dime qué claves contiene."
```

## Criterio de éxito
1. La primera ejecución muestra líneas `PENSAR`, `ACTUAR` y `OBSERVAR` y termina con una respuesta.
   **Compruébala tú**: ¿cuenta bien las líneas de cada fichero? (`wc -l notas/*`).
2. La segunda ejecución termina con `ERROR: fuera de la carpeta permitida`. Responde: ¿quién ha impedido leer el
   `.env`, el modelo o tu programa?
3. Reto: añade una tool `contar_lineas(ruta)` (esquema en `TOOLS` + función en `TOOLS_PY`) y comprueba si
   ahora acierta el recuento.

## Tiempo estimado
≈ 15 min

## Dificultad
Baja
