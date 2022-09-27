import datetime

from pydantic import BaseModel


class FileInfo(BaseModel):
    name: str
    path: str
    is_dir: bool
    mode: str
    modified_date: datetime.datetime

    class Config:
        schema_extra = {
            "example": {
                "name": "sample.txt",
                "path": "/dir1/dir2/sample.txt",
                "is_dir": False,
                "mode": "-rw-r--r-- 1",
                "modified_date": "2022-06-23 16:14:11"
            }
        }
