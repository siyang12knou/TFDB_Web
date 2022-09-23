import asyncio
import json
from datetime import datetime

from sqlmodel.ext.asyncio.session import AsyncSession

from model.log import Log


def info(session: AsyncSession, action: str, message: str, user_id: str, data=None):
    __log_sync__(session, "INFO", action, message, user_id, data)


def warning(session: AsyncSession, action: str, message: str, user_id: str, data=None):
    __log_sync__(session, "WARNING", action, message, user_id, data)


def error(session: AsyncSession, action: str, message: str, user_id: str, data=None):
    __log_sync__(session, "ERROR", action, message, user_id, data)


def __log_sync__(session: AsyncSession, level: str, action: str, message: str, user_id: str, data):
    loop = None
    try:
        loop = asyncio.get_event_loop()
    except:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    if loop is not None:
        coroutine = __log__(session, level, action, message, user_id, data)
        loop.run_until_complete(coroutine)


async def __log__(session: AsyncSession, level: str, action: str, message: str, user_id: str, data):
    log = Log(level=level, action=action, message=message, user_id=user_id,
              data=data if isinstance(data, str) else json.dumps(data) if None is not data else data,
              created_date=datetime.now())
    session.add(log)
    await session.commit()
    await session.refresh(log)
    return log
