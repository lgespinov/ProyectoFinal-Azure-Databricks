# Databricks notebook source
# ==================================================
# CAPA SILVER - LIMPIEZA Y TRANSFORMACIÓN DE DATOS
# ==================================================

from pyspark.sql import functions as F
from pyspark.sql.types import *

# 1. Leer tablas de la capa Bronze
df_ecommerce = spark.table(
    "proyectofinal_dev.bronze.ecommerce"
)

df_metals = spark.table(
    "proyectofinal_dev.bronze.metals"
)

# 2. Validar cantidad de registros
print("=== DATASET E-COMMERCE ===")
print("Registros:", df_ecommerce.count())
print("Columnas:", len(df_ecommerce.columns))
df_ecommerce.printSchema()

print("\n=== DATASET METALS ===")
print("Registros:", df_metals.count())
print("Columnas:", len(df_metals.columns))
df_metals.printSchema()

# COMMAND ----------

from pyspark.sql import functions as F

# ==========================================
# 1. LIMPIEZA DATASET E-COMMERCE
# ==========================================

df_silver_ecommerce = (
    df_ecommerce
    .dropDuplicates()
    .dropna(subset=[
        "Date",
        "Product_Category",
        "Price",
        "Units_Sold"
    ])
    .select(
        F.col("Date").alias("fecha"),
        F.col("Product_Category").alias("categoria_producto"),
        F.col("Price").alias("precio"),
        F.col("Discount").alias("descuento"),
        F.col("Customer_Segment").alias("segmento_cliente"),
        F.col("Marketing_Spend").alias("gasto_marketing"),
        F.col("Units_Sold").alias("unidades_vendidas"),
        F.col("fecha_carga"),
        F.col("fuente")
    )
    .withColumn(
        "categoria_producto",
        F.trim(F.col("categoria_producto"))
    )
    .withColumn(
        "segmento_cliente",
        F.trim(F.col("segmento_cliente"))
    )
    .withColumn(
        "importe_venta",
        F.round(
            F.col("precio") * F.col("unidades_vendidas"), 2
        )
    )
)

# ==========================================
# 2. LIMPIEZA DATASET METALS
# ==========================================

df_silver_metals = (
    df_metals
    .dropDuplicates()
    .dropna(subset=[
        "Metal",
        "Symbol",
        "Youngs_Modulus_GPa"
    ])
    .select(
        F.col("Metal").alias("metal"),
        F.col("Symbol").alias("simbolo"),
        F.col("Youngs_Modulus_GPa").alias("modulo_young_gpa"),
        F.col("fecha_carga"),
        F.col("fuente")
    )
    .withColumn(
        "metal",
        F.trim(F.col("metal"))
    )
    .withColumn(
        "simbolo",
        F.trim(F.col("simbolo"))
    )
)
 
 

display(df_silver_ecommerce.limit(5))
display(df_silver_metals.limit(5))

# COMMAND ----------

 

# 1. Guardar E-commerce
(
    df_silver_ecommerce.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("proyectofinal_dev.silver.ecommerce")
)

print("Tabla Silver E-commerce creada correctamente.")

# 2. Guardar Metals
(
    df_silver_metals.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("proyectofinal_dev.silver.metals")
)

print("Tabla Silver Metals creada correctamente.")

# COMMAND ----------

#validaciones

spark.sql("""
SELECT 'E-commerce' AS dataset, COUNT(*) AS registros
FROM proyectofinal_dev.silver.ecommerce

UNION ALL

SELECT 'Metals' AS dataset, COUNT(*) AS registros
FROM proyectofinal_dev.silver.metals
""").display()