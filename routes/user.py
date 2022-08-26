from fastapi import APIRouter, HTTPException, status
from models.user import User, UserSignIn

user_router = APIRouter(
    tags=["User"]
)

users = {}


@user_router.post("/signup")
async def signup_user(data: User) -> dict:
    if data.id in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )

    users[data.id] = data

    return {
        "message": "User successfully registered!"
    }


@user_router.post("/signin")
async def signin_user(user: UserSignIn) -> dict:
    if user.id not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )

    if users[user.id].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )

    return {
        "message": "User signed in successfully"
    }

