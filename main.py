import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from config.db import conn_db
from router.project import project_router
from router.sample import sample_router
from router.session import session_router
from router.user import user_router

app = FastAPI()

app.include_router(session_router, prefix="/session")
app.include_router(user_router, prefix="/user")
app.include_router(project_router, prefix="/project")
app.include_router(sample_router, prefix="/sample")


@app.on_event("startup")
async def on_startup():
    await conn_db()


@app.get("/")
async def home():
    return RedirectResponse(url="/sample/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
