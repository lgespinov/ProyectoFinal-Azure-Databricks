# Databricks notebook source

ruta_raw = "abfss://raw@stproyectofinaldbx01.dfs.core.windows.net/"

df_archivos = spark.sql("""
    LIST 'abfss://raw@stproyectofinaldbx01.dfs.core.windows.net/'
""")

display(df_archivos)

# COMMAND ----------

archivos = dbutils.fs.ls(ruta_raw)
display(archivos)

# COMMAND ----------


ruta_base = "abfss://raw@stproyectofinaldbx01.dfs.core.windows.net/"

print("DATASET E-COMMERCE")
display(dbutils.fs.ls(ruta_base + "ecommerce/"))

print("DATASET YOUNG'S MODULUS OF METALS")
display(dbutils.fs.ls(ruta_base + "metals/"))

# COMMAND ----------

# Rutas de los datasets en Azure Data Lake
ruta_base = "abfss://raw@stproyectofinaldbx01.dfs.core.windows.net/"

# Obtener automáticamente el nombre completo de cada CSV
ruta_ecommerce = [
    f.path for f in dbutils.fs.ls(ruta_base + "ecommerce/")
    if f.name.lower().endswith(".csv")
][0]

ruta_metals = ruta_base + "metals/youngs_modulus.csv"

# Lectura de archivos mediante PySpark
df_ecommerce = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(ruta_ecommerce)
)

df_metals = (
    spark.read
    .option("header", "true")
    .option("inferSchema", "true")
    .csv(ruta_metals)
)

# Validar cantidad de registros y columnas
print("E-COMMERCE")
print("Registros:", df_ecommerce.count())
print("Columnas:", len(df_ecommerce.columns))
df_ecommerce.printSchema()
display(df_ecommerce.limit(5))

print("YOUNG'S MODULUS OF METALS")
print("Registros:", df_metals.count())
print("Columnas:", len(df_metals.columns))
df_metals.printSchema()
display(df_metals.limit(5))

# COMMAND ----------

# Corregir lectura del dataset Young's Modulus

df_metals = (
    spark.read
    .option("header", "true")
    .option("sep", ";")
    .option("inferSchema", "true")
    .csv(ruta_metals)
)

# Validar estructura
print("Registros:", df_metals.count())
print("Columnas:", len(df_metals.columns))

df_metals.printSchema()

display(df_metals.limit(10))

# COMMAND ----------

# ==================================================
# CAPA BRONZE - CARGA INICIAL DE DATOS
# ==================================================

from pyspark.sql.functions import current_timestamp, lit

# 1. Preparar datos E-commerce
df_bronze_ecommerce = (
    df_ecommerce
    .withColumn("fecha_carga", current_timestamp())
    .withColumn("fuente", lit("ecommerce"))
)

# 2. Preparar datos Metals
df_bronze_metals = (
    df_metals
    .withColumnRenamed(
        "Young's Modulus (GPa)",
        "Youngs_Modulus_GPa"
    )
    .withColumn("fecha_carga", current_timestamp())
    .withColumn("fuente", lit("metals"))
)

# 3. Guardar E-commerce como tabla Delta
(
    df_bronze_ecommerce.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("proyectofinal_prod.bronze.ecommerce")
)

# 4. Guardar Metals como tabla Delta
(
    df_bronze_metals.write
    .format("delta")
    .mode("overwrite")
    .saveAsTable("proyectofinal_prod.bronze.metals")
)

print("Carga Bronze finalizada correctamente.")

# COMMAND ----------

# Validación de registros en Bronze
spark.sql("""
SELECT 'E-commerce' AS dataset, COUNT(*) AS registros
FROM proyectofinal_prod.bronze.ecommerce
UNION ALL
SELECT 'Metals' AS dataset, COUNT(*) AS registros
FROM proyectofinal_prod.bronze.metals
""").display()
