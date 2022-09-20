from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str

    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_USER: str
    MYSQL_PWD: str

    SFTP_HOST: str
    SFTP_PORT: int
    SFTP_USER: str
    SFTP_PWD: str

    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env"
