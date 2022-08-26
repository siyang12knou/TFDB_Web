from fastapi import Form
from pydantic import BaseModel
from typing import List, Optional


class Project(BaseModel):
    id_project: Optional[int]
    project_name: str
    project_description: str

    @classmethod
    def as_form(cls, project_name: str = Form(...), project_description: str = Form(...)):
        return cls(project_name=project_name, project_description=project_description)
