from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .internal import admin
from .routers import items, clients, students

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(clients.router)
app.include_router(items.router)
app.include_router(students.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "This is the description"}},
)


@app.get("/hello", tags=["custom_tag"])
async def root():
    return {"message": "Hello API clients!"}
