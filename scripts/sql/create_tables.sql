/*Creacion de tablas*/
CREATE TABLE IF NOT EXISTS pbs (
    pbs_ci_identification VARCHAR(255) PRIMARY KEY,
    pbs_level INT,
    pbs_component VARCHAR(255),
    pbs_subassembly VARCHAR(255),
    pbs_assemblys VARCHAR(255),
    pbs_unit VARCHAR(255),
    pbs_modules VARCHAR(255),
    pbs_subsystems VARCHAR(255),
    pbs_systems VARCHAR(255),
    item_name VARCHAR(255),
    acronym VARCHAR(255),
    component_active BOOLEAN,
    component_type VARCHAR(255),
    component_status VARCHAR(255),
    component_description TEXT,
    component_field BOOLEAN,
    institution VARCHAR(255),
    lab_tool VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bom (
    id_bom INT AUTO_INCREMENT PRIMARY KEY,
    mass DECIMAL(10,2),
    material VARCHAR(255),
    treatment VARCHAR(255),
    coating VARCHAR(255),
    step_link VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    pbs_ci_identification VARCHAR(255),
    FOREIGN KEY (pbs_ci_identification) REFERENCES pbs(pbs_ci_identification)
);