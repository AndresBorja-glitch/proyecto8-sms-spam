# Bitácora de uso de IA generativa — Proyecto 8 (Clasificación de SMS)

Equipo: Andres Borja, Cristian Londoño, Daniel Florez y Ana Jurado.

Registro del apoyo de herramientas de IA generativa durante el proyecto, como pide la guía del curso. Cada entrada distingue qué hizo la herramienta, qué decidió el equipo y cómo se validó.

> **Completar por el equipo:** agregar las entradas del Corte 1 y del Corte 2 (herramientas usadas, fechas y validación) y revisar las del Corte 3.

| Fecha | Corte | Herramienta / modelo | Propósito | Interacción relevante | Validación realizada | Aporte propio del equipo |
|---|---|---|---|---|---|---|
| [fecha] | 1 | [herramienta] | [p. ej. apoyo en el EDA] | [resumen] | [cómo se comprobó] | [qué decidió o escribió el equipo] |
| [fecha] | 2 | [herramienta] | [p. ej. benchmark y análisis de errores] | [resumen] | [cómo se comprobó] | [qué decidió o escribió el equipo] |
| [fecha] | 2 | Gemini en NotebookLM (marca visible en las diapositivas) | Diseño visual de la presentación del Corte 2 | Generación de diapositivas a partir de los resultados del notebook | Revisión de que cada cifra coincidiera con el notebook | Resultados, decisiones y textos del modelo |
| 2026-11-19 | 3 | Claude (Anthropic), Claude Opus 5.5 | Diseño y código del notebook del Corte 3 | Propuso la profundización (calibración Platt, umbral por costo 5:1, n-gramas de caracteres, embeddings MiniLM como referencia), las pruebas de robustez y la función de inferencia, siguiendo la guía del curso | El código se probó de principio a fin y se corrió en Colab con el dataset real de UCI. Se verificó que la partición coincidiera con el Corte 2 (3.618 / 775 / 776) | [Completar: revisión del código, supuesto de costo 5:1 aceptado o ajustado, interpretación de resultados] |
| 2026-11-19 | 3 | Claude (Anthropic), Claude Opus 5.5 | Presentación final y documentación | Redactó las diapositivas del Corte 3 con guion, la model card, la ficha del dataset, el README y esta bitácora a partir de los resultados del notebook | Las cifras de las diapositivas se tomaron de las salidas del notebook (Corte 2 y Corte 3), sin valores inventados | [Completar: revisión del contenido, ajustes de redacción, preparación de la defensa] |

## Decisiones humanas clave

- Elección del problema y del criterio de éxito: el error más costoso es bloquear un mensaje legítimo (Corte 1).
- Eliminación de duplicados antes de partir y partición estratificada 70/15/15 con semilla 42 (Corte 1).
- Selección del modelo provisional SVM lineal + TF-IDF (1,2), min_df = 2, por F1 de spam en validación (Corte 2).
- [Completar: decisiones del Corte 3 que el equipo tomó o validó.]

## Validaciones realizadas

- Las métricas de las diapositivas se contrastaron con las salidas del notebook.
- El test reservado solo se usó para la evaluación final, sin elegir hiperparámetros con él.
- [Completar.]
