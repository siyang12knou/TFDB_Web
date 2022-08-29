from fastapi import APIRouter, HTTPException, status, Depends
from database.connection import get_session
from models.user import User, UserSignIn, UserOut
from models.result_message import ResultMessage

user_router = APIRouter(
    tags=["User"]
)

users = {}


@user_router.post("/signup")
async def signup_user(data: User, session=Depends(get_session)) -> ResultMessage:
    user_exist = User.find_one(User.id == data.id)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    await session.add(data)
    await session.commit()
    await session.refresh(data)

    return ResultMessage(message="User successfully registered!")


@user_router.post("/signin")
async def signin_user(user: UserSignIn) -> ResultMessage:
    user_exist = User.find_one(User.id == user.id)

    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if user_exist.password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return ResultMessage(message="User signed in successfully", data=UserOut.as_user(user_exist))

