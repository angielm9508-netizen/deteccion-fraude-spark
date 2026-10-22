# Análisis en batch de transacciones financieras y detección de fraude con Apache Spark

Proyecto de la **Tarea 3 – Procesamiento de Datos con Apache Spark** del curso Big Data (código 202016911), Universidad Nacional Abierta y a Distancia (UNAD).

La aplicación `fraude_batch.py` procesa en lote (batch) los registros históricos de transacciones financieras con PySpark. Realiza la carga, la limpieza, la transformación, el análisis exploratorio (EDA) y la identificación de operaciones de alto riesgo.

## Problema
¿Cómo se puede aprovechar el procesamiento distribuido en memoria de Apache Spark para procesar grandes volúmenes de transacciones históricas (Batch), calcular perfiles y detectar transacciones sospechosas que superen los umbrales de riesgo establecidos?

## Conjunto de datos
* **Nombre:** Credit Card Fraud Detection (o conjuntos de datos equivalentes de transacciones financieras)
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
spark-submit fraude_batch.py creditcard_transactions.csv 500.00

Argumentos:

    Ruta del archivo CSV de transacciones.

    Umbral de monto en USD para la detección de riesgo.

Si no se indican argumentos, el programa usa los valores por defecto establecidos en el script.

Qué hace el código

    Carga: Lee el archivo CSV de transacciones en un DataFrame de PySpark, mostrando el esquema inicial y el número de registros totales.

    Limpieza: Elimina registros con valores nulos en columnas críticas (como Amount y Time) y filtra montos negativos o no válidos.

    Transformación: Estructura y procesa las variables numéricas y temporales para optimizar el análisis de los datos.

    Análisis exploratorio: Calcula estadísticas descriptivas, agrupa los registros según el estado de la transacción (Class: 0 para legítimas, 1 para fraudulentas) y obtiene los montos promedio.

    Detección de riesgo: Aplica reglas condicionales basadas en umbrales de alto riesgo para identificar, clasificar y contabilizar operaciones sospechosas.

Salida

Las tablas de resultados analíticos y resúmenes de transacciones se muestran directamente en la consola de manera estructurada:

    Distribución por Estado (Class): Total de transacciones y monto promedio por categoría legítima vs. fraudulenta.

    Resumen de Alto Riesgo: Conteo de transacciones que superan el umbral crítico establecido.

Resultados principales

    Procesamiento Masivo: Capacidad de gestionar cientos de miles o millones de registros históricos superando las limitaciones de los sistemas tradicionales.

    Segmentación Eficiente: Identificación rápida de patrones de comportamiento anómalos y transacciones con montos elevados que requieren auditoría o alerta temprana.

Limitaciones

    La precisión del análisis depende de la calidad y anonimización previa de las variables del dataset (como las transformaciones PCA aplicadas).

    El procesamiento batch se enfoca exclusivamente en el análisis histórico; para la detección en tiempo real se complementa con arquitecturas de Streaming (como Apache Kafka).

Autora

Estudiante UNAD – Tutor: Angie Johanna Laguna Martinez – UNAD, 2026.
