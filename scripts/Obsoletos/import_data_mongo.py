import os
import sys
import pymongo
import pandas as pd
from pymongo import MongoClient

# Asume que el script se ejecuta desde el directorio raíz del proyecto
project_root = 'C:/Users/HARMONI/Documents/HARMONI/HRM_BBDD'
sys.path.append(project_root)

# Importar configuraciones desde el módulo config
from config.config import MONGODB_URI, MONGODB_DB_NAME, MONGODB_COLLECTION_NAME, MONGODB_URI_local
from config.config import DB_CONFIG, DATA_FILE_PATH

# Ruta al archivo CSV
csv_file = os.path.join(DATA_FILE_PATH, 'EjemploBOM_completo.csv')

# Leer el archivo CSV
df = pd.read_csv(csv_file, sep=';', encoding='latin1')

# Mapeo de las columnas del CSV a las variables de MongoDB
mapeo = {
    # pbs
    'pbs_number' : 'pbs.ci_identification',
    'pbs_name' : 'pbs.name',
    'pbs_acronym': 'pbs.acronym',
    'pbs_level': 'pbs.level',
    'pbs_system': 'pbs.structure.system',
    'pbs_subsystem': 'pbs.structure.subsystem',
    'pbs_module': 'pbs.structure.module',
    'pbs_unit': 'pbs.structure.unit',
    'pbs_assembly': 'pbs.structure.assembly',
    'pbs_subassembly': 'pbs.structure.subassembly',
    'pbs_component': 'pbs.structure.component',

    # component
    'pbs_is_component': 'component.is_component',
    'component_status': 'component.status',
    'component_description': 'component.description',
    'component_type': 'component.type',
    'component_field': 'component.field',

    # procurement
    'procurement_supplier': 'procurement.supplier',
    'procurement_manufacturer': 'procurement.manufacturer',
    'manufacturer_part_number': 'procurement.part_number',
    'procurement_catalog_reference': 'procurement.catalog_reference',
    'procurement_cost_unit': 'procurement.cost_unit',
    'procurement_cost_status': 'procurement.cost_status',
    'procurement_quantity': 'procurement.quantity',

    # mechanical
    'mechanical_mass': 'mechanical.mass',
    'mechanical_material': 'mechanical.material',
    'mechanical_treatment': 'mechanical.treatment',
    'mechanical_coating': 'mechanical.coating',
    'mechanical_step_link': 'mechanical.step_link',

    # electrical
    'electrical_power_budget': 'electrical.electrical_power_budget',
    'electrical_current_ps_only': 'electrical.current_ps_only',
    'electrical_voltaje_dc': 'electrical.voltaje_dc',
    'electrical_voltaje_ac': 'electrical.voltaje_ac',
    'electrical_initialization_power': 'electrical.initialization.power',
    'electrical_initialization_current': 'electrical.initialization.current',
    'electrical_standby_power': 'electrical.standby.power',
    'electrical_standby_standby': 'electrical.standby.standby',
    'electrical_calibration_power': 'electrical.calibration.power',
    'electrical_calibration_current': 'electrical.calibration.current',
    'electrical_observation_power': 'electrical.observation.power',
    'electrical_observation_current': 'electrical.observation.current',
    'electrical_maintenance_power': 'electrical.maintenance.power',
    'electrical_maintenance_current': 'electrical.maintenance.current',
    'electrical_ups_power_required': 'electrical.ups_power.required',
    'electrical_ups_power_time_required_ups': 'electrical.ups_power.time_required_ups',

    # thermical
    'thermical_heat_dissipated': 'thermical.heat_dissipated',
    'thermical_head_load_to_air': 'thermical.head_load_to_air',
    'thermical_head_load_to_coolant': 'thermical.head_load_to_coolant',
    'thermical_skin_temperature_above_ambient': 'thermical.skin_temperature_above_ambient',
    'thermical_requires_cooling': 'thermical.requires_cooling',

    # cables
    'cables_function': 'cables.function',
    'cables_max_length': 'cables.max_length',
    'cables_length': 'cables.length',
    'cables_outer_diameter': 'cables.outer_diameter',
    'cables_min_bending_radius_dynamic': 'cables.min_bending_radius_dynamic',
    'cables_min_bending_radius_static': 'cables.min_bending_radius_static',
    'cables_mass_density': 'cables.mass_density'
}

# Convertir el DataFrame de pandas a una lista de diccionarios con las claves mapeadas
datos = []
for _, row in df.iterrows():
    documento = {}
    for csv_columna, mongo_variable in mapeo.items():
        # Dividir las variables anidadas por puntos
        keys = mongo_variable.split('.')
        d = documento
        for key in keys[:-1]:
            d = d.setdefault(key, {})
        d[keys[-1]] = row[csv_columna]
    datos.append(documento)

try:
    # Conectar a MongoDB
    client = MongoClient(MONGODB_URI_local)
    db = client[MONGODB_DB_NAME]
    coleccion = db[MONGODB_COLLECTION_NAME]

    # Insertar los datos en MongoDB
    result = coleccion.insert_many(datos)
    print(f"Datos importados con éxito. Se insertaron {len(result.inserted_ids)} documentos.")
except Exception as e:
    print(f"Error al insertar datos en MongoDB: {str(e)}")