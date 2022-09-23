from fastapi import APIRouter, HTTPException, status, Depends

from auth.authenticate import authenticate
from config.db import get_session
from service.storage import storage_pool

storage_router = APIRouter(
    tags=["Storage"]
)


@storage_router.get("/list")
async def get_file_list(path: str):
    with storage_pool.get() as storage:
        return storage.list(path)

