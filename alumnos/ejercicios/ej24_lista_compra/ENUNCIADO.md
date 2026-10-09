# 🟢 EJ 24 · La cena de las fiestas

> 🗂️ **Puerta D · El ayuntamiento** · 🟢 Fácil · ⏱ 10 min · 🛠️ `opencode run` · Recomendado para: 🧭

## 📖 La escena

Seis a cenar, tres recetas para cuatro y media despensa llena. Pilar quiere la lista de la compra por secciones.

## 🎯 Objetivo

Escalar recetas, descontar lo que ya hay y agrupar la compra. Y comprobar las cuentas.

## 📦 Lo que tienes en esta carpeta

- `recetas/`: tres recetas para 4 personas.
- `despensa.txt`: lo que ya hay en casa.

## 💬 El encargo

Con el mando del taller (prepara la carpeta, carga tu `.env` y guarda la salida):

```bash
python3 taller.py lanzar ej24
```

O a mano, desde la carpeta de trabajo del ejercicio:

```bash
opencode run --standalone "Quiero cocinar las tres recetas de recetas/ para 6 personas (las recetas son para 4). Escribe lista_compra.md con las cantidades multiplicadas por 1,5 y agrupadas por sección del súper (verdura, lácteos, frutos secos…). No pongas lo que ya tengo según despensa.txt; añade al final una sección Ya lo tienes en casa con eso." | tee salida.txt
```

> 💡 Antes de lanzarlo, léelo buscando las cinco piezas de un buen encargo: **contexto, objetivo, entrega, límites y criterio**. ¿Falta alguna? Prueba a quitarla y mira qué pasa.

## ✅ ¿Lo ha hecho de verdad?

- `lista_compra.md` con 1,2 kg de pochas, 12 alcachofas, 600 g de guisantes, 1,5 l de leche de oveja…
- Sin aceite, sal, harina, miel ni huevos en la lista (están en la despensa: hacen falta 3 huevos y hay 6).

```bash
python3 taller.py comprobar ej24      # el agente no puede darte el sello: solo el comprobador
```

## 🔀 ¿Y ahora qué?

- **Explícame esta carta** → [🟢 EJ 25 · Explícame esta carta](../ej25_carta_explicada/ENUNCIADO.md)
- **La carpeta de Descargas** → [🟢 EJ 15 · La carpeta de Descargas](../ej15_ordenar_descargas/ENUNCIADO.md)
- **Volver a la plaza** → [↩️ La plaza](../../AVENTURA.md#-la-plaza)
