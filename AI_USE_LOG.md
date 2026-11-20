# Bitácora de uso de IA generativa — Proyecto 8

Equipo: Andres Borja, Cristian Londoño, Daniel Florez y Ana Jurado.

Esta bitácora distingue qué hizo cada herramienta de IA, qué decidió el equipo y cómo se comprobó.

## Registro de uso

| Fecha | Corte | Herramienta / modelo | Propósito | Interacción relevante | Validación realizada | Aporte propio del equipo |
|---|---|---|---|---|---|---|
| 2026-09 | 1 | ChatGPT | Entender los entregables del Corte 1 según la guía del Banco de Proyectos (Proyecto 8) | Le pedimos que explicara cada entregable (EDA, partición estratificada, línea base, primer modelo TF-IDF). Después le dimos nuestras respuestas y análisis y le preguntamos si estaban bien o mal, y por qué | Contrastamos sus explicaciones con la guía y corregimos nuestro análisis solo cuando la retroalimentación tenía sentido | Redactamos nuestro propio análisis y decidimos qué correcciones aceptar |
| 2026-09 | 1 | ChatGPT | Plantillas iniciales de código y solución de errores (EDA, partición, línea base) | Cuando no sabíamos cómo hacer algo o salía un error, le pedíamos una plantilla inicial de código o una explicación del error | Ejecutamos el código en Colab y revisamos que los resultados fueran coherentes con los datos | Ajustamos la plantilla, revisamos qué se podía cambiar y la adaptamos a nuestro proyecto |
| 2026-09 | 1 | NotebookLM (Gemini) | Generar las diapositivas del Corte 1 ("Clasificación Automática de Mensajes SMS (HAM vs. SPAM)") | Le dimos nuestros resultados y generó las diapositivas | Revisamos que las cifras y conclusiones coincidieran con el notebook | Definimos el contenido y los resultados presentados |
| 2026-10 | 2 | ChatGPT | Entender los entregables del Corte 2 y validar nuestro análisis del benchmark y de los errores | Le explicamos nuestro análisis y le preguntamos si era correcto y por qué | Contrastamos con la guía y con los resultados del notebook | Redactamos nuestro análisis y decidimos qué correcciones aceptar |
| 2026-10 | 2 | ChatGPT | Plantilla inicial del notebook del Corte 2 (pipeline TF-IDF, benchmark NB/RL/SVM, análisis de errores) y solución de errores | Le pedimos una plantilla inicial del notebook; cuando salían errores que no entendíamos, le pegábamos el mensaje y nos explicaba la causa y una solución | Ejecutamos todas las celdas en Colab hasta que corrieron sin error y revisamos que las métricas y la matriz de confusión fueran coherentes | Ajustamos la plantilla: auditamos duplicados, rehicimos la partición y el benchmark, analizamos los términos que más pesan para spam/ham y guardamos el modelo |
| 2026-10 | 2 | NotebookLM (Gemini) | Generar las diapositivas del Corte 2 ("Clasificación Binaria de SMS: Separando la Señal del Ruido") | Le dimos nuestros resultados y generó las diapositivas | Revisamos las cifras contra el notebook | Definimos el contenido y los resultados presentados |
| 2026-11 | 3 | Claude (Anthropic) | Entender los entregables del Corte 3 y revisar qué nos faltaba según la guía | Le dimos la guía, el notebook y las diapositivas del Corte 2 y le preguntamos qué pedía el Corte 3 y qué nos faltaba | Contrastamos su lista con la tabla de entregables por corte de la guía | Decidimos qué entregar y que todo el proyecto quedara en un solo notebook |
| 2026-11 | 3 | Claude (Anthropic) | Notebook del Corte 3: profundización, evaluación final, robustez e inferencia | Generó el notebook con la profundización (n-gramas de caracteres, calibración Platt, umbral por costo, comparación con embeddings MiniLM), la evaluación en test, las pruebas de robustez, la función `clasificar_sms()` y la demo | Ejecutamos el notebook completo en Colab con el dataset real; verificamos que la partición coincidiera con el Corte 2 (3.618 / 775 / 776) y que el umbral (0,58) y las métricas del test coincidieran con lo que imprime | Aceptamos el supuesto de costo 5:1, revisamos los resultados y la regla para cambiar de representación, y ensayamos la demo en vivo |
| 2026-11 | 3 | Claude (Anthropic) | Diapositivas, documentación y repositorio | Redactó las diapositivas del Corte 3 con guion, la model card, la ficha del dataset y el README a partir de las salidas del notebook; también creó el repositorio en GitHub y subió los archivos a pedido del equipo | Revisamos que cada cifra y cada tabla de las diapositivas coincidieran con la salida del notebook | Nos repartimos las diapositivas, hicimos el guion de exposición y la tabla de preguntas probables, y completamos esta bitácora |

## Revisión del equipo en el Corte 3

- **Notebook:** Ejecutamos el notebook completo en Colab con el dataset real. Comprobamos que el umbral elegido (0,58) y las métricas del test (precisión 98,9 %, recall 94,9 %, F1 96,9 %, 1 de 678 ham bloqueado) coinciden con lo que imprime el notebook.
- **Diapositivas:** Revisamos que cada cifra y cada tabla coincidieran con la salida del notebook y nos repartimos las diapositivas para que cada integrante pudiera explicar su parte.
- **Supuesto de costo 5:1:** Lo aceptamos como supuesto del equipo, porque bloquear un mensaje legítimo puede hacer perder un código de verificación o una cita. La tabla de sensibilidad muestra que de 5:1 a 20:1 el umbral se mantiene en 0,58, así que el supuesto no cambia la decisión.
- **Preparación de la defensa:** Hicimos un guion de exposición de unos 12 minutos con cuatro turnos: Andrés (diapositivas 1–3 y 21), Cristian (4–7), Daniel (8–14) y Ana (15–20). Armamos una tabla de preguntas probables con quién responde cada una y ensayamos la demo en vivo en Colab.

## Decisiones humanas clave

- Corte 1: quitar duplicados exactos antes de partir para evitar fugas entre entrenamiento y prueba.
- Corte 1: definir que bloquear un mensaje legítimo (falso positivo) es más costoso que dejar pasar un spam.
- Corte 2: elegir como modelo provisional el SVM lineal con TF-IDF (1,2) y min_df=2.
- Corte 3: fijar el costo 5·FP + 1·FN como criterio para el umbral.
- Corte 3: fijar, antes de ver resultados, que la representación solo se cambiaba si la PR-AUC subía al menos 0,005.
- Corte 3: descartar los embeddings MiniLM (PR-AUC 0,985 contra 0,994) y dejarlos solo como referencia.
- Corte 3: elegir el umbral sin usar el test y evaluar en test una sola vez.
- Corte 3: limitar el uso a filtro de apoyo con cuarentena revisable y solo para SMS en inglés.

## Validaciones realizadas

- Todo el código generado con apoyo de IA se ejecutó en Google Colab con el dataset real antes de usar sus resultados.
- Las explicaciones de la IA se contrastaron con la guía del Banco de Proyectos.
- Las cifras de todas las diapositivas se contrastaron con la salida del notebook.
- El test se mantuvo reservado hasta la evaluación final.
- Se hizo una tabla de sensibilidad del umbral al costo (de 1:1 a 20:1).
- Se probó la robustez con el test reescrito (mayúsculas, leetspeak, palabras partidas) y con mensajes escritos por el equipo.
