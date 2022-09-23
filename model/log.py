from datetime import datetime
from typing import Optional

from sqlalchemy import BigInteger
from sqlmodel import SQLModel, Field


class Log(SQLModel, table=True):

    __tablename__ = "tb_log"

    id: Optional[int] = Field(primary_key=True)
    level: str = "INFO"
    action: str
    message: str
    user_id: str
    data: str
    created_date: datetime

    class Config:
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "id": 1,
                "level": "INFO",
                "action": "login",
                "message": "worker가 로그인하였습니다.",
                "user_id": "worker",
                "data": "Json 문자열",
                "created_date": "2022-06-23 16:14:11"
            }
        }