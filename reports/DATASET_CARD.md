# Ficha del dataset — SMS Spam Collection

- **Fuente canónica:** UCI Machine Learning Repository, «SMS Spam Collection», Almeida, T. & Hidalgo, J. (2011). DOI: 10.24432/C5CC84. Licencia CC BY 4.0.
- **Contenido:** SMS en inglés etiquetados como ham o spam. UCI documenta 5.574 mensajes; la lectura del proyecto (pandas, separador tabulador) produce 5.572 filas.
- **Origen de los mensajes:** foro británico Grumbletext (spam), corpus NUS SMS de Singapur (ham), tesis doctoral de Caroline Tag y SMS Spam Corpus v.0.1.
- **Depuración:** se eliminaron 403 textos duplicados exactos (conservando la primera aparición) antes de partir, para evitar fuga entre particiones. No hubo textos con etiquetas contradictorias. Quedan 5.169 mensajes: 4.516 ham y 653 spam (12,6 %).
- **Longitud:** el spam es más largo (media 137,7 caracteres) que el ham (media 70,9).
- **Partición:** estratificada 70/15/15, `random_state=42`: entrenamiento 3.618 (457 spam), validación 775 (98 spam), test 776 (98 spam).
- **Sesgos conocidos:** inglés británico y de Singapur; época 2000–2004; spam centrado en concursos, tonos de celular y números premium; abreviaturas propias de SMS («u», «ur», «txt»).
- **Privacidad:** son mensajes reales publicados para investigación; no se debe intentar re-identificar a las personas.
- **Uso en el proyecto:** entrenamiento, validación y test reservado de un clasificador local y reproducible.
