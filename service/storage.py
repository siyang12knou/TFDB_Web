import os
import uuid
from datetime import datetime

import paramiko
from fastapi import Depends
from object_pool import ObjectPool
from stat import S_ISDIR, filemode

from config.db import get_session
from config.settings import Settings
from model.file_info import FileInfo
from service import logger
from service.user import SYSTEM_USER_ID
from service.secure import decrypt

settings = Settings()
separator = "___"


class Storage:
    client: paramiko.SSHClient

    def __init__(self) -> None:
        super().__init__()
        self.client = Storage.__connect__()

    @classmethod
    def __connect__(cls):
        cli = paramiko.SSHClient()
        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        pwd = decrypt(settings.SFTP_PWD)
        if pwd.find(os.sep) == -1:
            cli.connect(hostname=decrypt(settings.SFTP_HOST), port=settings.SFTP_PORT,
                        username=decrypt(settings.SFTP_USER), password=pwd)
            return cli
        else:
            k = paramiko.RSAKey.from_private_key_file(pwd)
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            cli.connect(hostname=decrypt(settings.SFTP_HOST), port=settings.SFTP_PORT,
                        username=decrypt(settings.SFTP_USER), pkey=k)
            return cli

    def check_invalid(self, **stats):
        try:
            transport = self.client.get_transport()
            transport.send_ignore()
            return True
        except EOFError:
            return False

    def clean_up(self, **stats):
        """quits sshclient and sets None, when this method is called"""
        self.client.close()
        self.client = None

    def get_file_list(self, remote_dir: str, session=Depends(get_session)):
        file_list = []
        with self.client.open_sftp() as sftp:
            for entry in sftp.listdir_attr(remote_dir):
                file_list.append(FileInfo(name=entry.filename,
                                          path=entry.longname,
                                          is_dir=S_ISDIR(entry.st_mode),
                                          mode=filemode(entry.st_mode),
                                          last_modified=datetime.fromtimestamp(entry.st_mtime)))

        logger.info(session, "storage_list", "")
        return file_list

    def download_file(self, remote_file_path: str, session=Depends(get_session), request_user_id: str = SYSTEM_USER_ID):
        local_file_path = os.path.join(settings.TEMP_DIR, uuid.uuid4() + separator + remote_file_path[remote_file_path.rindex("/") + 1:])
        with self.client.open_sftp() as sftp:
            sftp.get(remote_file_path, local_file_path)

        return local_file_path

    def upload_file(self, local_file, user_id: str, request_user_id: str = SYSTEM_USER_ID):
        pass


storage_pool = ObjectPool(Storage, min_init=2)
