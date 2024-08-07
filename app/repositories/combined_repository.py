from fastapi import HTTPException, status
from db.session import db_client
from bson import ObjectId
from typing import Dict, Any
from logs.logger import logger

async def get_combined_data(ci_identification: str) -> Dict[str, Any]:
    try:
        # Buscar en cada colección
        components = db_client.Components.find_one({"ci_identification": ci_identification})
        electrical = db_client.Electrical.find_one({"ci_identification": ci_identification})
        mechanical = db_client.Mechanical.find_one({"ci_identification": ci_identification})
        procurement = db_client.Procurement.find_one({"ci_identification": ci_identification})
        thermical = db_client.Thermical.find_one({"ci_identification": ci_identification})

        # Verificar si al menos uno de los datos fue encontrado
        if not (components or electrical or mechanical or procurement or thermical):
            logger.debug(f"No se encontraron datos para {ci_identification}")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data not found")

        # Combinar los datos
        combined_data = {
            "components": components if components else {},
            "electrical": electrical if electrical else {},
            "mechanical": mechanical if mechanical else {},
            "procurement": procurement if procurement else {},
            "thermical": thermical if thermical else {}
        }

        # Limpiar los datos vacíos
        combined_data = {k: v for k, v in combined_data.items() if v}

        logger.debug(f"Datos combinados para {ci_identification}: {combined_data}")
        return combined_data

    except HTTPException as e:
        # Propagar excepciones HTTP
        logger.error(f"HTTPException al obtener datos combinados para {ci_identification}: {str(e)}")
        raise e
    except Exception as e:
        # Manejar otros errores
        logger.error(f"Error al obtener datos combinados para {ci_identification}: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
