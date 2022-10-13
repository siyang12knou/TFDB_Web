import asyncio
import json
from datetime import datetime

from sqlmodel.ext.asyncio.session import AsyncSession

from config.constants import Level, Action
from model.log import Log


def info(session: AsyncSession, action: Action, message: str, user_id: str, created_date: datetime = datetime.now(), data=None):
    __log_sync__(session, Level.INFO, action, message, user_id, created_date, data)


def warning(session: AsyncSession, action: Action, message: str, user_id: str, created_date: datetime = datetime.now(), data=None):
    __log_sync__(session, Level.WARNING, action, message, user_id, created_date, data)


def error(session: AsyncSession, action: Action, message: str, user_id: str, created_date: datetime = datetime.now(), data=None):
    __log_sync__(session, Level.ERROR, action, message, user_id, created_date, data)


def __log_sync__(session: AsyncSession, level: Level, action: Action, message: str, user_id: str, created_date: datetime = datetime.now(), data=None):
    loop = None
    try:
        loop = asyncio.get_event_loop()
    except:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if loop is not None:
        coroutine = __log__(session, level, action, message, user_id, created_date, data)
        loop.run_until_complete(coroutine)


async def __log__(session: AsyncSession, level: Level, action: Action, message: str, user_id: str, created_date: datetime = datetime.now(), data=None):
    log = Log(level=level.name, action=action.name, message=message, user_id=user_id,
              data=data if isinstance(data, str) else json.dumps(data) if None is not data else data,
              created_date=created_date)
    print(f"log: {log}")
    session.add(log)
    await session.commit()
    await session.refresh(log)
    return log

