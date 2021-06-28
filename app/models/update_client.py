from pydantic import BaseModel
import datetime
from datetime import date
from typing import List, Optional

from app.models.personal_record import PersonalRecord
from app.models.pyobject import PyObjectId
from bson import ObjectId

class UpdateClientModel(BaseModel):
    fullName: Optional[str]
    joinDate: Optional[datetime.date]
    risc: Optional[str]
    etapaId: Optional[str]
    personalRecord: Optional[List[PersonalRecord]]

    class Config:
        schema_extra = {
            "example": {
                "fullName": "Name Of Women",
                "joinDate": "2021-05-04",
                "risc": "Alt",
                "etapaId" : "8345691"
                # "personalRecord": {
                #     "":"h",
                # }
            }
        }
