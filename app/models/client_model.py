import datetime
from datetime import date
from typing import List

from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.pyobject import PyObjectId
from app.models.personal_record import PersonalRecord


class ClientModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    fullName: str = Field()
    joinDate: datetime.date = Field(default=date.today())
    personalRecord: List[PersonalRecord] = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "fullName": "Simple Women Name",
                "joinDate": "2021-05-04",
            }
        }