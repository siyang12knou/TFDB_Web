from pydantic import BaseModel


class FileInfo(BaseModel):
    name: str
    path: str
    is_dir: bool
    mode: str

    class Config:
        schema_extra = {
            "example": {
                "name": "sample.txt",
                "path": "/dir1/dir2/sample.txt",
                "is_dir": False,
                "mode": "-rw-r--r-- 1"
            }
        }
