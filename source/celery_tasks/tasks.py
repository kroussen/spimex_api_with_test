import redis

from datetime import datetime
from ..celety_config import celery_app


@celery_app.task(name='check_execution_time')
def check_execution_time():
    now = datetime.now()
    if now.hour == 14 and now.minute == 11:
        clear_cache()


@celery_app.task(name='clear_cache')
def clear_cache():
    redis_client = redis.Redis.from_url("redis://localhost:6379/0")
    redis_client.flushall()
    return "Cache cleared"
