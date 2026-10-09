# Revisión de código · PR #42 «Búsqueda por nombre, cuota juvenil y avisos por SMS»

**Revisor:** agente (revisión tipo senior) · **Fecha:** 2026-10-09
**Alcance:** `cambio.diff` (2 ficheros: `app/socios.py`, `tests/test_socios.py`) y `DESCRIPCION_PR.md`.
**Veredicto al final:** ❌ **Pedir cambios** (bloqueante: 2 críticos).

> Las líneas se refieren al fichero **resultante** de aplicar el diff; al venir de un diff son aproximadas, pero se identifica siempre la función concreta.

---

## 🔴 Críticos

### P1 · Inyección SQL en la búsqueda por nombre
- **Dónde:** `app/socios.py` · `buscar_socios()` · ~líneas 19–21 (hunk 1)
- **Qué pasa:** se construye la consulta por concatenación de texto:
  ```python
  consulta = "SELECT nombre, dni, telefono FROM socios WHERE nombre LIKE '%" + texto + "%'"
  ```
- **Por qué importa:** cualquier entrada como `' OR 1=1 --` (o `' ; DROP TABLE socios --`, según configuración de SQLite) altera la consulta. `texto` viene de secretaría, es decir, de usuario. Además es una **regresión**: la función anterior (`buscar_socio(conn, dni)`) usaba parámetros `(?)` correctamente.
- **Cómo corregirlo:** parametrizar y pasar el comodín como dato, nunca como código:
  ```python
  def buscar_socios(conn, texto):
      patron = f"%{texto}%"
      return conn.execute(
          "SELECT nombre, dni, telefono FROM socios WHERE nombre LIKE ?",
          (patron,),
      ).fetchall()
  ```

### P2 · Clave de API escrita en el código (secreto en el repositorio)
- **Dónde:** `app/socios.py` · constante `API_KEY` · ~línea 5 (hunk 1)
- **Qué pasa:** `API_KEY = "sk-live-4f9a2b..."` queda en texto plano en el fuente y, al ser un diff, **quedará en el historial de git para siempre** aunque se borre después.
- **Por qué importa:** cualquiera con acceso al repo puede suplantar al club en el servicio de envíos (coste económico, spam en nombre del club). El comentario «clave del servicio de envíos» confirma que es real y de producción (`sk-live-`). La clave viaja además en el cuerpo del POST (véase P6).
- **Cómo corregirlo:**
  1. **Rotar la clave ahora mismo** (está comprometida solo con existir en el PR).
  2. Cargarla de entorno y abortar si falta:
     ```python
     import os
     API_KEY = os.environ["SMS_API_KEY"]
     ```
  3. Añadir `sk-live-*` a reglas de detección de secretos en CI y quitar la clave del historial antes de mezclar (el PR no debe entrar tal cual).

---

## 🟠 Altos

### P3 · Regresión de negocio: los jubilados de 65 años pierden el descuento
- **Dónde:** `app/socios.py` · `cuota_anual()` · ~líneas 33–34 (hunk 2)
- **Qué pasa:** el código original aplicaba la tarifa reducida con `edad >= 65`; el cambio la deja en `edad > 65`. Con 65 años exactos la cuota sube de 15 € a 30 €.
- **Por qué importa:** cambia el comportamiento pactado sin que la descripción del PR lo mencione; afecta a facturación real. Es exactamente el caso que cubría el test `test_cuota_jubilado` que este mismo PR elimina (véase P4): el test no «fallaba con el cambio», **detectaba el bug**.
- **Cómo corregirlo:**
  ```python
  if edad >= 65:
      return 15
  ```

### P4 · Tests borrados para que la suite pase
- **Dónde:** `tests/test_socios.py` · ~líneas 8–12 · `test_alta_y_busqueda` (aserción recortada) y `test_cuota_jubilado` (eliminado entero)
- **Qué pasa:** en lugar de adaptar los tests a la nueva API, se eliminan. `DESCRIPCION_PR.md` lo presenta como «he quitado un par de tests que fallaban con el cambio».
- **Por qué importa:** es la práctica más peligrosa de esta revisión: convierte la suite en cómplice de las regresiones (P1 y P3). Los tests no se borran porque fallen; se arregla el código o se reescribe el test **preservando la cobertura**.
- **Cómo corregirlo:** restaurarlos adaptados a la API nueva:
  ```python
  def test_alta_y_busqueda_por_nombre(conn):
      alta_socio(conn, "Ane Goñi", "12345678Z", "600000000")
      resultados = buscar_socios(conn, "Goñi")
      assert ("Ane Goñi", "12345678Z", "600000000") in resultados

  def test_busqueda_no_inyecta_sql(conn):
      alta_socio(conn, "Ane Goñi", "12345678Z", "600000000")
      assert buscar_socios(conn, "' OR 1=1 --") == []   # P1

  def test_cuota_jubilado():
      assert cuota_anual(65) == 15                      # P3

  def test_cuota_juvenil():
      assert cuota_anual(17) == 10
      assert cuota_anual(18) == 30                      # borde de los 18
  ```

