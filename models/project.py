from typing import Optional

from fastapi import Form
from sqlmodel import SQLModel, Field


class Project(SQLModel, table=True):
    id_project: Optional[int] = Field(default=None, primary_key=True)
    project_name: str
    project_description: str

    @classmethod
    def as_form(cls, project_name: str = Form(...), project_description: str = Form(...)):
        return cls(project_name=project_name, project_description=project_description)

    class Config:
        schema_extra = {
            "example": {
                "project_name": "project name",
                "project_description": "this is a sample project."
            }
        }