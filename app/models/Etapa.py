from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId


class EtapaModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    nom: str = Field(...)
    descripció: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "nom" : "etapa inicial",
                "descripció" : "Primer punt de contacte amb l'entitat Valentes i Acompanyades",
            }
        }
