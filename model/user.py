from pydantic import BaseModel, EmailStr, constr
from typing import Optional
from sqlmodel import SQLModel, Field
from model.system_info import SystemInfo


class User(SQLModel, SystemInfo, table=True):

    __tablename__ = "tb_user"

    id: str = Field(default=None, primary_key=True)
    name: str
    type: str
    password: str
    email: EmailStr
    tel: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^\d{3}-\d{3,4}-\d{4}$",
        )
    ]
    type: str

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


class UserOut(BaseModel):
    id: str
    name: str
    type: str
    email: EmailStr
    tel: Optional[
        constr(
            strip_whitespace=True,
            regex=r"^\d{3}-\d{3,4}-\d{4}$",
        )
    ]

    class Config:
        schema_extra = {
            "example": {
                "id": "sample@example.com",
                "name": "100aquinas",
                "email": "sample_other@example.com",
                "tel": "010-3104-5284",
                "type": "USER",
            }
        }

    @classmethod
    def as_user(cls, user: User):
        return cls(id=user.id, name=user.name, email=user.email, tel=user.tel, type=user.type)


class PasswordIn(BaseModel):
    id: str
    current_password: str
    new_password: str

    class Config:
        schema_extra = {
            "example": {
                "id": "fastapi@example.com",
                "current_password": "Current password",
                "new_password": "New strong password",
            }
        }
