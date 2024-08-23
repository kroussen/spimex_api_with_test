from typing import Optional

import redis.asyncio as redis


class RedisCache:
    def __init__(self, redis_url):
        self.client = redis.from_url(redis_url)

    async def get_cache(self, key: str) -> Optional[str]:
        value = await self.client.get(key)
        return value.decode() if value else None

    async def set_cache(self, key: str, value: str, expiration: Optional[int] = None):
        await self.client.set(key, value, ex=expiration)

    async def close(self):
        await self.client.close()


redis_cache = RedisCache("redis://localhost:6379/0")

def get_redis_client():
    client = redis.Redis(host='localhost', port=6379, db=0)
    try:
        yield client
    finally:
        client.close()
