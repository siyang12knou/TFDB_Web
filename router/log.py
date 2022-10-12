from fastapi import APIRouter, Depends

from config.db import get_session
from log.log_creator import create_log

log_router = APIRouter(
    tags=["Log"]
)


@log_router.get("/dummy")
async def create_dummy_log(session=Depends(get_session)):
    await create_log(session)
