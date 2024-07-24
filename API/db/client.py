#Conectamos con el servidor. 
#En este caso se trata de una base de datos en local.
from pymongo import MongoClient


# Base de datos harmoni_db local en MongoDB
db_client = MongoClient().harmoni_db