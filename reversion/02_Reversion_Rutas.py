
# Databricks notebook source
# =====================================================
# REVERSION DE RUTAS FISICAS - AZURE DATABRICKS
# Modo seguro: solo inspeccion
# =====================================================

catalogo = "proyectofinal_dev"

tablas = [
    "bronze.ecommerce",
    "bronze.metals",
    "silver.ecommerce",
    "silver.metals",
    "gold.indicadores_ecommerce",
    "gold.indicadores_metals"
]

for tabla in tablas:
    nombre = f"{catalogo}.{tabla}"

    try:
        detalle = spark.sql(
            f"DESCRIBE DETAIL {nombre}"
        ).first()

        print(f"Tabla: {nombre}")
        print(f"Ruta: {detalle['location']}")
        print(f"Formato: {detalle['format']}")
        print("-" * 60)

    except Exception as e:
        print(f"No se pudo inspeccionar {nombre}: {e}")

# IMPORTANTE:
# No se eliminan rutas automaticamente.
# Las rutas externas requieren validacion
# y autorizacion antes de su eliminacion.
