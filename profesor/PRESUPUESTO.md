# 💰 Presupuesto de GLM-5.3-Flash en OpenRouter

> Para pedir los créditos (a Mikel, a la Cátedra o a quien corresponda). Cifras **medidas**, no estimadas a ojo:
> salen de los tokens reales de la validación del 09-10-2026 (`herramientas/validacion.json`).

## Precio (OpenRouter, octubre de 2026)

| Modelo | Entrada | Salida | Entrada en caché |
|---|---:|---:|---:|
| `z-ai/glm-5.3-flash` | 0,15 $ / M tokens | 0,50 $ / M tokens | 0,03 $ / M tokens |

Admite *tool calling* (`tools`, `tool_choice`, `parallel_tool_calls`), que es lo que necesita opencode.

## Lo que gasta un ejercicio (medido)

| | Coste por ejecución |
|---|---:|
| Mediana de las 35 ejercicios medidos | **0,0125 $** (≈ 1 céntimo) |
| Media | 0,019 $ |
| La más barata (F.5 · MCP) | 0,005 $ |
| La más cara (EJ 13 · revisar un deck, 565.000 tokens de entrada) | 0,09 $ |
| **Todas los ejercicios una vez** (lo que gasta el docente en revalidar el kit) | **0,65 $** |

Lo que más gasta **no es la respuesta, es la entrada**: en cada paso del bucle el agente vuelve a leer todo el
contexto. Solo decir «hola» a opencode ya son ≈ 8.000 tokens de entrada (instrucciones del sistema y definiciones
de las tools). Por eso la entrada supone el 97 % de los tokens.

## Cuánto gasta un alumno en el taller (≈ 1 h 45 min de práctica)

| Perfil de uso | Ejecuciones | Coste por alumno |
|---|---|---:|
| **Bajo** · explorador, 4-5 ejercicios sin repetir | 5 × 0,0125 $ | **0,06 $** |
| **Esperado** · 7 ejercicios y la mitad repetidos para mejorar el encargo | 10 × 0,019 $ | **0,20 $** |
| **Alto** · arquitecto/programador: 20 ejecuciones, sesiones interactivas largas (+50 %), F.9 y el reto avanzado | 20 × 0,019 $ × 1,5 + 0,10 $ | **0,70 $** |

Más un fijo de **5 $** para el docente: demos en directo y una revalidación completa del kit la víspera (0,65 $ cada una).

## 👉 Cuánto pedir según el número de alumnos

Rango en dólares (OpenRouter factura en $). La última columna es el máximo más un 20 % de margen, redondeado a 5 $.

| Alumnos | Mínimo | Esperado | Máximo prudente | **Pedir** |
|---:|---:|---:|---:|---:|
| 10 | 6 $ | 7 $ | 12 $ | **15 $** |
| 20 | 6 $ | 9 $ | 19 $ | **25 $** |
| 30 | 7 $ | 11 $ | 26 $ | **35 $** |
| 40 | 7 $ | 13 $ | 33 $ | **40 $** |
| 50 | 8 $ | 15 $ | 40 $ | **50 $** |
| 60 | 9 $ | 17 $ | 47 $ | **60 $** |
| 80 | 10 $ | 21 $ | 61 $ | **75 $** |
| 100 | 11 $ | 25 $ | 75 $ | **90 $** |

**Regla rápida:** `pedir ≈ (0,70 $ × alumnos + 5 $) × 1,2`. Para un aula típica de 30 personas: **35 $**.
Lo que sobre se queda en la cuenta para la próxima edición (los créditos de OpenRouter no se pierden al acabar el taller).

## Para que nadie se coma el presupuesto

- Crea **una clave por alumno** (o por pareja) con **límite de crédito de 1 $** (OpenRouter → *Keys* → *Credit limit*).
  Un alumno que deje un agente en bucle no puede gastar más que eso.
- `doom_loop: deny` en el `opencode.json` del kit corta los bucles infinitos.
- `taller.py lanzar` enseña al alumno los tokens y el coste de cada encargo: que lo vean es parte de la lección.
- Las cifras son un **techo**: la validación se hizo contra un LiteLLM que no informa de la caché; en OpenRouter, la
  parte repetida del contexto se cobra a 0,03 $/M en vez de 0,15 $/M, así que el gasto real debería ser menor.
- OpenRouter cobra una pequeña comisión al comprar créditos: compruébala al pagar y redondea hacia arriba.

## Cómo se ha medido

`python3 taller.py lanzar` y `medir.py` (F.9) leen `opencode stats --json --project .` en cada carpeta de trabajo;
para la tabla se sumaron los tokens de todas las sesiones de la ronda de validación desde la base de datos local
de opencode. El precio es el publicado por la API de modelos de OpenRouter el 09-10-2026.
