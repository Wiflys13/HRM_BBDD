# Preprocesamiento de Datos para `harmoni_db`

Este documento describe el proceso de preprocesamiento realizado en los datos de harmoni. 
El objetivo es preparar los datos para su análisis y carga en herramientas como MongoDB y PowerBI.

## Descripción del Dataset
- **Archivo de Entrada**: `pbs.csv`
- **Archivo de Entrada**: `bom.csv`
- **Archivo de Entrada**: `electric.csv`

## Pasos de Preprocesamiento

1. **Lectura del Archivo CSV**
Se cargan los ficheros de .csv para su tratamiento con python en un DataFrame de pandas

  ```python
  import pandas as pd
  ```

2. **Unificacion de formato** 
Se le tiene que asignar el mismo formato a cada uno de los datos para poder realizar la unificacion de la base de datos de forma homogenea
