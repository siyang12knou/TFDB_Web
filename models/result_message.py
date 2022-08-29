from pydantic import BaseModel


class ResultMessage(BaseModel):
    result: bool
    message: str
    data: object

    def __init__(self, result=True, message="데이터 처리에 성공하였습니다.", data=None):
        self.result = result
        self.message = message
        self.data = data

    class Config:
        schema_extra = {
            "example": {
                "result": False,
                "message": "이미 존재하는 사용자입니다."
            }
        }
