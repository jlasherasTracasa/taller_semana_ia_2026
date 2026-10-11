# Revisión de código · PR #42 — Búsqueda por nombre, cuota juvenil y avisos por SMS

**Revisor:** revisión tipo senior · **Fecha:** 2026-10-11
**Ficheros revisados:** `cambio.diff`, `DESCRIPCION_PR.md`
**Referencias de línea:** numeración del fichero resultante según el diff.

## Resumen

El PR responde a una necesidad real (búsqueda por nombre para secretaría) y añade funcionalidad razonable (cuota juvenil, avisos por SMS). Sin embargo:

- Introduce dos fallos de seguridad graves: **inyección SQL** y una **clave de API en producción escrita en el código**.
- Contiene una **regresión silenciosa**: un socio de 65 años pierde la tarifa de jubilado, y se **enmascara borrando los tests** que la habrían detectado.
- El envío masivo de SMS traga excepciones con `except: pass` y reporta éxito siempre, además de enviar datos personales a un tercero sin control.

La descripción del PR admite «he quitado un par de tests que fallaban con el cambio». Eso no es adaptar tests al nuevo comportamiento: es eliminar las alarmas. Es la señal de proceso más preocupante de todo el PR.

| # | Severidad | Problema | Fichero |
|---|-----------|----------|---------|
| 1 | 🔴 Crítico | Inyección SQL en la búsqueda por nombre | `app/socios.py` L12–14 |
| 2 | 🔴 Crítico | Clave de API en texto plano en el código | `app/socios.py` L5 |
| 3 | 🟠 Alto | Regresión: a los 65 años ya no se aplica la cuota de jubilado | `app/socios.py` L28 |
| 4 | 🟠 Alto | Tests borrados para que el PR pase | `tests/test_socios.py` L11–14 |
| 5 | 🟡 Medio | `except: pass` + éxito reportado siempre | `app/socios.py` L37–42 |
| 6 | 🟡 Medio | Datos personales (teléfonos, DNI) hacia un tercero sin base legal ni minimización | `app/socios.py` L36, L39 |
| 7 | 🟡 Medio | Cambio de API pública (`buscar_socio` → `buscar_socios`) sin migración | `app/socios.py` L12 |
| 8 | 🟢 Bajo | Dependencia `requests` sin declarar; `print` en vez de logger | `app/socios.py` L2, L42 |

---

## 1. 🔴 Crítico — Inyección SQL en la búsqueda por nombre

**Fichero/línea:** `app/socios.py`, líneas 12–14 (función `buscar_socios`)

**Qué pasa:** el valor de `texto` llega del usuario y se concatena directamente en la consulta:

```python
consulta = "SELECT nombre, dni, telefono FROM socios WHERE nombre LIKE '%" + texto + "%'"
return conn.execute(consulta).fetchall()
```

**Por qué importa:** cualquier entrada como `'; DROP TABLE socios; --` o `' OR '1'='1` se ejecuta como SQL: vaciado o manipulación de la tabla, y extracción de la base de datos completa (DNI y teléfonos incluidos). El código anterior ya usaba consultas parametrizadas; este cambio lo elimina. Es el fallo más grave del PR junto con la clave filtrada.

**Cómo corregirlo:** volver a parámetros (`?`). Para `LIKE`, construir el patrón con comodines escapando `%` y `_` del usuario:

```python
def buscar_socios(conn, texto):
    patron = "%" + texto.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"
    return conn.execute(
        "SELECT nombre, dni, telefono FROM socios WHERE nombre LIKE ? ESCAPE '\\'",
        (patron,),
    ).fetchall()
```

Añadir un test: `buscar_socios(conn, "' OR '1'='1")` debe devolver exactamente los socios cuyo nombre contenga esa cadena, es decir, ninguno.

---

## 2. 🔴 Crítico — Clave de API en texto plano en el código

**Fichero/línea:** `app/socios.py`, línea 5

**Qué pasa:** la clave del servicio de envíos queda escrita en el código:

```python
API_KEY = "***"   # clave del servicio de envíos
```

Es prefijo `sk-live-`: es una clave de producción, no de pruebas.

**Por qué importa:** queda en el historial de git para siempre; cualquiera con acceso al repo (o a una copia/fork) obtiene acceso de pago al servicio de SMS y puede hacer spam a coste de la organización. Una vez filtrada, borrarla de una rama no sirve: hay que rotarla. Además la clave viaja de nuevo dentro del cuerpo del POST, lo que hace que acabe en logs del proveedor.

**Cómo corregirlo:**

1. **Rotar la clave hoy mismo** (asumir comprometida desde el momento del commit).
2. Leerla del entorno y fallar pronto si falta:

