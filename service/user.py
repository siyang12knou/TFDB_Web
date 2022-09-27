from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from auth.hash_password import create_hash
from config import message
from model.user import User
from service import logger

SYSTEM_USER_ID = "system"


async def get_user(user_id: str, session: AsyncSession) -> User:
    return await session.get(User, user_id)


async def save_user(user: User, session: AsyncSession, request_user_id: str = SYSTEM_USER_ID) -> User:
    user_exist: User = await session.get(User, user.id)
    if not user_exist:
        return await create_user(user, session, request_user_id)
    else:
        return await update_user(user, session, user_exist, request_user_id)


async def create_user(user: User, session: AsyncSession, request_user_id: str = SYSTEM_USER_ID) -> User:
    user.enabled = True
    user.deleted = False
    now = datetime.now()
    user.created_date = now
    user.modified_date = now
    if user.password:
        user.password = create_hash(user.password.strip())
    if not user.role:
        user.role = "[\"Visitor\"]"
    session.add(user)
    await session.commit()
    await session.refresh(user)
    logger.info(session, "create_user", message.create_user.format(user_id=user.id), request_user_id)
    return user


async def update_user(user: User, session: AsyncSession, user_exist: User = None, request_user_id: str = SYSTEM_USER_ID) -> User:
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
    logger.info(session, "update_user", message.update_user.format(user_id=user.id), request_user_id)
    return user_exist


async def delete_user(user_id: str, session: AsyncSession, request_user_id: str = SYSTEM_USER_ID) -> bool:
    user_exist: User = await session.get(User, user_id)
    if user_exist is not None:
        user_exist.deleted = True
        session.add(user_exist)
        await session.commit()
        logger.info(session, "delete_user", message.delete_user.format(user_id=user_id), request_user_id)
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

    system: User = await session.get(User, SYSTEM_USER_ID)
    if not system:
        system = User()
        system.id = SYSTEM_USER_ID
        system.password = "Kailos0601!"
        system.role = "[\"ADMIN\"]"
        system.name = "System"
        system.email = "kailoslab@gmail.com"
        await create_user(system, session)

