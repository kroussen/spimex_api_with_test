import pytest

from source.schemas.spimex import DateLastSchema, TradingDynamicsSchema, TradingResultSchema
from source.utils.service import BaseService

from tests.fakes.fake_api_request_params import (
    TEST_API_REQUEST_GET_LAST_TRADING_DATA,
    TEST_API_REQUEST_GET_DYNAMICS,
    TEST_API_REQUEST_GET_TRADING_RESULTS
)


class TestBaseService:
    class _BaseService(BaseService):
        base_repository = 'spimex_repository'

    @pytest.mark.parametrize("count_last_days, expected_count",
                             TEST_API_REQUEST_GET_LAST_TRADING_DATA)
    async def test_get_last_trading_data(self, clean_database, add_data, spimex_data, get_data, count_last_days,
                                         expected_count):
        await clean_database()
        await add_data()

        data_in_db = await self._BaseService().get_last_trading_dates(
            schema=DateLastSchema(count_last_days=count_last_days))

        assert len(data_in_db) == expected_count

    @pytest.mark.parametrize("start_date, end_date, expected_count",
                             TEST_API_REQUEST_GET_DYNAMICS)
    async def test_get_dynamics(self, clean_database, add_data, spimex_data, get_data, start_date, end_date,
                                expected_count):
        await clean_database()
        await add_data()

        data_in_db = await self._BaseService().get_dynamics(
            schema=TradingDynamicsSchema(start_date=start_date,
                                         end_date=end_date)
        )

        assert len(data_in_db) == expected_count

    @pytest.mark.parametrize("oil_id, delivery_type_id, delivery_basis_id, expected_count",
                             TEST_API_REQUEST_GET_TRADING_RESULTS)
    async def test_get_trading_results(self, clean_database, add_data, spimex_data, get_data, oil_id, delivery_type_id,
                                       delivery_basis_id, expected_count):
        await clean_database()
        await add_data()

        data_in_db = await self._BaseService().get_trading_results(
            schema=TradingResultSchema(oil_id=oil_id,
                                       delivery_type_id=delivery_type_id,
                                       delivery_basis_id=delivery_basis_id))

        assert len(data_in_db) == expected_count
