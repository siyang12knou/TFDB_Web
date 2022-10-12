import nest_asyncio
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config.db import conn_db
from router.log import log_router
from router.project import project_router
from router.sample import sample_router
from router.session import session_router
from router.user import user_router

nest_asyncio.apply()
app = FastAPI()
api_app = FastAPI(title="API")

api_app.include_router(session_router, prefix="/session")
api_app.include_router(user_router, prefix="/user")
api_app.include_router(project_router, prefix="/project")
api_app.include_router(sample_router, prefix="/sample")
api_app.include_router(log_router, prefix="/log")

app.mount("/api/v1.0", api_app)
app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.on_event("startup")
async def on_startup():
    await conn_db()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, loop="asyncio")
