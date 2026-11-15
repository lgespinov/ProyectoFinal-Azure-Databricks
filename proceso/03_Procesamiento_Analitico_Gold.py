# Databricks notebook source
from pyspark.sql import functions as F

# ==========================================
# 1. LEER TABLAS DE LA CAPA SILVER
# ==========================================

df_ecommerce = spark.table(
    "proyectofinal_dev.silver.ecommerce"
)

df_metals = spark.table(
    "proyectofinal_dev.silver.metals"
)

# ==========================================
# 2. INDICADORES ANALÍTICOS E-COMMERCE
# ==========================================

df_gold_ecommerce = (
    df_ecommerce
    .groupBy("categoria_producto")
    .agg(
        F.count("*").alias("total_registros"),
        F.sum("unidades_vendidas").alias("total_unidades"),
        F.round(
            F.sum("importe_venta"), 2
        ).alias("total_ventas"),
        F.round(
            F.avg("precio"), 2
        ).alias("precio_promedio"),
        F.round(
            F.avg("descuento"), 2
        ).alias("descuento_promedio"),
        F.round(
            F.sum("gasto_marketing"), 2
        ).alias("total_gasto_marketing")
    )
)

# ==========================================
# 3. Indicadores claves 
# ==========================================

df_gold_metals = (
    df_metals
    .select(
        "metal",
        "simbolo",
        "modulo_young_gpa"
    )
    .withColumn(
        "clasificacion_rigidez",
        F.when(
            F.col("modulo_young_gpa") < 50,
            "Baja"
        )
        .when(
            F.col("modulo_young_gpa") < 150,
            "Media"
        )
        .otherwise("Alta")
    )
)

# ==========================================
# 4. VALIDACIÓN DE RESULTADOS
# ==========================================

print("=== INDICADORES E-COMMERCE ===")
display(df_gold_ecommerce)

print("=== INDICADORES METALS ===")
display(df_gold_metals.limit(10))

# COMMAND ----------

# ==========================================
# GUARDAR DATASETS EN CAPA GOLD
# ==========================================

# 1. Guardar indicadores E-commerce
(
    df_gold_ecommerce.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("proyectofinal_dev.gold.indicadores_ecommerce")
)

print("Tabla Gold E-commerce creada correctamente.")

# 2. Guardar indicadores Metals
(
    df_gold_metals.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .saveAsTable("proyectofinal_dev.gold.indicadores_metals")
)

print("Tabla Gold Metals creada correctamente.")

# COMMAND ----------

# ==========================================
# VALIDACIÓN DE TABLAS GOLD
# ==========================================

spark.sql("""
SELECT 'E-commerce' AS dataset, COUNT(*) AS registros
FROM proyectofinal_dev.gold.indicadores_ecommerce

UNION ALL

SELECT 'Metals' AS dataset, COUNT(*) AS registros
FROM proyectofinal_dev.gold.indicadores_metals
""").display()