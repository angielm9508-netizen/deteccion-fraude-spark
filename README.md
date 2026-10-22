# Análisis de Transacciones Financieras y Detección de Fraude con Apache Spark

Proyecto de la **Tarea 3 – Procesamiento de Datos con Apache Spark** del curso Big Data, Universidad Nacional Abierta y a Distancia (UNAD).

La aplicación `fraude_batch.py` procesa en lote (batch) los registros de transacciones financieras. Realiza la carga de datos, la limpieza, la transformación, el análisis exploratorio y la detección de transacciones sospechosas por encima de un umbral de riesgo.

## Problema
¿Cómo se puede aprovechar el procesamiento distribuido en memoria de Apache Spark para analizar volúmenes masivos de transacciones históricas e identificar patrones de comportamiento anómalos o sospechosos?

## Conjunto de datos
* **Nombre:** Credit Card Fraud Detection Dataset
* **Fuente:** Kaggle
* **Formato:** CSV (`creditcard_transactions.csv`)

## Archivos del repositorio
* `fraude_batch.py`: Código principal de procesamiento batch en PySpark.
