from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from database.connection import conn
from routes.project import project_router
from routes.user import user_router
from routes.sample import sample_router

import uvicorn

app = FastAPI()

app.include_router(project_router, prefix="/project")
app.include_router(user_router, prefix="/user")
app.include_router(sample_router, prefix="/sample")


@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/sample/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
