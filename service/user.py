from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from auth.hash_password import create_hash
from model.user import User


async def get_user(user_id: str, session: AsyncSession) -> User:
    user = await session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sample with supplied ID does not exist"
        )
    return user


async def save_user(user: User, session: AsyncSession) -> User:
    user_exist: User = await session.get(User, user.id)
    if not user_exist:
        return create_user(user, session)
    else:
        return update_user(user, session, user_exist)


async def create_user(user: User, session: AsyncSession) -> User:
    user.enabled = True
    user.deleted = False
    now = datetime.now()
    user.created_date = now
    user.modified_date = now
    if user.password:
        user.password = create_hash(user.password.strip())
    if not user.type:
        user.role = "[\"Visitor\"]"
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def update_user(user: User, session: AsyncSession, user_exist: User = None) -> User:
    if not user_exist:
        user_exist = await session.get(User, user.id)
        if not user_exist:
            return None

    user_exist.email = user.email
    user_exist.tel = user.tel
    user_exist.name = user.name
    user_exist.modified_date = datetime.now()
    if user.password:
        user_exist.password = create_hash(user.password)
    session.add(user_exist)
    await session.commit()
    await session.refresh(user_exist)
    return user_exist


async def delete_user(user_id: str, session: AsyncSession) -> bool:
    user_exist: User = await session.get(User, user_id)
    if user_exist is not None:
        user_exist.deleted = True
        session.add(user_exist)
        await session.commit()
        return True
    else:
        return False


async def init_user(session: AsyncSession):
    admin: User = await session.get(User, "admin")
    if not admin:
        admin = User()
        admin.id = "admin"
        admin.password = "Kailos0601!"
        admin.role = "[\"ADMIN\"]"
        admin.name = "Admin"
        admin.email = "kailoslab@gmail.com"
        await create_user(admin, session)

