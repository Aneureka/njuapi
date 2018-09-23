import redis
from flask import current_app


class IRedis(object):
    _instance = None

    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(IRedis, cls).__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        _redis_client = redis.Redis(
            host=current_app.config['REDIS_HOST'],
            port=current_app.config['REDIS_PORT'],
            password=current_app.config['REDIS_PASSWORD']
        )

