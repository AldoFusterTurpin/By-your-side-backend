import os
from typing import List

import fastapi
import motor.motor_asyncio
from app.models.etapa import Etapa
from fastapi import Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from ..config import MONGODB_URL

SPECIFIC_ETAPA_PATH = "/etapes/{id}"
ETAPES_PATH = "/etapes"
ETAPES_COLLECTION = "etapes"
DB_NAME = "by_your_side"

motor_client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
my_db = motor_client[DB_NAME]
router = fastapi.APIRouter(tags=["etapes"])

@router.get(ETAPES_PATH, response_description="Get etapes", response_model=List[Etapa])
async def get_etapes():
    cursor = my_db[ETAPES_COLLECTION].find()
    return [item async for item in cursor]  # PEP 530 -- Asynchronous Comprehensions


@router.post(ETAPES_PATH, response_description="Add new Etapa", response_model=Etapa)
async def create_etapa(my_input: Etapa = Body(...)):
    etapa_encoded = jsonable_encoder(my_input)

    new_etapa = await my_db[ETAPES_COLLECTION].insert_one(etapa_encoded)
    created_etapa = await my_db[ETAPES_COLLECTION].find_one({"_id": new_etapa.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_etapa)


@router.get(SPECIFIC_ETAPA_PATH, response_description="Get etapa by id", response_model=Etapa)
async def get_etapa_by_id(etapa_id: str):
    etapa_found = await my_db[ETAPES_COLLECTION].find_one({"_id": etapa_id})
    if etapa_found is None:
        raise HTTPException(status_code=404, detail=f"Etapa {etapa_id} not found")
    
    return etapa_found

@router.delete(SPECIFIC_ETAPA_PATH, response_description="Delete a etapa")
async def delete_etapa(id: str):
    delete_result = await my_db[ETAPES_COLLECTION].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse({"result": "resource deleted"}, status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")