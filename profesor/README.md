# 🧑‍🏫 Material del docente

| Fichero | Qué es |
|---|---|
| `notas_profesor.md.enc` | **Notas del profesor, cifradas** (AES-256): minutado, guion de demos, qué contar en cada ejercicio, problemas típicos, preguntas difíciles |
| `taller-con-notas.pptx.enc` | La presentación con notas del ponente, cifrada |
| `notas.sh` | `bash profesor/notas.sh descifrar` / `cifrar`. La contraseña **no** está en el repositorio |
| [`PRESUPUESTO.md`](PRESUPUESTO.md) | Cuánto cuesta GLM-5.3-Flash en OpenRouter según el número de alumnos (medido) |
| `validar.sh` | Ejecuta los ejercicios como un alumno y deja un resumen |

> Los alumnos tienen acceso a este repositorio: por eso las notas solo van cifradas. Lo descifrado va a
> `profesor_privado/` y a `presentacion/*-con-notas.pptx`, que están en `.gitignore`.

## Validar el kit

```bash
bash profesor/validar.sh                    # todos los ejercicios con encargo (≈ 10 min, ≈ 0,65 $)
bash profesor/validar.sh ej07 f4            # solo algunos
python3 herramientas/guardar_soluciones.py /tmp/validacion_taller/<ronda>   # copia salidas y ficheros a alumnos/soluciones
```

Necesita las claves en `alumnos/.env`. Aísla tu configuración global de opencode (`HOME` y `XDG_CONFIG_HOME`
propios): los MCP y skills globales del docente cambian el comportamiento del agente. Revisa siempre a mano lo que
falle **y lo que pase**: un OK del comprobador no lo es todo. Después, actualiza `herramientas/validacion.json`.

F.0, F.1 y F.9 son programas de Python (`python3 alumnos/taller.py ejecutar f0 react_min.py`), F.3 y EJ 21 son de modo
interactivo (`taller.py abrir …`) y conviene probarlos a mano.
