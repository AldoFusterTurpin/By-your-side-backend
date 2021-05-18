from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId


class Resposta(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    text: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {

            }
        }
