from typing import Optional
from sqlmodel import SQLModel, Field


class EDS(SQLModel, table=True):
    id_eds: int = Field(default=None, primary_key=True)
    id_sample: int
    Comment: str
    Points: int


