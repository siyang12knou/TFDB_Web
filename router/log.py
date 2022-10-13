from fastapi import APIRouter, Depends

from config.db import get_session

log_router = APIRouter(
    tags=["Log"]
)


@log_router.get("/dummy")
async def create_dummy_log(session=Depends(get_session)):
    pass
