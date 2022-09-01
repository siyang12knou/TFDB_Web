import redis

from config.settings import Settings

settings = Settings()


def get_redis_conn():
    if RedisConnection.redis_conn is not None:
        return RedisConnection.redis_conn

    pool = redis.ConnectionPool(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)
    r = redis.Redis(connection_pool=pool)
    RedisConnection.redis_conn = r
    return r


class RedisConnection:
    redis_conn: redis.Redis = None
