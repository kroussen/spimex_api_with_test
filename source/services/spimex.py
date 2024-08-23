import json

from datetime import datetime
from typing import List

from schemas.serializers.serializers import datetime_to_string
from schemas.spimex import DateLastSchema, TradingDynamicsSchema, TradingResultSchema
from utils.service import BaseService
from utils.unit_of_work import transaction_mode


class SpimexService(BaseService):
    base_repository: str = 'spimex_repository'

    async def _fetch_and_cache(self, cache_key: str, fetch_func, cache, **kwargs):
        cached_data = await cache.get(cache_key)
        if cached_data:
            return json.loads(cached_data)

        data = await fetch_func(**kwargs)
        serialized_data = [item.to_pydantic_schema().dict() for item in data]
        await cache.set(cache_key, json.dumps(serialized_data, default=datetime_to_string))
        return serialized_data

    @transaction_mode
    async def get_last_trading_dates(self, schema: DateLastSchema, cache) -> List[str]:
        cache_key = f"last_trading_dates:{schema.count_last_days}"

        cached_data = await cache.get(cache_key)
        if cached_data:
            return json.loads(cached_data)

        date_list: List[datetime] = await self.uow.spimex_repository.get_last_trading_dates(schema=schema)
        formatted_dates: List[str] = [date_tuple[0].strftime('%Y-%m-%d') for date_tuple in date_list]

        await cache.set(cache_key, json.dumps(formatted_dates))
        return formatted_dates

    @transaction_mode
    async def get_dynamics(self, schema: TradingDynamicsSchema, cache):
        cache_key = f"dynamics:{schema.start_date}:{schema.end_date}:{schema.oil_id}:{schema.delivery_type_id}:{schema.delivery_basis_id}"
        return await self._fetch_and_cache(cache_key, self.uow.spimex_repository.get_dynamics, schema=schema,
                                           cache=cache)

    @transaction_mode
    async def get_trading_results(self, schema: TradingResultSchema, cache):
        cache_key = f"trading_results:{schema.oil_id}:{schema.delivery_type_id}:{schema.delivery_basis_id}"
        return await self._fetch_and_cache(cache_key, self.uow.spimex_repository.get_trading_results, schema=schema,
                                           cache=cache)
