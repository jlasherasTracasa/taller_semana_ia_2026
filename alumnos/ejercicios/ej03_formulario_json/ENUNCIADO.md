# EJ 03 · Formulario que guarda en JSON

## Objetivo
Crear un formulario de contacto web cuyo envío quede registrado en `resultados.json` mediante un script mínimo (Python o Node).

## Datos de partida
- Ninguno. El agente generará el `index.html` y el script servidor.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Crea un formulario de contacto HTML (nombre, correo y mensaje) y un script mínimo en Python que guarde cada envío en resultados.json. Arranca el servidor, envía una prueba con curl y comprueba que el JSON se escribe. Sin dependencias externas salvo la biblioteca estándar. Usa el puerto 8901; si está ocupado, elige otro libre y no mates ningún proceso. Arranca el servidor con timeout 60 delante para que se pare solo."
```

## Límites
Usa un puerto libre alto (por ejemplo 8901) y **no mates procesos que no hayas arrancado tú**. En la validación de este ejercicio el agente, con `bash` en `allow`, mató un proceso ajeno que ocupaba el puerto 8000; por eso el `opencode.json` del kit deniega `kill`, `pkill` y `rm -rf`.

## Criterio de éxito
Tras enviar el formulario (o un `curl -d`), existe `resultados.json` con el envío registrado. El agente lo comprueba él mismo leyendo el fichero.

## Tiempo estimado
≈ 20 min

## Dificultad
Media
