from fastapi import APIRouter, HTTPException, status, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_redis_session import getSession, getSessionStorage, SessionStorage, setSession, getSessionId, deleteSession

from auth.authenticate import authenticate
from auth.hash_password import verify_hash
from auth.jwt_handler import create_access_token
from config import message
from config.db import get_session
from model.result_message import ResultMessage
from model.session import SessionInfo
from model.user import User
from model.token_response import TokenResponse
from service import logger
from service.user import get_user

session_router = APIRouter(
    tags=["Session"]
)


@session_router.get("/current")
def get_current(user_id: str = Depends(authenticate),
                session_info: SessionInfo = Depends(getSession)) -> SessionInfo:
    if session_info is not None and session_info.id == user_id:
        return session_info

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User does not exist"
    )


@session_router.post("/login")
async def login_user(response: Response, user: OAuth2PasswordRequestForm = Depends(), session=Depends(get_session),
                     sessionStorage: SessionStorage = Depends(getSessionStorage)) -> ResultMessage:
    user_exist: User = await get_user(user.username, session)
    if not user_exist:
        logger.error(session, "login", message.login_not_exist.format(user_id=user.username), user.username)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sample with supplied ID does not exist"
        )

    if not verify_hash(user.password, user_exist.password):
        logger.error(session, "login", message.login_pwd_fail, user.username)
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    access_token = create_access_token(user_exist.id)
    session_info = SessionInfo.as_user(user_exist)
    setSession(response, session_info, sessionStorage)

    token: TokenResponse = TokenResponse(token_type="Bearer", access_token=access_token)
    logger.info(session, "login", message.login.format(user_id=user.username), user.username)
    return ResultMessage.as_data(message="User login successfully", data=token)


@session_router.post("/logout")
async def logout_user(user_id: str = Depends(authenticate), session=Depends(get_session),
                      session_id: str = Depends(getSessionId),
                      session_storage: SessionStorage = Depends(getSessionStorage)) -> ResultMessage:
    deleteSession(session_id, session_storage)
    logger.info(session, "logout", message.logout.format(user_id=user_id), user_id)
    return ResultMessage(message="User logout successfully")
