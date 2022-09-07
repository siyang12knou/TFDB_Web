import json
from typing import Any

from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


class ResultMessage(BaseModel):
    result: bool = True
    message: str = ""
    data: str = None

    class Config:
        schema_extra = {
            "example": {
                "result": False,
                "message": "이미 존재하는 사용자입니다."
            }
        }

    @classmethod
    def as_data(cls, result=True, message: str = "", data: Any = None):
        return cls(result=result, message=message, data=json.dumps(jsonable_encoder(data if data is not None else {})))
