from pydantic import BaseModel, EmailStr, constr
from typing import Optional, List
from models.system_info import SystemInfo
from models.sample import Sample


class UserOut(BaseModel):
    id: EmailStr
    name: str
    email: EmailStr
    tel: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^\d{3}-\d{3,4}-\d{4}$",
        )
    ]
    type: str
    samples: Optional[List[Sample]]


class User(UserOut, SystemInfo):
    password: str

    class Config:
        schema_extra = {
            "example": {
                "id": "sample@example.com",
                "password": "password string",
                "name": "100aquinas",
                "email": "sample_other@example.com",
                "tel": "010-3104-5284",
                "type": "USER",
                "enabled": 1,
                "deleted": 0,
                "created_date": "2022-06-23 16:14:11",
                "modified_date": "2022-06-23 16:14:11"
            }
        }


class UserSignIn(BaseModel):
    id: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@example.com",
                "password": "strong!!!",
                "events": [],
            }
        }
