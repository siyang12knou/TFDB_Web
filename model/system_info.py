import datetime

from pydantic import BaseModel


class SystemInfo(BaseModel):
    enabled: bool
    deleted: bool
    created_date: datetime.datetime
    modified_date: datetime.datetime