```python
import os

API_KEY = os.environ.get("SMS_API_KEY")
if not API_KEY:
    raise RuntimeError("SMS_API_KEY no configurada")
```

3. Enviarla por cabecera, no en el cuerpo:

```python
headers={"Authorization": f"Bearer {API_KEY}"}
```

4. Añadir un escáner de secretos al CI (p. ej. gitleaks) para que esto no vuelva a pasar.

---

## 3. 🟠 Alto — Regresión: a los 65 años ya no se aplica la cuota de jubilado

**Fichero/línea:** `app/socios.py`, línea 28 (función `cuota_anual`)

**Qué pasa:** el cambio de `edad >= 65` a `edad > 65` altera el caso límite: un socio de **65 años exactos** pasa de pagar 15 € a pagar 30 €.

```python
def cuota_anual(edad):
    if edad > 65:      # antes: edad >= 65
        return 15
```

**Por qué importa:** nadie lo pide en el PR, no está documentado y probablemente el autor lo hizo por accidente al reordenar. Afecta a cobros reales: todo socio de 65 años exactos sería facturado al doble. Es exactamente el tipo de regresión silenciosa que sale a la luz con una reclamación meses después.

**Cómo corregirlo:** restaurar el límite inclusivo y añadir la nueva tarifa juvenil debajo:

```python
def cuota_anual(edad):
    if edad >= 65:
        return 15
    if edad < 18:
        return 10
    return 30
```

Y cubrir los bordes con tests (ver problema 4): `cuota_anual(64) == 30`, `cuota_anual(65) == 15`, `cuota_anual(17) == 10`, `cuota_anual(18) == 30`.

---

## 4. 🟠 Alto — Tests borrados para que el PR pase

**Fichero/línea:** `tests/test_socios.py`, líneas eliminadas 11–14 (hunk `@@ -8,6 +8,3 @@`): se elimina `test_cuota_jubilado` y la aserción sobre `buscar_socio`.

**Qué pasa:** en lugar de actualizar los tests al nuevo comportamiento, se eliminan. El autor lo confirma en `DESCRIPCION_PR.md`: «He quitado un par de tests que fallaban con el cambio».

**Por qué importa:** los tests que fallaban eran exactamente los guardianes de los problemas 3 y 7. Borrandolos, la suite pasa en verde y la regresión entra a producción sin nadie la detecte. Un test que falla tras un cambio funcional significa «el comportamiento cambió: decide si eso es correcto y documenta/tests actualizados», no «quita el test». Esto convierte un bug puntual en un fallo de proceso que se repetirá.

**Cómo corregirlo:** restaurar los tests eliminados y ampliarlos al nuevo comportamiento:

```python
def test_cuota_jubilado_incluye_65():
    assert cuota_anual(65) == 15

def test_cuota_juvenil():
    assert cuota_anual(17) == 10
    assert cuota_anual(18) == 30

def test_busqueda_por_nombre(conn):
    alta_socio(conn, "Ane Goñi", "12345678Z", "600000000")
    resultados = buscar_socios(conn, "Goñi")
    assert ("Ane Goñi", "12345678Z", "600000000") in resultados
```

Si algún test realmente queda obsoleto, se sustituye en el mismo PR por su equivalente para la nueva API, nunca se borra sin más.

---

## 5. 🟡 Medio — `except: pass`: errores invisibles y éxito garantizado (falso)

**Fichero/línea:** `app/socios.py`, líneas 37–42 (función `avisar_socios`)

**Qué pasa:** cada envío va envuelto en `try/except` desnudo que descarta cualquier error, y al final se imprime éxito incondicional:

```python
try:
    requests.post("https://api.envios-ejemplo.com/sms", json={...})
except:
    pass
print("Avisos enviados a todos los socios")
```

**Por qué importa:** el `except` desnudo atrapa *todo* —incluido `KeyboardInterrupt` y `SystemExit`— y oculta fallos reales: caída del proveedor, clave inválida (401), teléfono mal formateado (400), sin cuota contratada. Si el proveedor está caído, la función imprime «Avisos enviados a todos los socios» y secretaría no reenvía el aviso pensando que ya está hecho. Además no hay `timeout`: sin él, `requests.post` puede bloquearse indefinidamente.

**Cómo corregirlo:** capturar la excepción concreta, registrarla, comprobar la respuesta HTTP y reflejar el resultado real:

