import os
from typing import List

from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
import fastapi

from app.models.client import Client
from app.models.personal_record import PersonalRecord

from ..config import MONGODB_URL


CLIENTS_PATH = "/clients"
SPECIFIC_CLIENT_PATH = CLIENTS_PATH + "/{id}"
CLIENTS_COLLECTION = "clients"
DB_NAME = "by_your_side"

motor_client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
my_db = motor_client[DB_NAME]
router = fastapi.APIRouter(tags=["clients"])


@router.get(CLIENTS_PATH, response_description="Get clients", response_model=List[Client])
async def get_clients():
    cursor = my_db[CLIENTS_COLLECTION].find()
    return [item async for item in cursor]  # PEP 530 -- Asynchronous Comprehensions
    # return await my_db[CLIENTS_COLLECTION].find().to_list(1000) # <- before


@router.get(SPECIFIC_CLIENT_PATH + "/personal_records", response_description="Get personal record of specific client by id", response_model=PersonalRecord)
async def get_personal_record(client_id: str):
    client_found = await my_db[CLIENTS_COLLECTION].find_one({"_id": client_id})
    print(client_found)
    if client_found is None:
        raise HTTPException(status_code=404, detail=f"Student {client_id} not found")
    
    return client_found["personalRecord"]

@router.post(CLIENTS_PATH, response_description="Add new client", response_model=Client)
async def create_client(input_client: Client = Body(...)):
    client_encoded = jsonable_encoder(input_client)

    new_client = await my_db[CLIENTS_COLLECTION].insert_one(client_encoded)
    created_client = await my_db[CLIENTS_COLLECTION].find_one({"_id": new_client.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_client)


@router.get(SPECIFIC_CLIENT_PATH, response_description="Get client by id", response_model=Client)
async def get_client_by_id(client_id: str):
    client_found = await my_db[CLIENTS_COLLECTION].find_one({"_id": client_id})
    if client_found is None:
        raise HTTPException(status_code=404, detail=f"Student {client_id} not found")
    
    return client_found

@router.delete(SPECIFIC_CLIENT_PATH, response_description="Delete a client")
async def delete_client(id: str):
    delete_result = await my_db[CLIENTS_COLLECTION].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse({"result": "resource deleted"}, status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")