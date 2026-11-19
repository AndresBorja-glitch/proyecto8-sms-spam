# Model card — Clasificador de SMS ham/spam (Proyecto 8, Corte 3)

## Descripción
- **Tarea:** clasificación binaria de SMS en *ham* (legítimo) o *spam* (no deseado).
- **Modelo:** TF-IDF de palabras (1,2), `min_df=2`, unido a TF-IDF de caracteres `char_wb` (2,5), `min_df=2`, ambos con `sublinear_tf`; SVM lineal calibrado con Platt scaling (`CalibratedClassifierCV`, sigmoide, 5 folds).
- **Decisión:** se marca spam si la probabilidad calibrada es ≥ **0,58**. El umbral minimiza el costo 5·FP + 1·FN sobre predicciones *out-of-fold* de entrenamiento más las de validación (4.393 mensajes), sin usar el test.
- **Entrenamiento final:** entrenamiento + validación (4.393 mensajes). scikit-learn 1.6.1 (Colab).

## Uso previsto
- Apoyo académico y demostrativo para filtrar SMS en **inglés** de estilo parecido al corpus.
- Como **filtro de sugerencia o carpeta de cuarentena** que el usuario puede revisar, no como bloqueo automático definitivo.

## Usos no recomendados
- Bloquear mensajes automáticamente sin posibilidad de revisión.
- Spam moderno (smishing de paquetería, bancos, plataformas, cripto): en la prueba ilustrativa detectó **0 de 3**.
- Mensajes en **español** u otros idiomas: no validado. En la prueba ilustrativa acertó los 3 ham y 2 de 3 spam, pero por rasgos como «www», cifras y «$», no por entender el idioma.
- Decisiones con consecuencias legales, financieras o de seguridad.

## Desempeño en el test reservado (776 mensajes, 98 spam)

| Modelo | Precisión spam | Recall spam | F1 spam | Ham bloqueado (FP) | Spam que pasa (FN) |
|---|---|---|---|---|---|
| Regla por palabras clave (Corte 1) | 0,756 | 0,663 | 0,707 | 21 | 33 |
| SVM provisional (Corte 2) | 0,989 | 0,918 | 0,952 | 1 | 8 |
| **Final, umbral 0,58** | **0,989** | **0,949** | **0,969** | **1** | **5** |

PR-AUC 0,988 · Brier 0,0075 · Accuracy 0,992.
Estos valores describen el desempeño **en este dataset**; en el mundo real se espera un desempeño menor por cambio de idioma, época y estrategias de spam.

## Sensibilidad del umbral al costo (selección, 4.393 mensajes)

| Costo FP : FN | Umbral | FP | FN |
|---|---|---|---|
| 1 : 1 | 0,24 | 12 | 21 |
| 2 : 1 | 0,47 | 3 | 32 |
| 5 : 1 (elegido) | 0,58 | 1 | 40 |
| 10 : 1 y 20 : 1 | 0,58 | 1 | 40 |

## Robustez (recall de spam en el test perturbado)

| Perturbación | SVM Corte 2 | Modelo final |
|---|---|---|
| Original | 0,918 | 0,949 |
| MAYÚSCULAS | 0,918 | 0,949 |
| Leetspeak (FR33, W1N) | 0,816 | 0,939 |
| Palabras con puntos (f.r.e.e) | 0,878 | 0,898 |
| Sin números | 0,888 | 0,898 |

El modelo final mantuvo 1 ham bloqueado en todas las perturbaciones.

## Errores en test
- **1 ham bloqueado** (p = 0,72): notificación de una red social con «FREE SMS», dominio «.COM» e instrucciones de baja.
- **5 spam que pasan** (p entre 0,01 y 0,25): mensajes que imitan una conversación personal o son muy cortos («ringtoneking 84484»).

## Limitaciones y riesgos
- **Idioma:** corpus en inglés (Reino Unido y Singapur).
- **Época y región:** mensajes de aprox. 2000–2004. Varios rasgos de mayor peso son de esa época o país: prefijos 08/09 de números premium, «uk», «£», «ringtone».
- **Cambio de estrategias de spam:** el spam actual usa enlaces, suplantación de marcas y bancos; hay que reentrenar periódicamente con datos recientes y etiquetados.
- **Tamaño:** solo 98 spam en test; un mensaje mueve cerca de 1 punto de recall.
- **Privacidad:** en uso real los SMS son datos personales; no se deben almacenar ni enviar a terceros sin consentimiento.
- **Calibración:** las probabilidades están calibradas para ~12,6 % de spam; si la proporción real cambia, el umbral debe revisarse.

## Condiciones de uso
Solo con SMS en inglés, como sugerencia o cuarentena revisable, citando el dataset y revisando periódicamente los falsos positivos.
