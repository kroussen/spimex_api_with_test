import pytest

from source.models.spimex import SpimexData
from source.repositories.spimex import SpimexRepository
from source.schemas.spimex import DateLastSchema, TradingDynamicsSchema, TradingResultSchema

from tests.fakes.fake_api_request_params import (
    TEST_API_REQUEST_GET_LAST_TRADING_DATA,
    TEST_API_REQUEST_GET_DYNAMICS,
    TEST_API_REQUEST_GET_TRADING_RESULTS
)


class TestSpimexRepository:
    class _SpimexRepository(SpimexRepository):
        model = SpimexData

    @pytest.mark.parametrize("count_last_days, expected_count",
                             TEST_API_REQUEST_GET_LAST_TRADING_DATA)
    async def test_get_last_trading_dates(self, clean_database, add_data, async_session, count_last_days,
                                          expected_count):
        await clean_database()
        await add_data()

        sql_alchemy_repository = self._SpimexRepository(session=async_session)
        schema = DateLastSchema(count_last_days=count_last_days)

        dates_in_db = await sql_alchemy_repository.get_last_trading_dates(schema=schema)
        assert len(dates_in_db) == expected_count
        await async_session.close()

    @pytest.mark.parametrize("start_date, end_date, expected_count",
                             TEST_API_REQUEST_GET_DYNAMICS)
    async def test_get_dynamics(self, add_data, clean_database, async_session, start_date, end_date,
                                expected_count):
        await clean_database()
        await add_data()

        sql_alchemy_repository = self._SpimexRepository(session=async_session)
        schema = TradingDynamicsSchema(start_date=start_date, end_date=end_date)

        dates_in_db = await sql_alchemy_repository.get_dynamics(schema=schema)

        assert len(dates_in_db) == expected_count
        await async_session.close()

    @pytest.mark.parametrize("oil_id, delivery_type_id, delivery_basis_id, expected_count",
                             TEST_API_REQUEST_GET_TRADING_RESULTS)
    async def test_get_trading_results(self, add_data, clean_database, async_session, oil_id, delivery_type_id,
                                       delivery_basis_id, expected_count):
        await clean_database()
        await add_data()

        sql_alchemy_repository = self._SpimexRepository(session=async_session)
        schema = TradingResultSchema(oil_id=oil_id, delivery_type_id=delivery_type_id,
                                     delivery_basis_id=delivery_basis_id)

        dates_in_db = await sql_alchemy_repository.get_trading_results(schema=schema)

        assert len(dates_in_db) == expected_count
        await async_session.close()
