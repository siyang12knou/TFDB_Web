import os
import uuid
from datetime import datetime
from stat import S_ISDIR, filemode

import paramiko
from fastapi import UploadFile
from object_pool import ObjectPool
from sqlmodel.ext.asyncio.session import AsyncSession

from config import message
from config.constants import Action
from config.settings import Settings
from model.file_info import FileInfo
from service import logger
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

    def get_file_list(self, remote_dir: str, session: AsyncSession, user_id: str):
        file_list = []
        with self.client.open_sftp() as sftp:
            for entry in sftp.listdir_attr(remote_dir):
                file_list.append(FileInfo(name=entry.filename,
                                          path=entry.longname,
                                          is_dir=S_ISDIR(entry.st_mode),
                                          mode=filemode(entry.st_mode),
                                          last_modified=datetime.fromtimestamp(entry.st_mtime)))

        return file_list

    def download_file(self, remote_file_path: str, session: AsyncSession, user_id: str):
        local_file_path = os.path.join(settings.TEMP_DIR, uuid.uuid4() + separator + remote_file_path[remote_file_path.rindex("/") + 1:])
        with self.client.open_sftp() as sftp:
            sftp.get(remote_file_path, local_file_path)

        logger.info(session, Action.download_file.name, message.download_file.format(user_id=user_id, file=remote_file_path), user_id)

        return local_file_path

    def upload_file(self, upload_file: UploadFile, remote_dir: str, session: AsyncSession, user_id: str):
        with self.client.open_sftp() as sftp:
            sftp.putfo(fl=upload_file.file, remotepath=remote_dir)

        logger.info(session, Action.upload_file.name,
                    message.upload_file.format(user_id=user_id, file=remote_dir + "/" + upload_file.filename),
                    user_id)

    def delete_file(self, remote_file_path: str, session: AsyncSession, user_id: str):
        with self.client.open_sftp() as sftp:
            sftp.remove(remote_file_path)

        logger.info(session, Action.upload_file.name,
                    message.delete_file.format(user_id=user_id, file=remote_file_path),
                    user_id)


storage_pool = ObjectPool(Storage, min_init=2)
