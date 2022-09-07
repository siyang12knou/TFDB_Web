from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from auth.authenticate import authenticate
from auth.hash_password import verify_hash
from auth.jwt_handler import create_access_token
from config.db import get_session
from config.redis import exist_redis, set_dict_redis, get_dict_redis, delete_redis
from model.result_message import ResultMessage
from model.session import SessionInfo
from model.user import User
from model.token_response import TokenResponse
from service.user import get_user

session_router = APIRouter(
    tags=["Session"]
)


@session_router.get("/current")
async def get_current(user_id: str = Depends(authenticate)) -> SessionInfo:
    if exist_redis(user_id):
        return SessionInfo.as_dict(get_dict_redis(user_id))

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User does not exist"
    )


@session_router.post("/login")
async def login_user(user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session)) -> ResultMessage:
    user_exist: User = await get_user(user.username, session)

    if not verify_hash(user.password, user_exist.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    access_token = create_access_token(user_exist.id)
    session_info = SessionInfo.as_user(user_exist)
    set_dict_redis(user_exist.id, session_info.dict())

    token: TokenResponse = TokenResponse(token_type="Bearer", access_token=access_token)
    return ResultMessage.as_data(message="User login successfully", data=token)


@session_router.post("/logout")
async def logout_user(user_id: str = Depends(authenticate)) -> ResultMessage:
    delete_redis(user_id)

    return ResultMessage(message="User logout successfully")

