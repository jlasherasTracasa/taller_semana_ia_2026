# EJ 21 · Programar la tarea (cron)

## Objetivo
Automatizar la vigilancia del EJ 20 para que se ejecute sola cada cierto tiempo, sin que nadie la lance.

## Datos de partida
- `vigila/bin/vigila_cambios.sh` — script de vigilancia (copia del validado en el EJ 20).
- Nota de entorno: si no tienes `cron`, el equivalente moderno es un **timer de systemd usuario** (ver guía, EJ 21).

## Prompt sugerido
Este ejercicio se hace en **modo interactivo** (`opencode`, sin `run`): el `opencode.json` del kit marca
`systemctl *` y `crontab *` como `ask`, así que el agente **te pedirá permiso** antes de tocar tu sistema.
En `opencode run` (no interactivo) esa petición se quedaría bloqueada. Lee cada orden antes de aprobarla.

```bash
$ opencode --model vllm/GLM-5.3-Flash
> Quiero ejecutar vigila/bin/vigila_cambios.sh cada minuto. Si en este equipo no hay cron, usa un timer de systemd usuario equivalente. Genera los ficheros de unidad, arranca el timer, espera a que se registren al menos dos entradas en vigila/log/vigilancia.log y desactiva después el timer dejando el sistema limpio.
```

## Criterio de éxito
Línea de cron o ficheros `.service` + `.timer` correctos; tras dos disparos, el log muestra al menos dos entradas separadas ~60 s. Al acabar la prueba, desactiva el timer (`systemctl --user disable --now`) para dejar el sistema limpio.

## Tiempo estimado
≈ 20 min

## Dificultad
Alta
