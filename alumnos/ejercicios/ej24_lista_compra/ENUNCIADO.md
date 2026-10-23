# 🟢 EJ 24 · Lista de la compra a partir de recetas

> 🗂️ **Documentos y tareas repetitivas** · 🟢 Fácil · ⏱ 10 min · 🛠️ opencode interactivo · Recomendado para: 🧭

> ✋ **Práctica**: lo haces tú, a tu ritmo. Si te atascas, pregunta al profesor.

## 📌 La situación

Cena para seis con tres recetas pensadas para cuatro y media despensa llena. Hace falta la lista de la compra por secciones.

## 🎯 Objetivo

Escalar recetas, descontar lo que ya hay y agrupar la compra. Y comprobar las cuentas.

## 📦 Lo que tienes en esta carpeta

- `recetas/`: tres recetas para 4 personas.
- `despensa.txt`: lo que ya hay en casa.

## 💬 El encargo

**1.** Abre opencode en modo interactivo en tu carpeta de trabajo:

```bash
python taller.py abrir ej24
```

**2.** Copia este encargo, pégalo en opencode y pulsa Enter:

```text
Quiero cocinar las tres recetas de recetas/ para 6 personas (las recetas son para 4). Escribe lista_compra.md con las cantidades multiplicadas por 1,5 y agrupadas por sección del súper (verdura, lácteos, frutos secos…). No pongas lo que ya tengo según despensa.txt; añade al final una sección Ya lo tienes en casa con eso.
```

**3.** Mira lo que hace: qué ficheros lee, qué órdenes ejecuta, si te pide permiso. Cuando termine, sal con `Ctrl+C` (o sigue conversando: «revisa que…», «corrige…»).

<details><summary>Sin conversar, de una vez (opcional)</summary>

```bash
python taller.py lanzar ej24
```

O a mano, desde la carpeta de trabajo: `opencode run --standalone "…el encargo…"`.

</details>

> 💡 Antes de pegarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `lista_compra.md` con 1,2 kg de pochas, 12 alcachofas, 600 g de guisantes, 1,5 l de leche de oveja…
- Sin aceite, sal, harina, miel ni huevos en la lista (están en la despensa: hacen falta 3 huevos y hay 6).

```bash
python taller.py comprobar ej24      # el agente no decide si está bien: lo decide el comprobador
```

## 📂 Una solución de ejemplo

¿Te has atascado o no puedes ejecutarlo? Mira lo que hizo el agente con este encargo (el encargo, lo que escribió en pantalla y los ficheros): [`soluciones/ej24_lista_compra/`](../../soluciones/ej24_lista_compra/)

## 🔀 Siguiente paso

- **Entender una carta de la Administración** → [🟢 EJ 25 · Entender una carta de la Administración](../ej25_carta_explicada/ENUNCIADO.md)
- **La carpeta de Descargas** → [🟢 EJ 15 · Ordenar la carpeta de Descargas](../ej15_ordenar_descargas/ENUNCIADO.md)
- **Volver al inicio** → [↩️ Inicio: todas las áreas](../../ITINERARIOS.md#-áreas-y-ejercicios)
