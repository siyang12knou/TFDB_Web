from typing import List
from pydantic import BaseModel


class ProjectItem(BaseModel):
    project_name: str
    project_description: str

    class Config:
        schema_extra = {
            "example": {
                "project_name": "프로젝트 이름",
                "project_description": "프로젝트 설명"
            }
        }


class ProjectItems(BaseModel):
    projects: List[ProjectItem]

    class Config:
        schema_extra = {
            "example": [
                {
                    "project_name": "프로젝트 이름",
                    "project_description": "프로젝트 설명"
                },
                {
                    "project_name": "다른 프로젝트 이름",
                    "project_description": "다른 프로젝트 설명"
                }
            ]
        }