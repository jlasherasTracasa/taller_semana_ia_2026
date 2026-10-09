# EJ 20 · Vigilar una web pública

## Objetivo
Primera mitad de una rutina: un script que comprueba si una página web ha cambiado y deja constancia en un log.
En el EJ 21 lo programarás para que se ejecute solo.

## Datos de partida
- Ninguno. El agente crea `vigila/bin/vigila_cambios.sh` desde cero.

## Prompt sugerido
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Crea vigila/bin/vigila_cambios.sh: descarga https://example.com con curl, calcula su hash SHA-256, lo compara con el guardado en vigila/hash.txt y añade una línea con fecha a vigila/log/vigilancia.log (inicio, sin cambios o CAMBIO DETECTADO). Las rutas deben calcularse a partir de la ubicación del propio script, sin rutas absolutas, para que funcione se lance desde donde se lance. Ejecútalo dos veces y enséñame el log."
```

## Criterio de éxito
- El script funciona lanzado desde cualquier carpeta (prueba `cd /tmp && bash ~/…/vigila_cambios.sh`).
- `vigila/log/vigilancia.log` tiene dos líneas: «inicio vigilancia hash=…» y «sin cambios (…)».
- No hay rutas absolutas escritas a mano en el script.

## Pistas
- `DIR="$(cd "$(dirname "$0")/.." && pwd)"` da la carpeta `vigila/` sea cual sea el directorio actual.
- `sha256sum` corta con `cut -d' ' -f1`.

## Tiempo estimado
≈ 15 min

## Dificultad
Media
