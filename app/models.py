import datetime
from datetime import date
from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr


# custom validations class
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


# fitxa tècnica
class PersonalRecord(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")


class ClientModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    fullName: str = Field(...)
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


class UpdateStudentModel(BaseModel):
    firstName: Optional[str]
    email: Optional[EmailStr]
    course: Optional[str]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "firstName": "Jane Doe",
                "email": "jdoe@example.com",
                "course": "Experiments, Science, and Fashion in Nanophotonics",
                "gpa": "3.0",
            }
        }