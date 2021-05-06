from fastapi import APIRouter

router = APIRouter(tags=["clients"])


@router.get("/clients")
async def get_clients():
    return [
        {"client1": "info1"},
        {"client2": "info2"},
    ]


@router.get("/clients/{client_id}")
async def read_client(client_id: int):
    return {"client": client_id}