```python
import logging

logger = logging.getLogger(__name__)

def avisar_socios(conn, mensaje):
    fallos = 0
    for nombre, telefono in conn.execute("SELECT nombre, telefono FROM socios"):
        try:
            resp = requests.post(
                "https://api.envios-ejemplo.com/sms",
                json={"to": telefono, "text": mensaje},
                headers={"Authorization": f"Bearer {API_KEY}"},
                timeout=10,
            )
            resp.raise_for_status()
        except requests.RequestException as exc:
            fallos += 1
            logger.warning("SMS a %s no enviado: %s", nombre, exc)
    if fallos:
        raise RuntimeError(f"{fallos} avisos no enviados; revisar logs")
    logger.info("Avisos enviados a todos los socios")
```

---

## 6. 🟡 Medio — Datos personales hacia un tercero sin minimización ni base legal

**Fichero/línea:** `app/socios.py`, líneas 36 y 39 (bucle y POST de `avisar_socios`)

**Qué pasa:** la función lee `nombre, dni, telefono` de **todos** los socios y envía su número de teléfono a un servicio externo, de forma masiva y sin ninguna comprobación previa. En concreto, el `dni` se selecciona pero no se usa para nada.

**Por qué importa:** nombres, DNI y teléfonos son datos personales (RGPD/artículos regolarios equivalentes). Comunicarlos a un tercero exige base legal o consentimiento, contrato de encargado de tratamiento con el proveedor, y minimización: no compartir más de lo necesario. El mensaje no menciona cómo gestionar bajas («no enviar más SMS»), lo que en la práctica provoca quejas y denuncias ante la autoridad de protección de datos.

**Cómo corregirlo:**

- Minimizar: no consultar el `dni` si no se necesita. En el ejemplo del punto 5 ya se reduce a `nombre, telefono`.
- Mantener la lista dentro del sistema: enviar solo al proveedor lo imprescindible (el teléfono), y considerar un servicio interno de mensajería/EMAIL con consentimiento registrado en la tabla `socios`.

```sql
-- columna de consentimiento gestionada desde la app
ALTER TABLE socios ADD COLUMN acepta_aviso_sms INTEGER NOT NULL DEFAULT 0;
```

```python
for nombre, telefono in conn.execute(
    "SELECT nombre, telefono FROM socios WHERE acepta_aviso_sms = 1"
):
    ...
```

- Documentar en el PR quién es el encargado de tratamiento y dónde consta el consentimiento, antes de activar esto en producción.

---

## 7. 🟡 Medio — Cambio de API pública sin migración

**Fichero/línea:** `app/socios.py`, línea 12: `buscar_socio(conn, dni)` desaparece y la sustituye `buscar_socios(conn, texto)` (distinto nombre, distinta firma, distinto retorno: fila única → lista de filas).

**Por qué importa:** cualquier módulo que llame a `buscar_socio` dejará de funcionar (fallará en importación o en runtime). Como el retorno cambia de forma (una tupla frente a N tuplas), también afecta a los que iteren el resultado nuevo esperando el formato antiguo. No hay búsqueda por DNI sustituta, que es un caso de uso distinto y probablemente necesario en secretaría.

**Cómo corregirlo:** buscar todos los usos (`grep -rn "buscar_socio" app/ tests/`) y actualizarlos en este mismo PR; conservar la búsqueda por DNI si tiene consumidores:

```python
def buscar_por_dni(conn, dni):
    return conn.execute("SELECT nombre, dni, telefono FROM socios WHERE dni = ?", (dni,)).fetchone()

def buscar_socios(conn, texto):  # búsqueda por nombre (problema 1)
    ...
```

---

## 8. 🟢 Bajo — Varios menores

- **Dependencia sin declarar** (`app/socios.py`, línea 2): se añade `import requests` pero el diff no toca `requirements.txt`/`pyproject.toml`. Corregir: añadir `requests>=2.32` al manifest del proyecto.
- **`print` para resultados operativos** (línea 42): usar el módulo `logging` (ya mostrado en el punto 5), para poder enrutar por entorno.
- **Comentario residual** (línea 5): al mover la clave a variable de entorno, el comentario «# clave del servicio de envíos» debe desaparecer junto con la clave.

---

## Cosas que están bien

Para ser justos: la parametrización que había no se toca en `alta_socio`; la estructura del diff es pequeña y legible; y la funcionalidad pedida (búsqueda por nombre, cuota juvenil) es razonable y bien delimitada. Con las correcciones anteriores, el PR es perfectamente salvable.

---

## Veredicto: 🔴 **Pedir cambios**

No es aprobable en su estado actual: los problemas 1 y 2 son bloqueantes por sí solos (inyección SQL y clave de producción filtrada → rotación inmediata), y el 3+4 supone una regresión económica encubierta con tests borrados. Tras corregir, con la clave rotada, los tests restaurados/ampliados en verde y una pasada de CI con escáner de secretos, el PR puede volver a revisarse y aprobarse en la siguiente iteración. No mergear hoy.
