# mapping.py
from pydantic import BaseModel
from typing import Dict

#Importamos Schemas
from schemas.components import ComponentsSchema
from schemas.electrical import ElectricalSchema
from schemas.mechanical import MechanicalSchema
from schemas.procurement import ProcurementSchema
from schemas.thermical import ThermicalSchema
from schemas.partnumber import PartNumberSchema

# Diccionario para mapear modelos a esquemas
model_schemas = {
    'Electrical': ElectricalSchema,
    'Components': ComponentsSchema,
    'Mechanical': MechanicalSchema,
    'Procurement': ProcurementSchema,
    'Thermical': ThermicalSchema,
    'PartNumber': PartNumberSchema
}
