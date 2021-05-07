from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId


# fitxa tècnica
class PersonalRecord(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    description: str = Field(...)
