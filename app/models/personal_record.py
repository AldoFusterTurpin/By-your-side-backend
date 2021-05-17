from bson import ObjectId
from pydantic import BaseModel, Field
from app.models.pyobject import PyObjectId
from app.models.Preguntes import Preguntes

from typing import List


# fitxa tècnica
class PersonalRecord(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    Area: str = Field(...)  # enumeració
    Nivell: str = Field(...)  # enumeració [baix, mitjà, alt]
    Forumlari: List[Preguntes] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "Area": "",
                "Nivell": ""

            }
        }
