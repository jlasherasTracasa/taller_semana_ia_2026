# Solución · EJ 14 · Traducir un deck conservando el formato

## Prompt exacto usado
```bash
$ opencode run --model vllm/GLM-5.3-Flash "Traduce charla_taller_es.pptx al inglés editando el XML directamente (unzip → edita slideN.xml → zip). Usa defusedxml.minidom, no xml.etree. Entrega charla_taller_en.pptx. No alteres imágenes, tablas ni gráficos."
```

## Resultado
`charla_taller_en.pptx`: solo se tradujeron los `<a:t>` de slide1–4.xml con `defusedxml.minidom`, preservando estructura y namespaces; repackeado y validado (PASSED).

## Salida real (extracto validado 2026-09-28)
```
Listo: charla_taller_en.pptx
- Traduje solo los <a:t> de slide1–4.xml con un script que usa defusedxml.minidom
  (nada de xml.etree), preservando estructura y namespaces.
- Repackeado con zipfile (zip no está instalado) y validado con validate.py
  --original: PASSED. Texto verificado con markitdown.
```

El artefacto generado está en esta misma carpeta.
