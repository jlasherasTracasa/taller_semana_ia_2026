# 🟣 EJ 21 · Programar una tarea periódica (con tu permiso)

> 🗂️ **Documentos y tareas repetitivas** · 🟣 Avanzado · ⏱ 20 min · 🛠️ solo opencode interactivo · Recomendado para: 💻

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

La comprobación de la web tiene que ejecutarse sola cada cierto tiempo. El agente va a tocar tu sistema, así que te pedirá permiso.

## 🎯 Objetivo

Programar la vigilancia con el programador de tareas de tu sistema (Programador de tareas de Windows, cron o systemd en Linux, launchd en macOS) **aprobando** cada orden que toca el sistema.

## 📦 Lo que tienes en esta carpeta

- `vigila/vigila_cambios.py`: el script del EJ 20.

## 💬 El encargo

Modo **interactivo** (el kit pone `schtasks`, `crontab`, `systemctl` y `launchctl` en `ask`: opencode te pregunta
antes de ejecutarlas, y en `opencode run` la pregunta se quedaría colgada):
```bash
python taller.py abrir ej21
```
Copia este encargo, pégalo en opencode y pulsa Enter:
```text
Quiero ejecutar vigila/vigila_cambios.py cada minuto con el programador de tareas de este sistema (en Windows, el Programador de tareas con schtasks; en Linux, cron o un timer de systemd de usuario; en macOS, launchd). Usa la ruta completa del Python con el que se ejecuta el kit. Crea la tarea, espera a que haya al menos dos líneas nuevas en vigila/log/vigilancia.log y después elimina la tarea dejando el sistema limpio. Enséñame el log.
```

Lee cada orden antes de aprobarla: ¿qué crea?, ¿cada cuánto?, ¿cómo se borra?

## ✅ ¿Lo ha hecho de verdad?

- El log tiene al menos dos entradas separadas unos 60 s.
- Al terminar no queda la tarea: `schtasks /query | findstr vigila` (Windows), `crontab -l` y `systemctl --user list-timers` (Linux) o `launchctl list | grep vigila` (macOS) no la muestran.

```bash
python taller.py comprobar ej21      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej21_programar_cron/`](../../soluciones/ej21_programar_cron/)

## 🔀 Siguiente paso

- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
- **Auditar permisos** → [⚫ F.8 · Auditar permisos: ¿qué puede hacer tu agente sin preguntarte?](../f8_permisos/ENUNCIADO.md)
