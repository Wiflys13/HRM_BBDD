# Preprocesamiento de Datos para `harmoni_db`

Este documento describe el proceso de preprocesamiento realizado en los datos de harmoni. El objetivo es preparar los datos para su análisis y carga en herramientas como MongoDB y PowerBI.

## Descripción del Dataset

- **Archivo de Entrada**: `pbs.csv`
- **Descripción**: El archivo contiene información sobre identificaciones, nombres de ítems, acrónimos, y desarrolladores, junto con varias columnas numéricas relacionadas con el sistema.

## Pasos de Preprocesamiento

1. **Lectura del Archivo CSV**

   El archivo CSV se lee y se carga en un DataFrame de pandas.
   
   ```python
   import pandas as pd
   pbs_csv = pd.read_csv('pbs.csv')
