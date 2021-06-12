from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId
from app.models.etapa import Etapa


class Protocol(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    descripcio: str = Field(...)
    etapes: List[Etapa] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {

            }
        }
