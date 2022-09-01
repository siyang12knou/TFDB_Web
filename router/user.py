from fastapi import APIRouter, HTTPException, status, Depends

from config.db import get_session
from model.result_message import ResultMessage
from model.user import User
from service.user import init_user, save_user

user_router = APIRouter(
    tags=["User"]
)


@user_router.get("/init")
async def init(session=Depends(get_session)):
    await init_user(session)


@user_router.post("/signup")
async def signup_user(data: User, session=Depends(get_session)) -> ResultMessage:
    user_exist = User.find_one(User.id == data.id)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    save_user(data, session)

    return ResultMessage(message="User successfully registered!")
