# Solución · EJ 21 · Programar la tarea (cron)

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Quiero ejecutar vigila/bin/vigila_cambios.sh cada minuto durante dos minutos. Si en este equipo no hay cron, usa un timer de systemd usuario equivalente. Genera los ficheros de unidad necesarios y dame las órdenes exactas."
```

> El docente lo validó con permisos abiertos (`opencode run`). Con el `opencode.json` del kit, hazlo en modo
> interactivo y aprueba cada `systemctl` cuando el agente lo pida (ver ENUNCIADO).

## Resultado
Unidades `vigila-cambios.service` (oneshot) y `vigila-cambios.timer` (`OnCalendar=*-*-* *:*:00`) creadas en `~/.config/systemd/user`; timer arrancado, dos entradas de log separadas 60 s y limpieza completa al terminar.

## Salida real (extracto validado 2026-09-28)
```
Log con 2 entradas en vigila/log/vigilancia.log:
  2026-09-28 20:05:07 inicio vigilancia hash=5c88674...
  2026-09-28 20:06:07 sin cambios (5c88674...)

$ systemctl --user disable --now vigila-cambios.timer && rm -f ~/.config/systemd/user/vigila-cambios.{timer,service}
OK: sin timers de vigila
```

El log real es el del extracto de arriba (se generó con la versión anterior del script, basada en md5; la de `vigila/bin/` es la validada en el EJ 20). Las unidades de referencia están en `unidades/` (el agente las borró al terminar, como se le pidió). La prueba dejó el sistema limpio (sin unidades ni timers residuales).
