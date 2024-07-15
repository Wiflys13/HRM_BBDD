# C:\Users\HARMONI\Documents\HARMONI\HRM_BBDD\scripts\python\execute_sql_scripts.py
import sys
import os
import mysql.connector
from mysql.connector import Error
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(project_root)
from config.config import DB_CONFIG

# Función para ejecutar un archivo SQL
def execute_sql_script(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print(f"Connected to MySQL database for executing {file_path}")

            cursor = connection.cursor()
            for result in cursor.execute(sql_script, multi=True):
                if result.with_rows:
                    print(f"Query OK, {result.rowcount} rows affected.")
            connection.commit()
            print(f"Executed {file_path} successfully")

    except Error as e:
        print(f"Error while executing SQL script: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Ruta a los scripts SQL
sql_scripts = [
    os.path.join(os.path.dirname(__file__), '..', 'sql', 'create_tables.sql'),
    os.path.join(os.path.dirname(__file__), '..', 'sql', 'insert_data.sql'),
    os.path.join(os.path.dirname(__file__), '..', 'sql', 'query_data.sql')
]

# Ejecutar los scripts SQL
for script in sql_scripts:
    execute_sql_script(script)
