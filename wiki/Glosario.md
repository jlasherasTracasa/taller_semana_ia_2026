# 📖 Glosario

| Palabra | En una frase |
|---|---|
| **Agente** | Un modelo de lenguaje con herramientas, un bucle y permisos, que persigue un objetivo. |
| **LLM** | Modelo de lenguaje grande: predice texto. Aquí, GLM-5.3-Flash. |
| **Prompt / encargo** | Lo que le pides. Mejor con contexto, objetivo, entrega, límites y criterio. |
| **ReAct** | Patrón *Reason + Act*: pensar, actuar, observar… en bucle. |
| **Tool (herramienta)** | Función que el modelo puede **pedir**; la ejecuta el programa. |
| **Function calling** | La forma en que el modelo pide una tool: un JSON con nombre y argumentos. |
| **opencode** | El agente que usamos: libre, en la terminal, con cualquier modelo. |
| **`opencode run`** | Modo no interactivo: un encargo y listo. |
| **Modo interactivo** | `opencode` a secas: conversas y apruebas permisos. |
| **AGENTS.md** | Normas permanentes de un proyecto que el agente lee siempre. |
| **Comando** | Encargo guardado que invocas con `/nombre`. |
| **Skill** | Receta (instrucciones + scripts) que el agente carga cuando la necesita. |
| **MCP** | *Model Context Protocol*: estándar para enchufar servidores de tools a cualquier agente. |
| **Subagente** | Agente al que el principal delega una parte, con sus propios permisos. |
| **Permiso** | `allow` (hazlo), `ask` (pregúntame), `deny` (prohibido). |
| **Inyección de prompt** | Órdenes escondidas en algo que el agente lee. |
| **Contexto** | Todo lo que el modelo ve en cada paso: instrucciones, historial, ficheros leídos. |
| **Token** | Trozo de texto (≈ ¾ de palabra) por el que se paga. |
| **pass^k** | Probabilidad de que salga bien k veces seguidas. |
| **Comprobador** | `comprobar.py`: verifica el criterio de éxito sin fiarse del agente. |
| **Completado** | Lo que dice el comprobador cuando todo está bien (no lo decide el agente). |
