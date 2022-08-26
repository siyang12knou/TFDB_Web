from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from models.project import Project
from models.project_item import ProjectItems

project_router = APIRouter()
project_list = []
templates = Jinja2Templates(directory="templates/")


@project_router.post("/project", status_code=status.HTTP_201_CREATED)
async def add_project(request: Request, project: Project = Depends(Project.as_form)):
    project.id_project = len(project_list) + 1;
    project_list.append(project)
    return templates.TemplateResponse("project.html", {
        "request": request,
        "project_list": project_list
    })


@project_router.get("/project", response_model=ProjectItems)
async def get_projects(request: Request):
    return templates.TemplateResponse("project.html", {
        "request": request,
        "project_list": project_list
    })


@project_router.get("/project/{id_project}")
async def get_project(request: Request, id_project: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for project in project_list:
        if project.id_project == id_project:
            return templates.TemplateResponse("project.html", {
                "request": request,
                "project": project
            });

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project with supplied ID doesn't exist."
    )


@project_router.put("/project/{id_project}")
async def update_project(project_data: Project, id_project: int = Path(..., title="The ID of the project to be updated")) -> dict:
    for project in project_list:
        if project.id_project == id_project:
            project.project_name = project_data.project_name
            project.project_description = project_data.project_description
            return {
                "message": "Project updated successfully."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project with supplied ID doesn't exist."
    )


@project_router.delete("/project/{id_project}")
async def delete_project(id_project: int) -> dict:
    for index in range(len(project_list)):
        project = project_list[index]
        if project.id_project == id_project:
            project_list.pop(index)
            return {
                "message": "Project deleted successfully."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Project with supplied ID doesn't exist."
    )


@project_router.delete("/project")
async def delete_projects() -> dict:
    project_list.clear()
    return {
        "message": "Projects deleted successfully."
    }

