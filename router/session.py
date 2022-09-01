from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm

from auth.authenticate import authenticate, oauth2_scheme
from auth.hash_password import verify_hash
from auth.jwt_handler import create_access_token
from config.db import get_session
from config.redis import get_redis_conn
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
    redis_conn = get_redis_conn();
    if redis_conn.exists(user_id):
        session_dict = redis_conn.hgetall(user_id)
        return SessionInfo.as_dict(session_dict)

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

    redis_conn = get_redis_conn()
    access_token = create_access_token(user_exist.id)
    session_info = SessionInfo.as_user(user_exist)
    redis_conn.hmset(user_exist.id, session_info.__dict__)

    token: TokenResponse = TokenResponse(token_type="Bearer", access_token=access_token)
    return ResultMessage.as_data(message="User login successfully", data=token)


@session_router.post("/logout")
async def logout_user(user_id: str = Depends(authenticate)) -> ResultMessage:
    redis_conn = get_redis_conn()
    redis_conn.delete(user_id)

    return ResultMessage(message="User logout successfully")

