/*Creacion de tablas*/
CREATE TABLE IF NOT EXISTS pbs (
    pbs_id INT AUTO_INCREMENT PRIMARY KEY,
    pbs_ci_identification VARCHAR(255),
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
    lab_tool BOOLEAN,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bom (
    id_bom INT AUTO_INCREMENT PRIMARY KEY,
    mass INT,
    material VARCHAR(255),
    treatment VARCHAR(255),
    coating VARCHAR(255),
    step_link VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    pbs_id INT,
    FOREIGN KEY (pbs_id) REFERENCES pbs(pbs_id)
);