#schemas/thermical.py

from pydantic import BaseModel
from typing import Optional

class ThermicalSchema(BaseModel):
    _id: Optional[str] = None
    ci_identification: str
    thermical_heat_dissipated: Optional[float] = None
    thermical_head_load_to_air: Optional[float] = None
    thermical_head_load_to_coolant: Optional[float] = None
    thermical_skin_temperature_above_ambient: Optional[float] = None
    thermical_requires_cooling: Optional[bool] = None

    class Config:
        json_schema_extra  = {
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

