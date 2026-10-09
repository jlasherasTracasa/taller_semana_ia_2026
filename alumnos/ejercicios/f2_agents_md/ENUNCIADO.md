# 🟢 F.2 · AGENTS.md: las normas de la casa

> ⚙️ **Puerta F · La sala de máquinas** · 🟢 Fácil · ⏱ 15 min · 🛠️ `opencode run` · Recomendado para: 🧭 📚 💻

## 📖 La escena

El club de montaña quiere avisos siempre iguales: tuteo, sin emojis, firma de la junta. Se lo dices una vez y para siempre.

## 🎯 Objetivo

Dar **instrucciones permanentes** al agente con un fichero `AGENTS.md` en la carpeta del proyecto, y comprobar que cambian su comportamiento sin repetirlas en cada encargo.

## 📦 Lo que tienes en esta carpeta

- `datos_salida.txt`: la próxima excursión del club.
- `AGENTS.ejemplo.md`: unas normas de la casa.

## 💬 El encargo

1. **Sin normas.** Lanza el encargo y mira el resultado:
   ```bash
   opencode run --standalone "Escribe el aviso para los socios con la excursión de datos_salida.txt."
   ```
2. **Con normas.** Copia las normas y repite el MISMO encargo:
   ```bash
   cp AGENTS.ejemplo.md AGENTS.md
   opencode run --standalone "Escribe el aviso para los socios con la excursión de datos_salida.txt."
   ```
3. Compara los dos avisos. ¿Qué normas ha cumplido? ¿Alguna se ha saltado?

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Con `AGENTS.md`, el aviso se guarda en `avisos/2026-11-08_*.md`.
- Empieza por `Aviso:`, tiene `Qué llevar:` y firma `Junta del Club Andía`.
- Máximo 150 palabras, sin emojis, fechas como `08/11/2026`.

```bash
python3 taller.py comprobar f2      # el agente no puede darte el sello: solo el comprobador
```

## 🧗 Reto extra

Escribe tus propias normas (tu empresa, tu clase, tu casa) y pruébalas con tres encargos distintos.

## 🧪 Lo que pasó al validarlo (09-10-2026)

Con `AGENTS.md` cumplió todas las normas: carpeta `avisos/`, «Aviso:», «Qué llevar:», fechas dd/mm/aaaa y la firma. Sin él, el mismo encargo salió con emojis, firma «La organización» y una pregunta final.

Prompt, salida real y ficheros: [`soluciones/f2_agents_md/`](../../soluciones/f2_agents_md/)

## 🔀 ¿Y ahora qué?

- **Quiero un atajo para un encargo que repito** → [🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra](../f3_comandos/ENUNCIADO.md)
- **Quiero enseñarle una receta que use solo cuando haga falta** → [🔵 F.4 · Skills: recetas que el agente carga cuando las necesita](../f4_skills/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
