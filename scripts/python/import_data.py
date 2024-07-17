# scripts/python/import_data.py
import sys
import os
import csv
import mysql.connector
from mysql.connector import Error

# Asegúrate de tener configurado tu archivo config.py correctamente
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from config.config import DB_CONFIG, DATA_FILE_PATH

# Función para conectar a MySQL y cargar datos desde CSV
def import_data_from_csv_to_pbs(csv_file):
    connection = None
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()

            # Leer datos del archivo CSV
            with open(csv_file, 'r', encoding='latin1') as file:
                reader = csv.DictReader(file, delimiter=';')
                
                for row in reader:
                    # Obtener los datos de cada fila del CSV
                    pbs_ci_identification = row['PBS number']
                    pbs_level = row['PBS Level']
                    pbs_component = row['Component']
                    pbs_subassembly = row['Subassembly']
                    pbs_assemblys = row['Assembly']
                    pbs_unit = row['Unit']
                    pbs_modules = row['Module']
                    pbs_subsystems = row['Subsystem']
                    pbs_systems = row['System']
                    item_name = row['Name from PBS/BoM']
                    acronym = row['Acronym']
                    # Convertir 'Is component' a entero
                    component_active_str = row['Is component'].strip().lower()  # Convertir a minúsculas y eliminar espacios
                    component_active = 1 if component_active_str == 'yes' else 0

                    component_type = row['Component type']
                    component_type = row['Component type']
                    component_status = row['Status of component selection']
                    component_description = row['Description']
                                        # Convertir 'Field components?' a entero
                    component_field_str = row['Field components?'].strip().lower()  # Convertir a minúsculas y eliminar espacios
                    component_field = 1 if component_field_str == 'yes' else 0
                    institution = row['Institution Responsible']
                    lab_tool = row['Lab tool?']

                    # Insertar datos en la tabla MySQL
                    cursor.execute("""
                        INSERT INTO harmoni_db.pbs (
                            pbs_ci_identification, pbs_level, pbs_component, pbs_subassembly,
                            pbs_assemblys, pbs_unit, pbs_modules, pbs_subsystems, pbs_systems,
                            item_name, acronym, component_active, component_type, component_status, 
                            component_description, component_field, institution, lab_tool
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (pbs_ci_identification, pbs_level, pbs_component, pbs_subassembly,
                          pbs_assemblys, pbs_unit, pbs_modules, pbs_subsystems, pbs_systems,
                          item_name, acronym, component_active, component_type, component_status, 
                          component_description, component_field, institution, lab_tool))
            
            # Confirmar los cambios en la base de datos
            connection.commit()
            print("Datos insertados correctamente en la tabla 'pbs'.")

    except Error as e:
        print(f"Error al conectar a MySQL o al insertar datos: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada.")

# Función para conectar a MySQL y cargar datos desde CSV
def import_data_from_csv_to_bom(csv_file):
    connection = None
    try:
        # Conectar a la base de datos
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()

            # Leer datos del archivo CSV
            with open(csv_file, 'r', encoding='latin1') as file:
                reader = csv.DictReader(file, delimiter=';')
                
                for row in reader:
                    # Obtener los datos de cada fila del CSV
                    mass = float(row['Mass']) if row['Mass'] else None 
                    material = row['Material']
                    treatment = row['Treatment']
                    coating = row['Coating']
                    step_link = row['STEP Link']
                    pbs_ci_identification = row['PBS number']

                    # Insertar datos en la tabla MySQL
                    cursor.execute("""
                        INSERT INTO harmoni_db.bom (
                            mass, material, treatment, coating, step_link, pbs_ci_identification
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                    """, (mass, material, treatment, coating, step_link, pbs_ci_identification))
            
            # Confirmar los cambios en la base de datos
            connection.commit()
            print("Datos insertados correctamente en la tabla 'pbs'.")

    except Error as e:
        print(f"Error al conectar a MySQL o al insertar datos: {e}")

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada.")

"""
# Ejecutar la función con el nombre del archivo CSV
if __name__ == "__main__":
    csv_file = os.path.join(DATA_FILE_PATH, 'EjemploBOM_completo.csv')  # Ruta al archivo CSV
    import_data_from_csv_to_pbs(csv_file)
"""
if __name__ == "__main__":
    csv_file = os.path.join(DATA_FILE_PATH, 'EjemploBOM_completo.csv')  # Ruta al archivo CSV
    import_data_from_csv_to_bom(csv_file)