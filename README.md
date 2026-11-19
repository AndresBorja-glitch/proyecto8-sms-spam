# Proyecto 8 — Clasificación automática de SMS no deseados

**Profundización III · Inteligencia Artificial · Banco de proyectos integradores 2026-II**

Equipo: Andres Borja, Cristian Londoño, Daniel Florez y Ana Jurado

Clasificador de SMS en **ham** (legítimo) o **spam** (no deseado), entrenado y evaluado localmente con el dataset público *SMS Spam Collection* de UCI. El criterio central del proyecto: **bloquear un mensaje legítimo es más grave que dejar pasar un spam**.

## Resultado final (test reservado: 776 mensajes, 98 spam)

| Modelo | Precisión spam | Recall spam | F1 spam | Ham bloqueado (FP) | Spam que pasa (FN) |
|---|---|---|---|---|---|
| Clase mayoritaria (Corte 1) | 0 % | 0 % | 0 % | 0 | 98 |
| Regla por palabras clave (Corte 1) | 75,6 % | 66,3 % | 70,7 % | 21 | 33 |
| TF-IDF (1,1) + Naive Bayes | 100 % | 62,2 % | 76,7 % | 0 | 37 |
| SVM lineal provisional (Corte 2) | 98,9 % | 91,8 % | 95,2 % | 1 | 8 |
| Modelo final, umbral 0,5 | 97,9 % | 94,9 % | 96,4 % | 2 | 5 |
| **Modelo final, umbral 0,58** | **98,9 %** | **94,9 %** | **96,9 %** | **1** | **5** |

**Modelo final:** TF-IDF de palabras (1,2) + n-gramas de caracteres (2,5), SVM lineal calibrado con Platt scaling, umbral 0,58 elegido minimizando `5·FP + 1·FN` sin usar el test. Accuracy 99,2 %, PR-AUC 0,988, Brier 0,0075.

Estos números describen el desempeño **en este dataset**. Con spam actual (smishing de paquetería, bancos, cripto) el modelo detectó 0 de 3 mensajes de prueba: ver `reports/MODEL_CARD.md`.

## Estructura

```
├── README.md
├── AI_USE_LOG.md                 # bitácora de uso de IA generativa
├── requirements.txt
├── data/                         # el notebook descarga aquí el dataset (ver data/README.md)
├── notebooks/
│   └── proyecto_sms_spam_corte3.ipynb   # proyecto completo: datos, modelos, profundización, test, robustez, inferencia y demo
├── src/
│   └── inferencia.py             # clasificar_sms(texto) para mensajes nuevos
├── models/                       # modelo_final_sms.joblib (lo genera el notebook)
└── reports/
    ├── MODEL_CARD.md             # ficha del modelo
    ├── DATASET_CARD.md           # ficha del dataset
    └── resultados_corte3.json    # números usados en la presentación final
```

## Cómo reproducir

1. Abrir `notebooks/proyecto_sms_spam_corte3.ipynb` en Google Colab (Archivo → Subir notebook) o en Jupyter local con `pip install -r requirements.txt`.
2. Ejecutar todas las celdas. El notebook:
   - descarga el dataset desde UCI,
   - elimina duplicados y crea la partición estratificada 70/15/15 (`random_state = 42`): 3.618 / 775 / 776,
   - compara línea base, modelo del Corte 2 y representaciones nuevas en validación,
   - calibra el modelo y elige el umbral con validación cruzada en entrenamiento + validación,
   - evalúa una sola vez en el test reservado,
   - corre las pruebas de robustez y fuera de dominio,
   - guarda el modelo en `models/` y escribe `src/inferencia.py`,
   - genera figuras, la model card, la ficha del dataset y `resultados_corte3.zip`.
3. Tiempo aproximado en Colab: 3 minutos (la comparación con embeddings descarga el modelo MiniLM la primera vez).

## Uso de la función de inferencia

```python
from src.inferencia import clasificar_sms
clasificar_sms("Congratulations! You have won a free prize. Click now to claim.")
# {'etiqueta': 'spam', 'prob_spam': 0.9966, 'umbral': 0.58, 'aviso': '...'}
```

El notebook incluye en la sección 12 una demo interactiva con una caja de texto y un control para mover el umbral.

## Decisiones principales

| Decisión | Evidencia |
|---|---|
| Quitar 403 duplicados exactos antes de partir | Evita que un mismo texto quede en entrenamiento y en prueba |
| Métrica principal: precisión, recall y F1 de spam, no accuracy | La clase mayoritaria tiene 87 % de accuracy y F1 de spam 0 |
| SVM lineal sobre Naive Bayes y regresión logística (Corte 2) | Mejor F1 de spam en validación (92,5 %) |
| Agregar n-gramas de caracteres | PR-AUC en validación de 0,971 a 0,994; más robusto ante «leetspeak» (recall 93,9 % vs. 81,6 %) |
| Embeddings MiniLM solo como referencia | PR-AUC 0,985: no supera al TF-IDF, que además es más simple y explicable |
| Calibrar con Platt scaling | Brier en validación de 0,044 a 0,007 |
| Umbral 0,58 con costo 5:1 | Mismo umbral para costos de 5:1 a 20:1; en test evita el segundo ham bloqueado que da 0,5 |

## Fuente de los datos

Almeida, T. & Hidalgo, J. (2011). *SMS Spam Collection* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5CC84 — Licencia CC BY 4.0.
