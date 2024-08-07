import logging
import os

# Crear directorio de logs si no existe
log_directory = os.path.join(os.path.dirname(__file__))
os.makedirs(log_directory, exist_ok=True)

# Ruta del archivo de log
log_filename = os.path.join(log_directory, 'app.log')

# Configurar el logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Crear un manejador para escribir en el archivo de log
file_handler = logging.FileHandler(log_filename)
file_handler.setLevel(logging.DEBUG)

# Crear un formateador y añadirlo al manejador
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Añadir el manejador al logger
logger.addHandler(file_handler)

# Si deseas eliminar el manejador de consola (StreamHandler)
logger.propagate = False