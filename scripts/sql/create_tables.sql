/*Creacion de tablas*/

CREATE TABLE IF NOT EXISTS pbs (
    id_pbs INT AUTO_INCREMENT PRIMARY KEY,
    ci_identificacion VARCHAR(255),
    component VARCHAR(255),
    subAssembly VARCHAR(255),
    assemblys VARCHAR(255),
    unit VARCHAR(255),
    modules VARCHAR(255),
    sub_systems VARCHAR(255),
    systems VARCHAR(255),
    acronym VARCHAR(255),
    notes TEXT,
    category VARCHAR(255),
    estado VARCHAR(50),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bom (
    id_bom INT AUTO_INCREMENT PRIMARY KEY,
    componente_id VARCHAR(50),
    nombre_bom VARCHAR(255),
    n_pieza VARCHAR(50),
    unidades INT,
    masa FLOAT,
    material VARCHAR(255),
    component_type VARCHAR(255),
    field_components BOOLEAN,
    status_design VARCHAR(50),
    description TEXT,
    id_institucion_responsable INT,
    lab_tool BOOLEAN,
    id_lab_tool INT,
    supplier VARCHAR(255),
    id_supplier INT,
    id_catalog_reference INT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

