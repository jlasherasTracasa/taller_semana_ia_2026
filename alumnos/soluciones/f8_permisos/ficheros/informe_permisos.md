# Informe de auditoría de permisos — `opencode_inseguro.json`

**Fecha:** 11 de octubre de 2026
**Ficheros analizados:** `opencode_inseguro.json`, `comandos_prueba.txt`
**Herramienta de verificación:** `simular_permisos.py`

---

## 1. Recordatorio: cómo evalúa opencode las reglas

- Los patrones usan únicamente los comodines `*` (cualquier cadena, incluso vacía) y `?` (un carácter).
- Las reglas se evalúan **en orden de aparición** y **gana la última regla que coincide** con la orden.
- Si ninguna regla coincide, la decisión por defecto es **`ask`**.

Consecuencia clave: una regla genérica como `"*": "allow"` colocada al final **anula todas las reglas específicas anteriores**, convirtiéndolas en letra muerta.

---

## 2. Agujeros detectados

### 🔴 Agujero 1 — `"*": "allow"` anula todas las reglas anteriores (crítico)

En la configuración original, dentro de `bash` el orden es:

```
"rm -rf *"  : deny
"sudo *"    : deny
"git push *": ask
"*"         : allow      ← casi última
"kill *"    : deny
"git *"     : allow
```

Al ganar la última coincidencia, cualquier orden que toque `rm -rf *`, `sudo *` o `git push *` también coincide con `"*"`, y como esta está después, **permite** lo que las reglas anteriores pretendían prohibir.

- **Por qué es peligroso:** bloquea de papel. El simulador lo confirma: `rm -rf ~/fotos`, `sudo apt install nmap` o `git push --force origin main` se ejecutan **sin preguntar**. Es la causa directa de 11 de los 12 fallos.
- **Única excepción:** `kill *: deny` sí funciona, porque casualmente está *después* de `"*"`. Es una protección por pura suerte, no por diseño.
- **Cómo se corrige:** invertir la filosofía: poner el comodín genérico (`"*": "ask"`) **el primero** como base restrictiva, y las reglas específicas después, en orden de creciente especificidad: primero los `allow` amplios, luego los `deny`/`ask` concretos que deban prevalecer sobre ellos.

### 🔴 Agujero 2 — Patrones demasiado estrechos: huecos evidentes (crítico)

Las pocas reglas `deny` existentes cubren variantes mínimas:

- `rm -rf *` no cubre `rm -r ../otro_proyecto` (distinta forma del flag) ni `rm -fr *`. El borrado recursivo pasa sin obstáculos → el test lo confirma (`allow`).
- No existe regla alguna para: `pkill`, `chmod -R`, tuberías `curl … | sh`, lectura de claves privadas (`cat ~/.ssh/*`), `crontab` ni `git reset --hard`.

- **Por qué es peligroso:** un atacante (o el propio agente confundido) no necesita la forma exacta que se quiso bloquear; basta con escribir el comando ligeramente distinto. `pkill python` mata procesos; `chmod -R 777 .` expone todo el árbol; `curl … | sh` ejecuta código remoto arbitrario; leer `~/.ssh/id_rsa` compromete credenciales.
- **Cómo se corrige:** usar patrones por *familia de riesgo*, no por comando exacto: `rm -*`, `sudo *`, `pkill *`, `chmod -R *`, `cat ~/.ssh/*`, `curl *` y un patrón final `* | sh` que deniega cualquier ejecución de entrada tubería.

### 🟠 Agujero 3 — `"external_directory": "allow"` (alto)

Permite leer y manipular ficheros fuera del directorio de trabajo.

- **Por qué es peligroso:** convierte al agente en lector de `~/.ssh/id_rsa`, credenciales de otros proyectos, variables de entorno exportadas, etc. Está directamente relacionado con el fallo de `cat ~/.ssh/id_rsa`.
- **Cómo se corrige:** `"external_directory": "deny"`. El ámbito del agente debe ser su proyecto.

### 🟠 Agujero 4 — `"webfetch": "allow"` (alto)

Permite descargar cualquier URL sin confirmación.

- **Por qué es peligroso:** habilita dos ataques: *ingreso* (descargar y ejecutar código malicioso, como `curl … | sh`) y *exfiltración* (enviar ficheros sensibles a un servidor externo) sin dejar rastro de aprobación humana.
- **Cómo se corrige:** `"webfetch": "ask"`, de modo que cada descarga sea revisada.

### 🟡 Agujero 5 — `"edit": "allow"` (medio)

Edición de ficheros totalmente silenciosa.

- **Por qué es peligroso:** combinado con los demás permisos, permite modificar scripts de arranque, `.gitconfig` o el propio `opencode.json` (¡elevación de privilegios sobre la configuración!) sin que el humano lo vea.
- **Cómo se corrige:** `"edit": "ask"`. Se pierde algo de fluidez, pero se recupera supervisión sobre los cambios.

### 🟡 Agujero 6 — `apiKey` en claro en el fichero (medio-alto)

```
"apiKey": "***"
```

- **Por qué es peligroso:** cualquier `read: allow` (o una fuga del fichero a un repositorio) expone la credencial. Los ficheros de configuración se copian, versionan y comparten; las claves deben vivir fuera de ellos.
- **Cómo se corrige:** sustituir por interpolación de entorno: `"apiKey": "{env:LITELLM_API_KEY}"`.

---

## 3. Diseño de `opencode_seguro.json`

Principios aplicados:

1. **Base restrictiva primero:** `"*": "ask"` en primera posición — nada se permite si no hay una regla explícita posterior que lo permita.
2. **`allow` concretos después:** solo para operaciones seguras y cotidianas (`ls`, `cat`, `python3`, `git status/diff`, resto de `git`).
3. **`deny` de alto riesgo tras los `allow`:** así prevalecen sobre ellos aunque los patrones se solapen (p. ej. `cat *` va antes que `cat ~/.ssh/*`).
4. **`ask` de riesgo medio al final:** `git push *`, `git reset --hard *`, `crontab *`.
5. **Cierre duro:** `* | sh` (ejecutar algo tubería-abajo) denegado al final.

Traza de las decisiones clave (gana la última coincidencia):

| Orden | Coincide con… | Decisión |
|---|---|---|
| `sudo apt install nmap` | `*`(ask) → `sudo *` | **deny** |
| `cat ~/.ssh/id_rsa` | `*`(ask) → `cat *`(allow) → `cat ~/.ssh/*` | **deny** |
| `git push --force origin main` | `*` → `git *`(allow) → `git push *` | **ask** |
| `rm -r ../otro_proyecto` | `*` → `rm -*` | **deny** |
| `cat datos/ventas.csv` | `*` → `cat *` | **allow** |

## 4. Verificación

```
$ python3 simular_permisos.py opencode_inseguro.json   →   6/17  ❌
$ python3 simular_permisos.py opencode_seguro.json     →  17/17  ✅
```

Todos los casos de `comandos_prueba.txt` producen la decisión esperada y la clave de API ya no aparece escrita en el fichero.
