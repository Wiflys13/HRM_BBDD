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
def import_data_from_csv(csv_file):
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
                    ci_identificacion = row['CI_identification']
                    component = row['Component']
                    subAssembly = row['SubAssemblie']
                    assemblys = row['Assemblie']
                    unit = row['Unit']
                    module = row['Module']
                    sub_systems = row['SubSystem']
                    systems = row['System']
                    acronym = row['Acronym']
                    notes = row['Item_Name']
                    category = row['Developed_by']
                    
                    # Insert row into MySQL table
                    cursor.execute("""
                        INSERT INTO pbs (
                            ci_identificacion, component, subAssembly, assemblys, unit,
                            module, sub_systems, systems, acronym, notes, category
                        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """, (ci_identificacion, component, subAssembly, assemblys, unit,
                          module, sub_systems, systems, acronym, notes, category))

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
    csv_file = os.path.join(DATA_FILE_PATH, 'PBS.csv')  # Ruta al archivo CSV
    import_data_from_csv(csv_file)
