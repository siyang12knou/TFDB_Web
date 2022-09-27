from typing import Union

from fastapi import APIRouter, Form, UploadFile, Depends
from starlette.responses import FileResponse

from auth.authenticate import authenticate
from config.db import get_session
from model.result_message import ResultMessage
from service.storage import storage_pool

storage_router = APIRouter(
    tags=["Storage"]
)


@storage_router.get("/list")
def get_file_list(path: str, session=Depends(get_session), user_id=Depends(authenticate)):
    with storage_pool.get() as storage:
        return storage.get_file_list(path, session, user_id)


@storage_router.get("/download")
def download_file(path: str, session=Depends(get_session), user_id=Depends(authenticate)):
    with storage_pool.get() as storage:
        local_file_path = storage.download_file(str, session, user_id)
        file_name = local_file_path[path.rfind("/") + 1:]
        return FileResponse(local_file_path, media_type='application/octet-stream', filename=file_name)


@storage_router.get("/upload")
def upload_file(file: Union[UploadFile, None] = None, path: str = Form(), session=Depends(get_session), user_id=Depends(authenticate)):
    if not file:
        return ResultMessage.as_data(False, "업로드하는 파일이 존재하지 않습니다.")

    try:
        with storage_pool.get() as storage:
            storage.upload_file(file, path, session, user_id)

        return ResultMessage.as_default()
    except (Exception,):
        return ResultMessage.as_data(False, f"파일({file.filename})을 업로드하는데 실패하였습니다.")
