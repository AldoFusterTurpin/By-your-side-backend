from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId
from app.models.Resposta import Resposta


class Preguntes(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    Pregunta: str = Field(...)
    Resposta: Resposta = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {

            }
        }
