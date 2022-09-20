from pydantic import BaseModel

from model.user import User


class SessionInfo(BaseModel):
    id: str
    name: str
    role: str

    class Config:
        schema_extra = {
            "example": {
                "id": "sample@example.com",
                "name": "100aquinas",
                "role": "[\"USER\"]",
            }
        }

    @classmethod
    def as_user(cls, user: User):
        return cls(id=user.id, name=user.name, role=user.role)

    @classmethod
    def as_dict(cls, info: dict):
        return cls(id=info.get("id", ""), name=info.get("name", ""), role=info.get("role", ""))


