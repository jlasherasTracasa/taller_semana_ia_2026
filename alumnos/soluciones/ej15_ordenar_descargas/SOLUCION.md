# Solución · Ordenar carpeta de descargas

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Organiza descargas/: crea subcarpetas facturas/, fotos/, \
  hojas_calculo/, documentos/, imagenes/ y mueve cada archivo según su tipo sin borrar nada. \
  Luego muéstrame el árbol resultante."
```

## Resultado
Los 11 archivos repartidos en facturas/, fotos/, hojas_calculo/, documentos/ e imagenes/; árbol final en `resultado_arbol/` (ninguno perdido ni renombrado).

## Salida real (extracto validado 2026-09-28)
```
Árbol real final mostrado por el agente tras opencode run (validado 2026-09-28) —
11 archivos movidos, ninguno perdido:
descargas/documentos/contrato_alquiler_2025.pdf
descargas/documentos/cv_actualizado.docx
descargas/documentos/receta_tarta_santiago.pdf
descargas/documentos/temario_oposiciones.pdf
descargas/facturas/factura_enero_2026.pdf
descargas/fotos/foto_cumple_mama.jpg
descargas/fotos/foto_playa_001.jpg
descargas/fotos/foto_sierra_002.jpg
descargas/hojas_calculo/lista_clientes_final.xlsx
descargas/hojas_calculo/resumen_gastos_agosto.xlsx
descargas/imagenes/logo_evento.png
```

Los artefactos generados (archivos de resultado) están en esta misma carpeta.
