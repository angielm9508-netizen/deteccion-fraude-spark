from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, when

# 1. Inicializar la sesión de Spark
spark = SparkSession.builder \
    .appName("Batch-DeteccionDeFraudeFinanciero") \
    .getOrCreate()

print("--- 1. CARGA DEL CONJUNTO DE DATOS ---")
file_path = "creditcard_transactions.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(file_path)

print("--- 2. LIMPIEZA Y TRANSFORMACIÓN DE DATOS ---")
df_cleaned = df.dropna(subset=["Amount", "Time"]).filter(col("Amount") >= 0)

print("--- 3. ANÁLISIS EXPLORATORIO ---")
analisis_fraude = df_cleaned.groupBy("Class").agg(
    count("*").alias("total_transacciones"),
    avg("Amount").alias("monto_promedio")
)
analisis_fraude.show(truncate=False)

print("--- 4. DETECCIÓN DE TRANSACCIONES SOSPECHOSAS ---")
df_sospechosas = df_cleaned.withColumn(
    "es_sospechosa", 
    when(col("Amount") > 500.0, 1).otherwise(0)
)
df_sospechosas.groupBy("es_sospechosa").count().show(truncate=False)

spark.stop()
