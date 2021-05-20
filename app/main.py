import os

import uvicorn
from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .internal import admin
from .routers import items, clients, students, etapes
from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI(dependencies=[Depends(get_query_token)])
app = FastAPI()

app.include_router(clients.router)
# app.include_router(items.router) # TODO remove
# app.include_router(students.router) # TODO remove
app.include_router(etapes.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "This is the description"}},
# )

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/hello", tags=["Hello world"])
# async def root():
#     return {"message": "Hello API clients!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)