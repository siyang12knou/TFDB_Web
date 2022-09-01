from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: Optional[str] = None
    DB_URL: Optional[str] = f'mysql+aiomysql://kailoslab:Kailos0601!@localhost:3306/tfdb?charset=utf8mb4'
    REDIS_HOST: Optional[str] = 'localhost'
    REDIS_PORT: Optional[int] = 6379

    class Config:
        env_file = ".env"
