# Auditoría de accesibilidad — `web_centro_mayores.html`

**Fecha:** 09-oct-2026 · **Referencias:** WCAG 2.1 AA · Página auditada para usuarios mayores (centro de mayores).

Resumen: **9 incidencias** (3 críticas, 4 graves, 2 menores). El original no es utilizable por este público objetivo: texto casi invisible, letra de 8–9 px, imposible de usar en móvil y sin teclado. La corrección está aplicada en **`web_corregida.html`** (el original no se ha tocado).

---

## CRÍTICAS

### 1. Contraste de color del texto principal — INUTILIZABLE
- **Dónde:** `<style>` línea 4 — `background:#7a2c8f; color:#4d4d4d`.
- **Problema:** gris medio sobre morado oscuro = **1,04 : 1**. Requiere ≥ 4,5:1 (WCAG 1.4.3). A efectos prácticos el texto es invisible sobre el fondo; es el fallo más severo de la página.
- **Corrección:** texto **blanco `#ffffff`** sobre el mismo morado → **8,13 : 1** ✓.

### 2. Tamaño de letra — 9 px y hasta 8 px
- **Dónde:** línea 4 `font-size:9px`; línea 12 enlace a `font-size:8px`.
- **Problema:** 9 px es ilegible para el público mayor; el enlace "leer mas" baja a 8 px. Ninguna cabecera destaca.
- **Corrección:** base **18 px** (recomendable ≥ 16 px, y más en este colectivo), jerarquía con `h3` a 24 px, enlaces al tamaño base.

### 3. Navegación con teclado — el menú principal no es enfocable
- **Dónde:** línea 7 — `<div onclick="location='agenda.html'">`.
- **Problema:** un `div` clicable no recibe foco ni responde a Enter/Espacio (WCAG 2.1.1 y 4.1.2). Un usuario de teclado o lector de pantalla **no puede entrar a la agenda**. Además el `<div>` no expone rol de enlace.
- **Corrección:** sustituir por `<a href="agenda.html">`, que es enfocable, activable con Enter y anunciada como enlace. Único elemento interactivo real que existía (los otros dos enlaces son trampas, ver #8).

---

## GRAVES

### 4. Sin `<meta name="viewport">` y tabla a ancho fijo — adaptación al móvil
- **Dónde:** falta en `<head>`; línea 5 `table{width:900px}` y línea 9 `<table width="900">`.
- **Problema:** los móviles renderizan a ~980 px y escalan todo a la mitad: texto ya ilegible (9 px → ~4 px efectivos) y desplazamiento horizontal obligatorio (WCAG 1.4.10). Falla el test de 320 px.
- **Corrección:** `<meta name="viewport" content="width=device-width, initial-scale=1">`, tabla a `width:100%` con celdas apilables por media query y envuelta en contenedor con desbordamiento controlado como red de seguridad.

### 5. Falta el atributo `lang`
- **Dónde:** línea 2 — `<html>`.
- **Problema:** sin `lang`, los lectores de pantalla no saben qué síntesis de voz usar (puede leer español con fonética inglesa) y los buscadores/correctores pierden contexto (WCAG 3.1.1).
- **Corrección:** `<html lang="es">`.

### 6. Imagen sin texto alternativo
- **Dónde:** línea 7 — `<img src="logo.gif">`.
- **Problema:** un lector de pantalla anuncia "imagen" sin más; si el logo fuera también enlace (está dentro del bloque de navegación), no se sabría a dónde lleva (WCAG 1.1.1).
- **Corrección:** `alt="Logotipo del centro de mayores"` (y si el conjunto fuese enlace, el `alt` describe el destino).

### 7. Enlaces con contraste insuficiente
- **Dónde:** línea 5 `a{color:#8fa}` (≈ **3,54 : 1**) y línea 12 enlace inline `color:#9aa` (**3,34 : 1**).
- **Problema:** ambos por debajo de 4,5:1 para texto normal (WCAG 1.4.3); el segundo además a 8 px.
- **Corrección:** color de enlace **`#ffd75e`** sobre el morado (**5,86 : 1** ✓), mismo tamaño que el texto, y subrayado para no depender solo del color.

---

## MENORES

### 8. Enlace trampa y texto no descriptivo
- **Dónde:** líneas 11–12 — "Pulsa **AQUI** …" + `<a href="#">leer mas</a>`.
- **Problema:** `href="#"` no lleva a ningún sitio (enlace muerto) y "leer mas"/"AQUI" no describen destino (WCAG 2.4.4). Con lectores de pantalla se listan los enlaces sueltos y estos no dicen nada.
- **Corrección:** un único enlace real: `<a href="excursiones.html">Información sobre las excursiones</a>` (si aún no existe esa página, quedará documentada como página pendiente; mejor un 404 honesto que un `#`).

### 9. Título de la página engañoso
- **Dónde:** línea 3 — `<title>Pensionista del barrio</title>`.
- **Problema:** no describe la página (habla del programa semanal del centro). Es lo que anuncian pestaña, historial y lector de pantalla (WCAG 2.4.2).
- **Corrección:** `<title>Programa semanal — Centro de Mayores</title>`.

---

## Matriz resumen

| # | Incidencia | Severidad | WCAG | Estado |
|---|---|---|---|---|
| 1 | Contraste texto 1,04:1 | Crítica | 1.4.3 | Corregida |
| 2 | Letra 8–9 px | Crítica | — (usabilidad) | Corregida |
| 3 | Menú no enfocable (`div onclick`) | Crítica | 2.1.1 / 4.1.2 | Corregida |
| 4 | Sin viewport, tabla 900 px | Grave | 1.4.10 | Corregida |
| 5 | Falta `lang="es"` | Grave | 3.1.1 | Corregida |
| 6 | `img` sin `alt` | Grave | 1.1.1 | Corregida |
| 7 | Enlaces < 4,5:1 | Grave | 1.4.3 | Corregida |
| 8 | Enlace `#` + "AQUI"/"leer mas" | Menor | 2.4.4 | Corregida |
| 9 | `<title>` genérico | Menor | 2.4.2 | Corregida |

**Contrastes verificados (WCAG 1.4.3):**

| Combinación | Ratio | Veredicto |
|---|---|---|
| `#4d4d4d` sobre `#7a2c8f` (original) | 1,04 : 1 | ✗ falla |
| `#8fa` sobre `#7a2c8f` (enlace original) | 3,54 : 1 | ✗ falla |
| `#9aa` sobre `#7a2c8f` (enlace original) | 3,34 : 1 | ✗ falla |
| `#ffffff` sobre `#7a2c8f` (corregido) | 8,13 : 1 | ✓ AAA |
| `#ffd75e` sobre `#7a2c8f` (enlace corregido) | 5,86 : 1 | ✓ AA |

## Decisiones tomadas sin preguntar

1. **Paleta conservada** (morado de fondo) pero texto blanco y enlaces ámbar: se mantiene la identidad con contrastes AAA/AA.
2. **Fuente:** se sustituye *Comic Sans MS* por una pila legible (`Verdana, Geneva, sans-serif`): Verdana tiene trazos anchos y buena diferenciación de caracteres para mayores; si se desea otra, cambiar una línea.
3. **Tabla del programa:** en móvil (≤600 px) cada día pasa a bloque apilado en vez de scroller horizontal; sigue siendo una `<table>` semántica para lectores de pantalla.
4. **Páginas de destino:** `agenda.html` se conserva como en el onclick original; las excursiones apuntan a `excursiones.html` (nueva); el logo deja de ser enlace (no lo era funcionalmente para teclado).
5. **El original no se toca**: correcciones solo en `web_corregida.html`.
