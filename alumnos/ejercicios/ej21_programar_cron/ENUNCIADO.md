# 🟣 EJ 21 · Programar una tarea periódica (con tu permiso)

> 🗂️ **Documentos y tareas repetitivas** · 🟣 Avanzado · ⏱ 20 min · 🛠️ `opencode` interactivo · Recomendado para: 💻

## 📌 La situación

La comprobación de la web tiene que ejecutarse sola cada cierto tiempo. El agente va a tocar tu sistema, así que te pedirá permiso.

## 🎯 Objetivo

Programar la vigilancia con cron o un timer de systemd **aprobando** cada orden que toca el sistema.

## 📦 Lo que tienes en esta carpeta

- `vigila/bin/vigila_cambios.sh`: el script del EJ 20.

## 💬 El encargo

Modo **interactivo** (el kit pone `crontab` y `systemctl` en `ask`; en `opencode run` la pregunta se quedaría colgada):
```bash
opencode
> Quiero ejecutar vigila/bin/vigila_cambios.sh cada minuto. Si en este equipo no hay cron, usa un timer de systemd de usuario. Genera los ficheros, arranca el timer, espera a que haya al menos dos entradas en vigila/log/vigilancia.log y desactívalo después dejando el sistema limpio.
```
Lee cada orden antes de aprobarla.

## ✅ ¿Lo ha hecho de verdad?

- El log tiene al menos dos entradas separadas ~60 s.
- Al terminar no queda el timer: `systemctl --user list-timers`.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Validado con `opencode run --auto` (aprueba los `ask`): timer de systemd de usuario, dos disparos a 60 s exactos y sistema limpio. **Comprobado a mano** que no quedó ningún timer ni unidad.

Prompt, salida real y ficheros: [`soluciones/ej21_programar_cron/`](../../soluciones/ej21_programar_cron/)

## 🔀 Siguiente paso

- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
- **Auditar permisos** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
