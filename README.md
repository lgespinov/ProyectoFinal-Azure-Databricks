# Proyecto Final – Azure Databricks

## 1. Descripción del proyecto

Implementación de una solución de ingeniería de datos en Microsoft Azure y Azure Databricks, utilizando arquitectura Medallion (Bronze, Silver y Gold), procesamiento distribuido con PySpark, gobierno de datos mediante Unity Catalog y automatización de despliegues mediante GitHub Actions.

El proyecto procesa dos datasets: E-commerce Sales Prediction y Young's Modulus of Metals.

## 2. Arquitectura de la solución

- **Azure Data Lake Storage Gen2:** almacenamiento de archivos de origen.
- **Azure Databricks:** procesamiento y transformación de datos con PySpark.
- **Unity Catalog:** administración de catálogos, esquemas y permisos.
- **Arquitectura Medallion:** capas Bronze, Silver y Gold.
- **Databricks Jobs:** ejecución secuencial de los notebooks.
- **GitHub Actions:** despliegue automatizado de notebooks mediante CI/CD.
- **AI/BI Dashboards:** visualización de indicadores analíticos.

## 3. Entornos de trabajo

| Entorno | Catálogo |
|---|---|
| Desarrollo | `proyectofinal_dev` |
| Producción | `proyectofinal_prod` |

Ambos entornos utilizan los esquemas `bronze`, `silver` y `gold`.

## 4. Procesamiento de datos

| Capa | Notebook | Funcionalidad |
|---|---|---|
| Bronze | `01_Carga_Inicial_Bronze.py` | Ingesta de archivos CSV y almacenamiento en tablas Delta |
| Silver | `02_Limpieza_Transformacion_Silver.py` | Limpieza, normalización y transformación de datos |
| Gold | `03_Procesamiento_Analitico_Gold.py` | Generación de indicadores analíticos |

## 5. Automatización CI/CD

El repositorio implementa GitHub Actions mediante el workflow:

`.github/workflows/deploy_databricks.yml`

Este workflow permite desplegar los notebooks hacia el entorno de producción de Azure Databricks.

Las credenciales se administran mediante GitHub Secrets, evitando almacenarlas directamente en el código.

## 6. Orquestación de procesos

El Job `JOB_Procesamiento_Medallion_ProyectoFinal` ejecuta secuencialmente las tres tareas:

**Bronze → Silver → Gold**

Se verificó la ejecución satisfactoria del procesamiento en producción.

## 7. Dashboard analítico

Se implementó el dashboard **Dashboard Analítico – E-commerce y Metales**, que presenta:


## 8. Estructura del repositorio

- `.github/`: automatización CI/CD.
- `PrepAmb/`: preparación del ambiente.
- `certificaciones/`: documentación de certificaciones.
- `datasets/`: información de datasets.
- `proceso/`: notebooks de procesamiento.
- `seguridad/`: scripts de permisos.
- `reversion/`: procedimientos de reversión.
- `dashboard/`: documentación del dashboard.
- `evidencias/`: capturas de implementación y ejecución.

## 9. Evidencias

Las capturas de los recursos, catálogos, ejecuciones y resultados se encuentran en la carpeta [evidencias](evidencias/).

