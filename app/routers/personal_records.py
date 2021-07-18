import os
from typing import List

from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
import fastapi

from app.models.personal_record import PersonalRecord
from ..config import MONGODB_URL


PERSONAL_RECORDS_PATH = "/personal_records"
SPECIFIC_PERSONAL_RECORD_PATH = PERSONAL_RECORDS_PATH + "/{id}"
PERSONAL_RECORD_COLLECTION = "personal_records"
DB_NAME = "by_your_side"

motor_client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
my_db = motor_client[DB_NAME]
router = fastapi.APIRouter(tags=[PERSONAL_RECORD_COLLECTION])


@router.get(PERSONAL_RECORDS_PATH, response_description="Get " + PERSONAL_RECORD_COLLECTION, response_model=List[PersonalRecord])
async def get_personal_records():
    cursor = my_db[PERSONAL_RECORD_COLLECTION].find()
    return [item async for item in cursor]  # PEP 530 -- Asynchronous Comprehensions
    # return await my_db[PERSONAL_RECORD_COLLECTION].find().to_list(1000) # <- before


@router.post(PERSONAL_RECORDS_PATH, response_description="Add new personal record", response_model=PersonalRecord)
async def create_personal_record(input_personal_record: PersonalRecord = Body(...)):
    personal_record_encoded = jsonable_encoder(input_personal_record)

    new_personal_record = await my_db[PERSONAL_RECORD_COLLECTION].insert_one(personal_record_encoded)
    created_personal_record = await my_db[PERSONAL_RECORD_COLLECTION].find_one({"_id": new_personal_record.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_personal_record)


@router.get(SPECIFIC_PERSONAL_RECORD_PATH, response_description="Get personal record by id", response_model=PersonalRecord)
async def get_personal_record_by_id(personal_record_id: str):
    personal_record_found = await my_db[PERSONAL_RECORD_COLLECTION].find_one({"_id": personal_record_id})
    if personal_record_found is None:
        raise HTTPException(status_code=404, detail=f"Personal record {personal_record_id} not found")
    
    return personal_record_found

@router.delete(SPECIFIC_PERSONAL_RECORD_PATH, response_description="Delete a personal record")
async def delete_personal_record(id: str):
    delete_result = await my_db[PERSONAL_RECORD_COLLECTION].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse({"result": "resource deleted"}, status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Personal record {id} not found")