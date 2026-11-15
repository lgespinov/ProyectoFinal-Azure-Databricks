
  -- Deesarrollo de un ambiente simple
CREATE CATALOG IF NOT EXISTS proyectofinal_dev;

-- Esquemas de procesamiento
CREATE SCHEMA IF NOT EXISTS proyectofinal_dev.bronze;

CREATE SCHEMA IF NOT EXISTS proyectofinal_dev.silver;

CREATE SCHEMA IF NOT EXISTS proyectofinal_dev.gold;

-- Verificacion
SHOW SCHEMAS IN proyectofinal_dev;
