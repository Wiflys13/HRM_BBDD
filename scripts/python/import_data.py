# scripts/python/import_data.py
import sys
import os
import csv
import mysql.connector
from mysql.connector import Error
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from config.config import DB_CONFIG , DATA_FILE_PATH # Asegúrate de tener configurado tu archivo config.py correctamente

# Función para conectar a MySQL y cargar datos desde CSV
def import_data_from_csv_to_pbs(csv_file):
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()

            # Truncate the table before inserting new data (optional)
            cursor.execute("TRUNCATE TABLE pbs")

            # Insert data from CSV into MySQL table
            with open(csv_file, 'r', encoding='utf-8-sig') as file:
                reader = csv.DictReader(file, delimiter=';')
                for row in reader:
                    pbs_ci_identification = row['PBS number']
                    pbs_level = row ['PBS Level']
                    pbs_component = row ['Component']
                    pbs_subassembly = row ['Subassembly']
                    pbs_assemblys = row ['Assembly']
                    pbs_unit = row ['Unit']
                    pbs_modules = row ['Module']
                    pbs_subsystems = row ['Subsystem']
                    pbs_systems = row ['System']
                    item_name = row ['Name from PBS/BoM']
                    acronym = row ['Acronym']
                    component_active = row ['Is component']
                    component_type = row ['Component type']
                    component_status = row ['Status of component selection']
                    component_description = row ['Description']
                    component_field = row ['Field components?']
                    institution = row ['Institution Responsible']
                    lab_tool = row ['Lab tool?']
                    
                    # Insert row into MySQL table
                    cursor.execute("""
                        INSERT INTO pbs (
                            pbs_ci_identification, pbs_level, pbs_component, pbs_subassembly,
                            pbs_assemblys, pbs_unit,  pbs_modules, pbs_subsystems, pbs_systems,
                            item_name, acronym, component_active, component_type, component_status, 
                            component_description, component_field, institution, lab_tool)
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)
                    """, (pbs_ci_identification, pbs_level, pbs_component, pbs_subassembly,
                            pbs_assemblys, pbs_unit,  pbs_modules, pbs_subsystems, pbs_systems,
                            item_name, acronym, component_active, component_type, component_status, 
                            component_description, component_field, institution, lab_tool))

            connection.commit()
            print("Datos insertados correctamente en la tabla 'pbs'.")

    except Error as e:
        print(f"Error al conectar a MySQL o al insertar datos: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada.")

# Ejecutar la función con el nombre del archivo CSV
if __name__ == "__main__":
    csv_file = os.path.join(DATA_FILE_PATH, 'EjemploBOM_completo.csv')  # Ruta al archivo CSV
    import_data_from_csv_to_pbs(csv_file)
