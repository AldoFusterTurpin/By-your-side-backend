import os
from typing import List

from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import motor.motor_asyncio
import fastapi

from app.models.client import ClientModel

SPECIFIC_CLIENT_PATH = "/clients/{id}"
CLIENTS_PATH = "/clients"

CLIENTS_COLLECTION = "clients"

motor_client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
my_db = motor_client["college"]
router = fastapi.APIRouter(tags=["clients"])


@router.get(CLIENTS_PATH, response_description="Get clients", response_model=List[ClientModel])
async def get_clients():
    return await my_db[CLIENTS_COLLECTION].find().to_list(1000)


@router.post(CLIENTS_PATH, response_description="Add new client", response_model=ClientModel)
async def create_client(input_client: ClientModel = Body(...)):
    client_encoded = jsonable_encoder(input_client)

    new_client = await my_db[CLIENTS_COLLECTION].insert_one(client_encoded)
    created_client = await my_db["clients"].find_one({"_id": new_client.inserted_id})

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_client)


@router.get(SPECIFIC_CLIENT_PATH, response_description="Get client by id", response_model=ClientModel)
async def get_client_by_id(client_id: str):
    client_found = await my_db[CLIENTS_COLLECTION].find_one({"_id": client_id})
    if client_found is not None:
        return client_found

    raise HTTPException(status_code=404, detail=f"Student {client_id} not found")
