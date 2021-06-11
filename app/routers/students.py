import os
from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
import motor.motor_asyncio
import fastapi

from app.models.update_student import UpdateStudent
from app.models.client import Client
from ..config import MONGODB_URL

STUDENTS_PATH = "/students"
ID_PATH = "/{id}"
SPECIFIC_STUDENT_PATH = "/students/{id}"
CREATE_RANDOM_STUDENT_PATH = "/create_random_student"
DB_NAME = "by_your_side"


motor_client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
my_db = motor_client[DB_NAME]

router = fastapi.APIRouter(tags=["students"])


@router.post(STUDENTS_PATH, response_description="Add new student", response_model=Client)
async def create_student(student: Client = Body(...)):
    student = jsonable_encoder(student)
    new_student = await my_db["students"].insert_one(student)
    created_student = await my_db["students"].find_one({"_id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@router.post(CREATE_RANDOM_STUDENT_PATH, response_description="Add new random student", response_model=Client)
async def create_student():
    student = Student(fullName="Manolo Provar")
    created_student = await my_db["students"].insert_one(student)
    print(created_student)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@router.get(STUDENTS_PATH, response_description="List all students", response_model=List[Client])
async def list_students():
    students = await my_db["students"].find().to_list(1000)
    return students


@router.get(
    SPECIFIC_STUDENT_PATH, response_description="Get a single student", response_model=Client
)
async def show_student(id: str):
    student = await my_db["students"].find_one({"_id": id})
    if student is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.put(SPECIFIC_STUDENT_PATH, response_description="Update a student", response_model=Client)
async def update_student(id: str, student: UpdateStudent = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}

    if len(student) >= 1:
        update_result = await my_db["students"].update_one({"_id": id}, {"$set": student})

        if update_result.modified_count == 1:
            updated_student = await my_db["students"].find_one({"_id": id})
            if updated_student is not None:
                return updated_student

    existing_student = await my_db["students"].find_one({"_id": id})
    if existing_student is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@router.delete(ID_PATH, response_description="Delete a student")
async def delete_student(id: str):
    delete_result = await my_db["students"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")
