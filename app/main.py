import os

import uvicorn
from fastapi import Depends, FastAPI

from .dependencies import get_token_header
from .internal import admin
from .routers import clients, etapes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(clients.router)
app.include_router(etapes.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/hello", tags=["Hello world"])
async def root():
    return {"message": "Hello world!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)