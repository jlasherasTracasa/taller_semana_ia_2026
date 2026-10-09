# 🛡️ Seguridad

## Las reglas de oro

1. **Las claves, en variables de entorno.** `opencode.json` solo lleva `{env:LITELLM_API_KEY}`; la clave vive en `.env`,
   que no se sube a git ni se pega en un chat.
2. **Lo que el agente lee es un dato, nunca una orden.** Correos, webs, PDF, respuestas de alumnos… pueden traer
   instrucciones escondidas (inyección de prompt). Ejercicios EJ 10 y EJ 23.
3. **Trabaja en copias.** `taller.py` prepara cada ejercicio en `~/taller-agentes/`, fuera del kit.
4. **Permite lo habitual, prohíbe lo irreversible, pregunta lo que sale de tu máquina.**
5. **«He terminado» no es una prueba.** Pasa el comprobador.
6. **Firma quien encarga.** El agente propone; tú decides.

## Permisos de opencode

```json
"permission": {
  "edit": "allow",
  "external_directory": "deny",
  "question": "deny",
  "bash": {
    "*": "allow",
    "rm -rf *": "deny", "sudo *": "deny", "kill *": "deny", "*| sh*": "deny",
    "git push *": "ask", "crontab *": "ask", "systemctl *": "ask"
  }
}
```

- `*` es «cualquier cosa» y `?` «un carácter». **Gana la última regla que coincide**: un `"*": "allow"` al final anula
  todos los `deny` anteriores (ejercicio F.8).
- Los patrones son un **cinturón, no una jaula**: `python3 -c "import shutil; shutil.rmtree('x')"` no lo para
  ningún patrón de `rm`. Para aislar de verdad: un contenedor o una máquina virtual.
- `ask` necesita a alguien delante: en `opencode run` se queda colgado. Usa el modo interactivo (EJ 21).

## Casos reales de la preparación del taller

| Qué pasó | Lección |
|---|---|
| Con `bash` libre y el puerto ocupado, el agente **mató un proceso ajeno** (EJ 03) | `deny` para `kill`; pedir `timeout 60` |
| Con 30 tools extra de un MCP global, escribió un script vacío y dijo **«Listo»** (EJ 20) | Más tools no es mejor; comprobar siempre |
| Lanzado desde un script, **escribió fuera de su carpeta** y modificó una solución del kit | Trabajar en copias; opencode usa `PWD` |
| Leyó un correo con órdenes escondidas y… **no cayó** (EJ 10) | Bien, pero no te fíes: que no tenga la tool de enviar |
| Una respuesta de examen pedía «un 10»: no cayó, pero **sumó mal** otra nota (EJ 23) | Firma quien corrige |

## Cuándo NO usar un agente

- Lo **irreversible** sin copia (borrar, enviar, pagar, publicar): que lo prepare, lo ejecutas tú.
- Lo que **no sabrías comprobar**.
- **Datos personales** de terceros (RGPD): lo que el agente lee viaja al proveedor del modelo.
- Lo que **lleva tu firma** sin revisarlo.
