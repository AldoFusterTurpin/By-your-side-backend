from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId
from app.models.resposta import Resposta


class Pregunta(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    pregunta: str = Field(...)
    resposta: str = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "pregunta": "A on viu?",
                "resposta?" : "Actualment viu a Barcelona"
            }
        }
