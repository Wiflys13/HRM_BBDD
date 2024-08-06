#schemas/thermical.py

from pydantic import BaseModel
from typing import Optional

class ThermicalSchema(BaseModel):
    id: Optional[str]
    ci_identification: str   #Clave primaria única
    thermical_heat_dissipated: Optional[float]
    thermical_head_load_to_air: Optional[float]
    thermical_head_load_to_coolant: Optional[float]
    thermical_skin_temperature_above_ambient: Optional[float]         #pendiente de determinar
    thermical_requires_cooling: Optional[float]  

    class Config:
        schema_extra = {
            "example": {
                "id": "603d2149e4b0a2b7c7d06f5f",
                "ci_identification": "315111-00001",
                "thermical_heat_dissipated": "-",
                "thermical_head_load_to_air": "-",
                "thermical_head_load_to_coolant": "-",
                "thermical_skin_temperature_above_ambient": "-",
                "thermical_requires_cooling": "-",
                # Incluye valores de ejemplo para otros campos si es necesario
            }
        }

