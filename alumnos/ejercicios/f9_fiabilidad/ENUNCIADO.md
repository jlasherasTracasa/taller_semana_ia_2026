# ⚫ F.9 · ¿Funciona siempre? Medir en vez de opinar

> ⚙️ **Puerta F · La sala de máquinas** · ⚫ Experto · ⏱ 30 min · 🛠️ tu propio programa en Python · Recomendado para: 🏛️

## 📖 La escena

El EJ 07 te salió bien una vez. Pilar pregunta: «¿Y mañana también?». Lo mides.

## 🎯 Objetivo

Ejecutar el **mismo** encargo varias veces, pasar el comprobador a cada intento y calcular la tasa de acierto, el tiempo y los tokens. Distinguir *pass@k* (alguna vez sale) de *pass^k* (sale todas las veces).

## 📦 Lo que tienes en esta carpeta

- `medir.py`: repite un ejercicio N veces en carpetas limpias y resume los resultados.

## 💬 El encargo

```bash
python3 taller.py ejecutar f9 medir.py ej07 5          # 5 intentos del EJ 07
python3 taller.py ejecutar f9 medir.py ej07 5 --prompt "tu versión mejorada del encargo"
```

## ✅ ¿Lo ha hecho de verdad?

- Una tabla con 5 intentos, cuántos pasan el comprobador, el tiempo medio y los tokens.
- Una conclusión escrita: ¿cambia la tasa de acierto al mejorar el encargo? ¿Cuánto cuesta cada intento?

## 🧗 Reto extra

Calcula pass^5 (probabilidad de que salgan bien los 5) a partir de la tasa de un intento. ¿Lo pondrías en producción?

## 🧪 Lo que pasó al validarlo (09-10-2026)

3 intentos del EJ 07: 3/3 aciertos, 29 s de media, ≈56.500 tokens de entrada por intento (≈0,01 $). Pero en la ronda general el EJ 07 falló: **3 de 4** en total. Mismo encargo, distinto resultado.

Prompt, salida real y ficheros: [`soluciones/f9_fiabilidad/`](../../soluciones/f9_fiabilidad/)

## 🔀 ¿Y ahora qué?

- **Al reto final: replicar un paper en CPU** → [⚫ RETO · La torre: replicar un paper de IA en CPU](../../replicar_paper/README.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