### P5 · `except: pass` que oculta errores y éxito fingido
- **Dónde:** `app/socios.py` · `avisar_socios()` · ~líneas 45–47 (hunk 2)
- **Qué pasa:** el bucle de envío traga cualquier excepción y al final imprime «Avisos enviados a todos los socios» pase lo que pase.
- **Por qué importa:** si la clave es inválida o el servicio cae, secretaría cree que los socios están avisados cuando no ha salido ni un SMS. Un `except:` desnudo además captura `KeyboardInterrupt`/`SystemExit`.
- **Cómo corregirlo:** excepciones concretas, registro de fallos y resultado honesto:
  ```python
  import logging
  log = logging.getLogger(__name__)

  def avisar_socios(conn, mensaje):
      ok, fallos = 0, []
      for nombre, dni, telefono in conn.execute("SELECT nombre, dni, telefono FROM socios"):
          try:
              r = requests.post(URL_SMS, json={"to": telefono, "text": mensaje},
                                headers={"Authorization": f"Bearer {API_KEY}"},
                                timeout=10)
              r.raise_for_status()
              ok += 1
          except requests.RequestException as e:
              log.error("SMS fallido para %s: %s", dni, e)
              fallos.append(dni)
      if fallos:
          raise RuntimeError(f"{len(fallos)} avisos sin enviar: {fallos}")
      return ok
  ```

### P6 · Envío de datos personales a un tercero sin criterio
- **Dónde:** `app/socios.py` · `avisar_socios()` · ~líneas 41–44 (hunk 2)
- **Qué pasa:** la función vuelca **todos** los teléfonos de la base de datos al servicio externo, sin límite, sin consentimiento registrado y con la clave en el cuerpo (`json={"to":..., "key": API_KEY}`).
- **Por qué importa:** datos personales de socios hacia un proveedor: obligaciones RGPD (encargado de tratamiento, minimización, derecho de oposición). Enviarlos masivamente sin control también multiplica el daño si P2 ocurre. No hay ninguna mención en la descripción del PR.
- **Cómo corregirlo:** como mínimo, lista de exclusión por socio (campo `acepta_sms`), autenticación por cabecera (no en el cuerpo) y trazabilidad de quién lanzó el envío:
  ```python
  SQL = "SELECT nombre, dni, telefono FROM socios WHERE acepta_sms = 1"
  ```

---

## 🟡 Medios

### P7 · Sin `timeout` en las peticiones HTTP
- **Dónde:** `app/socios.py` · `avisar_socios()` · ~línea 43
- **Qué pasa:** `requests.post(...)` sin `timeout`: si el proveedor no responde, el proceso se queda colgado indefinidamente.
- **Corrección:** `timeout=(3, 10)` (conexión, lectura) en cada llamada, como en el snippet de P5.

### P8 · Cambio de API sin migración: `buscar_socio` → `buscar_socios` rompe a los llamadores
- **Dónde:** `app/socios.py` · hunk 1 · ~líneas 12–14
- **Qué pasa:** cambia el nombre (singular→plural), los parámetros (dni→texto) y el tipo devuelto (fila única por `SELECT *` → lista de tuplas de 3 columnas). Cualquier llamador existente de `buscar_socio` fallará con `NameError`, y los que usaran columnas extra del `SELECT *` verán tupples distintos.
- **Por qué importa:** es un cambio rompiente de API interna que la descripción del PR no declara; combinado con P4, nadie detectará las roturas hasta producción.
- **Corrección:** mantener compatibilidad temporal (`def buscar_socio(conn, dni)` como *wrapper* deprecado) o migrar todos los llamadores en este mismo PR, y dejarlo escrito en la descripción. Escapar además los comodines `%`/`_` que el usuario pueda teclear (`texto.replace("%", r"\%")` con `ESCAPE '\'` en el SQL).

### P9 · Falsos positivos de búsqueda y sin límite de resultados
- **Dónde:** `app/socios.py` · `buscar_socios()` · ~líneas 19–21
- **Qué pasa:** `LIKE '%texto%'` sin escapar comodines (un `%` del usuario matchea todo) y `fetchall()` sin `LIMIT` sobre toda la tabla.
- **Corrección:** escapar comodines (P8) y devolver `LIMIT 50`, con paginación si hace falta en UI.

---

## 🟢 Bajos

### P10 · Detalles menores de estilo y empaquetado
- `print()` para informar de envíos → usar `logging` (coherente con P5).
- `import requests` introduce una dependencia nueva: actualizar `requirements.txt`/`pyproject.toml`.
- Constantes de módulo (`URL_SMS`, tiempos de espera) deberían ser configurables como la clave (P2).
- `DESCRIPCION_PR.md` pide mezclar «hoy»: la urgencia no reduce el radio de impacto de P1/P2/P3; mejor documentar los riesgos pendientes.

---

## Veredicto

**❌ Pedir cambios — no mezclar hoy.**

Bloqueantes: **P1** (inyección SQL, y encima es una regresión de código que ya estaba bien) y **P2** (secreto de producción en el repositorio, requiere rotación de clave inmediata). Prácticamente bloqueantes: **P3** (regresión de facturación que toca dinero) y **P4** (tests eliminados para maquillar exactamente esas dos regresiones).

Lo valioso del cambio (búsqueda por nombre, cuota juvenil, avisos SMS) es fácil de salvar: con parametrización SQL, clave por entorno, `>= 65`, excepciones explícitas y los tests restaurados/adaptados, sería un buen PR. Se recomienda revisión de nuevo cuando el autor reenvíe, y aplicar el checklist anterior como comentarios línea a línea en el PR.
