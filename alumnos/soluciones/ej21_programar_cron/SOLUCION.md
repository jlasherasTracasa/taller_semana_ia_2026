# ✅ Solución · EJ 21 · Programar una tarea periódica (con tu permiso)

Ejecución real del 11-10-2026 con opencode 2.0.19 y GLM-5.3-Flash, solo CPU · 93 s · 122.275 tokens de entrada y 6.530 de salida.


## Qué pasó

Validado en **modo interactivo** el 11-10 (Linux sin cron): creó un timer de systemd de usuario, pidió permiso 6 veces (`systemctl`), el log tuvo 3 entradas separadas un minuto y al final borró el timer. Sistema limpio, comprobado a mano.

## Veredicto del comprobador

```text
✅ el log tiene al menos 2 entradas (tiene 3)
  ✅ dos entradas separadas aproximadamente un minuto
  ✅ no queda ninguna tarea programada «vigila» en el sistema

🎉 Criterio de éxito cumplido · ej21
```

## Qué hay en esta carpeta

- Pasos: los del ENUNCIADO.
- `salida.txt`: lo que dijo e hizo el agente (rutas y usuario anonimizados).
- `ficheros/`: lo que creó o cambió el agente.

> Las respuestas de un modelo cambian entre ejecuciones. Compara el **criterio**, no el texto.
