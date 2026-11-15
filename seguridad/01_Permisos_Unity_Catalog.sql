
-- =====================================================
-- SEGURIDAD - PROYECTO FINAL AZURE DATABRICKS
-- Unity Catalog - Arquitectura Medallion
-- =====================================================

-- ACCESO AL CATALOGO
GRANT USE CATALOG ON CATALOG proyectofinal_dev
TO `grp_ingenieria_datos`;

GRANT USE CATALOG ON CATALOG proyectofinal_dev
TO `grp_consulta_gold`;

-- BRONZE: INGENIERIA DE DATOS
GRANT USE SCHEMA ON SCHEMA proyectofinal_dev.bronze
TO `grp_ingenieria_datos`;

GRANT SELECT ON SCHEMA proyectofinal_dev.bronze
TO `grp_ingenieria_datos`;

-- SILVER: INGENIERIA DE DATOS
GRANT USE SCHEMA ON SCHEMA proyectofinal_dev.silver
TO `grp_ingenieria_datos`;

GRANT SELECT ON SCHEMA proyectofinal_dev.silver
TO `grp_ingenieria_datos`;

-- GOLD: CONSULTA ANALITICA
GRANT USE SCHEMA ON SCHEMA proyectofinal_dev.gold
TO `grp_consulta_gold`;

GRANT SELECT ON SCHEMA proyectofinal_dev.gold
TO `grp_consulta_gold`;

-- GOLD: INGENIERIA DE DATOS
GRANT USE SCHEMA ON SCHEMA proyectofinal_dev.gold
TO `grp_ingenieria_datos`;

GRANT SELECT ON SCHEMA proyectofinal_dev.gold
TO `grp_ingenieria_datos`;

-- VERIFICACION
SHOW GRANTS ON CATALOG proyectofinal_dev;
SHOW GRANTS ON SCHEMA proyectofinal_dev.bronze;
SHOW GRANTS ON SCHEMA proyectofinal_dev.silver;
SHOW GRANTS ON SCHEMA proyectofinal_dev.gold;
