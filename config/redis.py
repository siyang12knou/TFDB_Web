import random
from datetime import timedelta

import redis
import json

from service.secure import decrypt
from config.settings import Settings
from fastapi_redis_session.config import basicConfig

settings = Settings()
host = decrypt(settings.REDIS_HOST)
port = settings.REDIS_PORT
db = 0

basicConfig(
    redisURL=f"redis://{host}:{port}/{db}",
    sessionIdName="TFDB_SESSION",
    sessionIdGenerator=lambda: str(random.randint(1000, 9999)),
    expireTime=timedelta(minutes=30),
    )


def get_redis_conn():
    if RedisWrapper.conn is not None:
        return RedisWrapper.conn

    pool = redis.ConnectionPool(host=host, port=port, db=db)
    r = redis.StrictRedis(connection_pool=pool, charset="utf-8", decode_responses=True)
    RedisWrapper.conn = r
    return r


def exist_redis(key: str) -> bool:
    redis_conn = get_redis_conn()
    if redis_conn is not None:
        return redis_conn.exists(key)

    return False


def set_dict_redis(key: str, value: dict):
    json_value = json.dumps(value, ensure_ascii=False).encode('utf-8')
    set_str_redis(key, json_value)


def get_dict_redis(key: str) -> dict:
    return dict(json.loads(get_str_redis(key)))


def set_list_redis(key: str, value: list):
    json_value = json.dumps(value, ensure_ascii=False).encode('utf-8')
    set_str_redis(json_value)


def get_list_redis(key: str) -> dict:
    return list(json.loads(get_str_redis(key)))


def set_str_redis(key: str, value: str):
    redis_conn = get_redis_conn()
    if redis_conn is not None:
        redis_conn.set(key, value)
    else:
        raise "Please connect a redis server."


def get_str_redis(key: str) -> str:
    redis_conn = get_redis_conn()
    if redis_conn is not None:
        return redis_conn.get(key).decode('utf-8')
    else:
        raise "Please connect a redis server."


def delete_redis(key: str):
    redis_conn = get_redis_conn()
    if redis_conn is not None:
        redis_conn.delete(key)


class RedisWrapper:
    conn: redis.Redis = None

