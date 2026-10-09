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

## 🔀 ¿Y ahora qué?

- **Al reto final: replicar un paper en CPU** → [⚫ RETO · La torre: replicar un paper de IA en CPU](../../replicar_paper/README.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
