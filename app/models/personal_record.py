from typing import List

from app.models.pregunta import Pregunta
from app.models.pyobject import PyObjectId
from bson import ObjectId
from pydantic import BaseModel, Field


# fitxa tècnica
class PersonalRecord(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    area: str = Field(...)  # enumeració
    nivellActual: int = Field(..., le=5) #
    nivellObjectiu: int = Field(..., le=5)
    preguntes: List[Pregunta] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "area": "Econòmica",
                "nivellActual": "",
                "formulari": "",
            }
        }
