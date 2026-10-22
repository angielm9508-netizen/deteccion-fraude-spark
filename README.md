# Análisis en batch de transacciones financieras y detección de fraude con Apache Spark

Proyecto de la **Tarea 3 – Procesamiento de Datos con Apache Spark** del curso Big Data (código 202016911), Universidad Nacional Abierta y a Distancia (UNAD).

La aplicación `fraude_batch.py` procesa en lote (batch) los registros históricos de transacciones financieras con PySpark. Realiza la carga, la limpieza, la transformación, el análisis exploratorio (EDA) y la identificación de operaciones de alto riesgo.

## Problema
¿Cómo se puede aprovechar el procesamiento distribuido en memoria de Apache Spark para procesar grandes volúmenes de transacciones históricas (Batch), calcular perfiles de usuario y detectar transacciones sospechosas que superen los umbrales de riesgo establecidos?

## Conjunto de datos
* **Nombre:** Credit Card Fraud Detection Dataset
* **Fuente:** Repositorio público de Kaggle
* **Archivo usado:** `creditcard_transactions.csv`
* **Formato:** CSV

El archivo de datos no se incluye en este repositorio por su tamaño. Descárguelo desde la plataforma correspondiente y guárdelo en la misma carpeta que `fraude_batch.py`.

## Requisitos
* Python 3
* Apache Spark 3.5.x con PySpark (probado con Spark 3.5.8, Java 11)
* Bibliotecas de Python: pandas y matplotlib

## Ejecución
```bash
spark-submit fraude_batch.py creditcard_transactions.csv
