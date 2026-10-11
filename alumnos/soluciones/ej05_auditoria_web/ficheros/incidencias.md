# Incidencias de accesibilidad — `web_centro_mayores.html`

Auditoría del fichero original `web_centro_mayores.html`. No se ha modificado el original; todas las correcciones están aplicadas en `web_corregida.html`.

## 1. Contraste de color ❌ → ✅

**Fallo:** El fondo es morado oscuro (`background:#7a2c8f`) y el texto gris medio (`color:#4d4d4d`). El contraste es muy bajo (≈ 1,6:1) e ilegible para personas con baja visión. Además, los enlaces usan colores verdosos claros (`#8fa`, `#9aa`) que también contrastan mal con el fondo y se confunden entre sí.

**Corrección:** Fondo blanco (#ffffff) con texto gris muy oscuro casi negro (#222222), contraste ≈ 16:1. Los enlaces pasan a azul oscuro subrayado (#0b57d0), que contrasta bien sobre blanco y se distingue claramente del texto normal.

## 2. Tamaño de letra ❌ → ✅

**Fallo:** El cuerpo usa `font-size:9px`, demasiado pequeño para lectores mayores, y un enlace está aún más pequeño (`font-size:8px`). Además, se fuerza un tipo de letra decorativo ("Comic Sans MS") poco legible.

**Corrección:** Tamaño base de 18 px (muy por encima del mínimo exigido de 14 px), la fuente pasa a una pila legible del sistema (`Arial, Helvetica, sans-serif`) y todos los elementos escalan relativos a esa base. Se elimina el tamaño diminuto del enlace.

## 3. Adaptación al móvil ❌ → ✅

**Fallo:** La tabla tiene anchura fija de 900 px (etiqueta `width="900"` y regla CSS `table{width:900px}`), lo que obliga a hacer scroll horizontal en pantallas pequeñas. Falta la etiqueta `<meta name="viewport">`, imprescindible para que el móvil escale la página correctamente.

**Corrección:** Se añade `<meta name="viewport" content="width=device-width, initial-scale=1">`, se elimina la anchura fija de la tabla (`width:100%`) y se añade una media query (`@media (max-width:600px)`) que apila las celdas del horario en vertical y reduce ligeramente el tamaño base.

## 4. Atributo `lang` ❌ → ✅

**Fallo:** La etiqueta `<html>` no declara el idioma; los lectores de pantalla no saben cómo pronunciar el texto.

**Corrección:** Se añade `lang="es"` en `<html lang="es">`.

## 5. Textos alternativos de las imágenes ❌ → ✅

**Fallo:** El logo usa `<img src="logo.gif">` sin atributo `alt`; un lector de pantalla lo anuncia como "imagen" sin más información (o lo ignora si no hay `alt`).

**Corrección:** Se añade `alt="Logotipo del centro de mayores"`. Al ser un logo que solo identifica el sitio, el texto alternativo es breve y descriptivo.

## 6. Navegación con teclado ❌ → ✅

**Fallo:** El bloque `<div onclick="location='agenda.html'">` es un enlace falso: un `div` clicable no recibe foco con la tecla Tab ni responde a Enter, así que quien navega con teclado o usa lector de pantalla no puede acceder a la agenda. Además, `<h3>` aparece sin haber un `<h1>` antes (jerarquía de encabezados rota) y el enlace "leer más" apunta a `#` (no lleva a ninguna parte) mientras que el texto del párrafo dice "Pulsa AQUI", dejando el destino ambiguo.

**Corrección:**
- El `div` clicable se sustituye por un `<a href="agenda.html">` real, que es enfocable con Tab y activable con Enter.
- Se reorganiza la jerarquía de encabezados: `<h1>` para el título principal del sitio y `<h2>` para "Programa del centro".
- El enlace "leer más" se elimina por estar roto (`href="#"`) y se sustituye por un enlace real a `excursiones.html` con un texto descriptivo ("información sobre las excursiones") en lugar de un "AQUI"/"leer más" fuera de contexto.

## Decisiones tomadas sin preguntar

- **Destino del enlace del logo:** mantenemos `agenda.html`, que era el destino del `onclick` original.
- **Enlace "leer más":** el original apuntaba a `#` (enlace vacío). Decido convertirlo en un enlace a `excursiones.html` con texto significativo, coherente con el párrafo que lo precede.
- **Tamaño de letra:** el requisito mínimo es 14 px; uso 18 px porque el público objetivo son personas mayores.
