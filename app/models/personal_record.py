from bson import ObjectId
from pydantic import BaseModel, Field
from app.models.pyobject import PyObjectId


# fitxa tècnica
class PersonalRecord(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    Risc: str = Field(...)


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "Risc": "Alt"

            }
        }
