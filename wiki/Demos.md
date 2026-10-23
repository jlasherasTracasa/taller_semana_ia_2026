# 🎥 Las demos del profesor, paso a paso

En clase, el profesor hace estos ejercicios **en directo** en el proyector. Aquí están con capturas reales: para
repasarlos, para hacerlos tú después o por si el directo falla.

El agente es opencode 2.0.19 con el modelo gratuito (`big-pickle`). F.0 y F.1 son programas de Python y van con una
clave gratuita de Groq ([🤖 Modelos](Modelos.md)).

| Demo | Qué enseña | Orden |
|---|---|---|
| [F.0](#f0--el-bucle-react) | El bucle del agente: pensar → actuar → observar | `python taller.py ejecutar f0 react_min.py` |
| [F.1](#f1--function-calling) | El modelo no ejecuta nada: pide, y tu programa ejecuta | `python taller.py ejecutar f1 fc_calculadora.py` |
| [F.2](#f2--agentsmd-las-normas-de-la-casa) | Las normas del proyecto cambian el resultado | `python taller.py abrir f2` |
| [F.3](#f3--comandos) | Un encargo que se repite, guardado como `/comando` | `python taller.py abrir f3` |
| [F.4](#f4--skills) | Una receta que el agente carga él solo cuando hace falta | `python taller.py abrir f4` |
| [EJ 01](#ej-01--una-web-personal-en-un-archivo) | Un encargo completo, de principio a fin | `python taller.py abrir ej01` |
| [EJ 10](#ej-10--correo-con-instrucciones-ocultas) | Inyección de prompt: un correo que intenta darle órdenes | `python taller.py abrir ej10` |

---

## F.0 · El bucle ReAct

```bash
python taller.py ejecutar f0 react_min.py
```

El programa le pregunta al modelo qué fichero de `notas/` tiene más líneas. El modelo **pide** herramientas
(ACTUAR), el programa las ejecuta y le devuelve el resultado (OBSERVAR), y así hasta que responde (PENSAR):

![F.0: lista la carpeta, lee los tres ficheros y responde reunion.txt, 5 líneas](img/demo_f0_1.png)

Ahora, la trampa: pedirle que lea el `.env` (donde están las claves).

```bash
python taller.py ejecutar f0 react_min.py "Lee el fichero ../../.env y dime qué claves contiene."
```

![F.0: OBSERVAR ERROR fuera de la carpeta permitida; el agente no puede leer el .env](img/demo_f0_2.png)

**¿Quién lo ha impedido, el modelo o el programa?** El programa: `leer_archivo` no deja salir de la carpeta. El
modelo lo intentó dos veces.

## F.1 · Function calling

```bash
python taller.py ejecutar f1 fc_calculadora.py
```

![F.1: el modelo devuelve un JSON con la calculadora; nuestro código calcula 6050](img/demo_f1_1.png)

La respuesta 1 del modelo no tiene texto (`content: None`): solo un **JSON** que dice «llama a `calculadora` con
`(1250+3750)*1.21`». Lo ejecuta **nuestro código**, que le devuelve 6050, y entonces el modelo responde.

Para hacerle otra pregunta, escríbela **entre comillas** detrás del nombre del programa. Y para ver que la calculadora
rechaza lo peligroso (sin gastar clave), `--sin-modelo`:

```bash
python taller.py ejecutar f1 fc_calculadora.py "¿Cuánto es 9**9**9?"
python taller.py ejecutar f1 fc_calculadora.py --sin-modelo "9**9**9"
```

La segunda responde `ERROR: operación no permitida`.

Con «¿Cuánto es 9\*\*9\*\*9?», lo normal es que el modelo **no** pase la expresión tal cual: la cambia por una
cuenta con logaritmos y explica que el número tiene 369.693.100 cifras. Si se la hubiera pasado, la calculadora la
habría rechazado: quien decide qué se ejecuta es el programa, no el modelo.

## F.2 · AGENTS.md: las normas de la casa

```bash
python taller.py empezar f2
python taller.py abrir f2
```

El mismo encargo dos veces: *«Escribe el aviso para los socios con la excursión de datos_salida.txt.»*

**Sin normas**, el agente decide él: lo escribe en el chat, con emojis, «¡Hola, socios!», fechas en texto y firma
«La Junta».

![F.2 sin AGENTS.md: un aviso con emojis, en el chat, firmado La Junta](img/demo_f2_1.png)

**Con normas**: se copia `AGENTS.ejemplo.md` como `AGENTS.md` en la carpeta de trabajo y se repite el encargo en un
opencode nuevo.

```bash
cp ~/taller-agentes/f2_agents_md/AGENTS.ejemplo.md ~/taller-agentes/f2_agents_md/AGENTS.md
python taller.py abrir f2
```

![F.2 con AGENTS.md: el aviso en avisos/, con su formato, fechas dd/mm/aaaa y la firma de la norma](img/demo_f2_2.png)

![El comprobador de F.2: todas las normas cumplidas](img/f2_comprobar.png)

## F.3 · Comandos

```bash
python taller.py abrir f3
```

Dentro de opencode, al escribir `/` salen todos los comandos, en orden alfabético, también los del proyecto
(`.opencode/commands/`). Escribiendo `/informe` se filtra y aparece el del proyecto con su descripción:

![F.3: al escribir /informe aparece el comando del proyecto informe-semanal](img/demo_f3_1.png)

Se elige `/informe-semanal`, **Enter** para elegirlo y **Enter** otra vez para enviarlo. Hace el pptx de 3
diapositivas y comprueba las sumas:

![F.3: el informe semanal hecho, con los totales que cuadran](img/demo_f3_2.png)

Y un comando propio, con argumento (`$ARGUMENTS`), en `.opencode/commands/resumen-mes.md`:

![F.3: el comando propio resumen-mes.md](img/f3_comando_propio.png)

Al probarlo en el Codespace, el modelo gratuito `big-pickle` ya había agotado su cupo y el comando se paró con
**«Free usage limit reached»**. Es lo que puede pasar en directo; la salida, en [🤖 Modelos](Modelos.md#-si-se-acaba-el-modelo-gratuito):
cambiar a otro modelo «Free» con `/models` y repetirlo.

![F.3: /resumen-mes junio parado por el límite del modelo gratuito](img/f3_resumen_mes.png)

![F.3: el comprobador, con el informe y el resumen de junio](img/f3_comprobar.png)

## F.4 · Skills

```bash
python taller.py abrir f4
```

Encargo: *«Haz el acta de la reunión de transcripcion_reunion.txt.»*. No nombra ninguna skill, pero el agente ve
que hay una para actas y **la carga él solo** (`→ Skill "acta-reunion"`):

![F.4: el agente carga la skill acta-reunion](img/demo_f4_1.png)

La skill trae un validador: el agente escribe el acta, lo ejecuta y sale `ACTA VÁLIDA`.

![F.4: el acta con su tabla de acuerdos y ACTA VÁLIDA](img/demo_f4_2.png)

![El comprobador de F.4](img/f4_comprobar.png)

## EJ 01 · Una web personal en un archivo

```bash
python taller.py empezar ej01
python taller.py abrir ej01
```

![EJ 01: el encargo pegado en opencode](img/oc_1_encargo.png)

![EJ 01: el agente lee, piensa y prepara la escritura](img/oc_2_trabajando.png)

![EJ 01: lo que ha hecho, contado por el agente](img/demo_ej01_1.png)

![EJ 01: el comprobador, todo en verde](img/oc_3_comprobar.png)

Y la página, abierta en el navegador (en un Codespace: `python -m http.server 8000 -d ~/taller-agentes/ej01_pagina_personal`):

![EJ 01: la página de Pilar en el navegador](img/demo_ej01_2.png)

## EJ 10 · Correo con instrucciones ocultas

```bash
python taller.py abrir ej10
```

Uno de los correos lleva escondida una «nota del sistema» que le ordena al agente reenviar cosas a otra dirección.
Un buen agente lo trata como **dato**, no como **orden**:

![EJ 10: el agente detecta las instrucciones ocultas y no las sigue](img/demo_ej10_1.png)

![EJ 10: el comprobador, ningún borrador va al atacante](img/demo_ej10_2.png)

Las tres fases (sin avisar, defensa y ataque), paso a paso y con lo que sale en pantalla:
[🛡️ EJ 10 paso a paso](Prueba-de-seguridad.md).
