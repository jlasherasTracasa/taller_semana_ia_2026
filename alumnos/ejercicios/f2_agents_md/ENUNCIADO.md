# 🟢 F.2 · AGENTS.md: las normas de la casa

> ⚙️ **Cómo funciona un agente** · 🟢 Fácil · ⏱ 15 min · 🛠️ opencode interactivo · Recomendado para: 🧭 📚 💻

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Un club de montaña manda avisos a sus socios y quiere que salgan siempre con el mismo formato y la misma firma, sin repetírselo al agente cada vez.

## 🎯 Objetivo

Dar **instrucciones permanentes** al agente con un fichero `AGENTS.md` en la carpeta del proyecto, y comprobar que cambian su comportamiento sin repetirlas en cada encargo.

## 📦 Lo que tienes en esta carpeta

- `datos_salida.txt`: la próxima excursión del club.
- `AGENTS.ejemplo.md`: unas normas de la casa.

## 💬 El encargo

Vas a hacer el **mismo encargo dos veces**: primero sin normas y después con normas. Este es el encargo que
pegarás las dos veces (es el mismo; no lo cambies):

```text
Escribe el aviso para los socios con la excursión de datos_salida.txt.
```

**1. Sin normas.** En la terminal, desde la carpeta `alumnos` y con el entorno activado:

```bash
python taller.py abrir f2
```

Se abre opencode a pantalla completa. Copia el encargo de arriba, **pégalo** en la caja de abajo (`Ctrl+V`, o clic
derecho en Windows) y pulsa **Enter**. Lee el aviso que escribe: ¿lleva emojis?, ¿cómo firma?, ¿cómo escribe las
fechas? Cuando termine, sal con **`Ctrl+C`** (con la caja vacía) o escribiendo `/exit`.

**2. Pon las normas.** `AGENTS.md` es un fichero que opencode lee **solo** al arrancar, si está en la carpeta en la que
trabaja. Copia el de ejemplo con ese nombre (esta orden vale igual en PowerShell, Linux y Mac):

```bash
cp ~/taller-agentes/f2_agents_md/AGENTS.ejemplo.md ~/taller-agentes/f2_agents_md/AGENTS.md
```

(O con el explorador de archivos: en tu carpeta `taller-agentes/f2_agents_md` copia `AGENTS.ejemplo.md` y llama a la
copia `AGENTS.md`. En Windows, cuidado si no ves las extensiones: no tiene que quedar `AGENTS.md.md`.)

Ábrelo y léelo: son las normas del club (formato, firma, fechas, dónde guardar el aviso).

**3. Con normas.** Abre un opencode **nuevo** (así lee `AGENTS.md`) y pega **el mismo encargo**:

```bash
python taller.py abrir f2
```

Esta vez el aviso debe quedar guardado en `avisos/2026-11-08_….md`, con la firma y las fechas de las normas. Sal con
`Ctrl+C`.

**4. Compara** los dos avisos. ¿Qué normas ha cumplido? ¿Alguna se ha saltado? Y compruébalo con la orden de abajo.

<details><summary>Sin conversar, de una vez (opcional)</summary>

`python taller.py lanzar f2` hace el encargo sin abrir la pantalla interactiva: sin `AGENTS.md` es el paso 1 y, con
`AGENTS.md`, el paso 3.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- Con `AGENTS.md`, el aviso se guarda en `avisos/2026-11-08_*.md`.
- Empieza por `Aviso:`, tiene `Qué llevar:` y firma `Junta del Club Andía`.
- Máximo 150 palabras, sin emojis, fechas como `08/11/2026`.

```bash
python taller.py comprobar f2      # el agente no decide si está bien: lo decide el comprobador
```

## 🧗 Reto extra

Escribe tus propias normas (tu empresa, tu clase, tu casa) y pruébalas con tres encargos distintos.

## 🧪 Lo que pasó al validarlo (11-10-2026)

El 11-10 se saltó una vez la norma de las fechas («domingo 8 de noviembre»). Con la norma reforzada con un ejemplo en `AGENTS.md`, la cumple. Sin `AGENTS.md`: emojis, firma inventada y una pregunta final.

Con el modelo gratuito de opencode (`big-pickle`): ✅ cumple el criterio.

Prompt, salida real y ficheros: [`soluciones/f2_agents_md/`](../../soluciones/f2_agents_md/)

## 🔀 Siguiente paso

- **Quiero un atajo para un encargo que repito** → [🔵 F.3 · Comandos: el encargo de todos los lunes en una palabra](../f3_comandos/ENUNCIADO.md)
- **Quiero enseñarle una receta que use solo cuando haga falta** → [🔵 F.4 · Skills: recetas que el agente carga cuando las necesita](../f4_skills/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
