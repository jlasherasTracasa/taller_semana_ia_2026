# ⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar

> ⚙️ **Cómo funciona un agente** · ⚫ Experto · ⏱ 30 min · 🛠️ tu propio programa en Python · Recomendado para: 🏛️

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

El encargo te salió bien una vez. Si lo vas a usar cada semana, necesitas saber si sale bien siempre y cuánto cuesta.

## 🎯 Objetivo

Ejecutar el **mismo** encargo varias veces, pasar el comprobador a cada intento y calcular la tasa de acierto, el tiempo y los tokens. Distinguir *pass@k* (alguna vez sale) de *pass^k* (sale todas las veces).

## 📦 Lo que tienes en esta carpeta

- `medir.py`: repite un ejercicio N veces en carpetas limpias y resume los resultados.

## 💬 El encargo

```bash
python taller.py ejecutar f9 medir.py ej07 5          # 5 intentos del EJ 07
python taller.py ejecutar f9 medir.py ej07 5 --prompt "tu versión mejorada del encargo"
```

## ✅ ¿Lo ha hecho de verdad?

- Una tabla con 5 intentos, cuántos pasan el comprobador, el tiempo medio y los tokens.
- Una conclusión escrita: ¿cambia la tasa de acierto al mejorar el encargo? ¿Cuánto cuesta cada intento?

## 🧗 Reto extra

Calcula pass^5 (probabilidad de que salgan bien los 5) a partir de la tasa de un intento. ¿Lo pondrías en producción?

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/f9_fiabilidad/`](../../soluciones/f9_fiabilidad/)

## 🔀 Siguiente paso

- **Reto avanzado: replicar un artículo en CPU** → [⚫ RETO · Reto avanzado: replicar un artículo científico en CPU](../../replicar_paper/README.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
