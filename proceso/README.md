

# Procesamiento ETL - Azure Databricks

Esta carpeta contiene los notebooks PySpark
utilizados en la arquitectura Medallion.

## Bronze
01_Carga_Inicial_Bronze.py
- Ingesta de datasets desde Azure Data Lake.
- Almacenamiento en tablas Delta Bronze.

## Silver
02_Limpieza_Transformacion_Silver.py
- Limpieza y transformación de datos.
- Generación de tablas Delta Silver.

## Gold
03_Procesamiento_Analitico_Gold.py
- Generación de indicadores analíticos.
- Creación de tablas Delta Gold.

## CI/CD
Los notebooks de esta carpeta serán desplegados
y ejecutados en producción mediante GitHub Actions.

Orden de ejecución:
Bronze -> Silver -> Gold
