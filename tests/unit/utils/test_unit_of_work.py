from source.utils.unit_of_work import UnitOfWork
from source.schemas.spimex import TradingResultSchema


class TestUnitOfWork:

    async def test_uow(self, clean_database, spimex_data, get_data, add_data):
        await clean_database()
        uow = UnitOfWork()
        await add_data()

        async with uow:
            res = await uow.spimex_repository.get_trading_results(schema=TradingResultSchema())

        data_in_db = await get_data()
        assert len(data_in_db) == len(res)
