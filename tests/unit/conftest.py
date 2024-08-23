import pytest

from copy import deepcopy
from datetime import date

from sqlalchemy import insert, text, select

from source.models.spimex import SpimexData
from source.schemas.spimex import SpimexDataSchema

from tests.fakes.fake_spimex_schema import FAKE_SPIMEX_DATA


@pytest.fixture(scope="function")
def spimex_data() -> list[SpimexDataSchema]:
    return deepcopy(FAKE_SPIMEX_DATA)


@pytest.fixture(scope="function")
async def clean_database(async_session_maker):
    sql = text("TRUNCATE TABLE spimex_trading_result_async RESTART IDENTITY CASCADE;")

    async def _clean_database():
        async with async_session_maker() as session:
            await session.execute(sql)
            await session.commit()

    return _clean_database


@pytest.fixture(scope="function")
def add_data(async_session_maker, spimex_data):
    async def _add_data():
        async with async_session_maker() as session:
            for data in spimex_data:
                await session.execute(
                    insert(SpimexData).values(**data.model_dump())
                )
            await session.commit()

    return _add_data


@pytest.fixture(scope="session")
def get_data(async_session_maker):
    async def _get_data():
        async with async_session_maker() as session:
            res = await session.execute(select(SpimexData))
            return res.scalars().all()

    return _get_data


@pytest.fixture(scope="function")
async def spimex_data_model():
    return SpimexData(
        id=1,
        exchange_product_id="A100ANK060F",
        exchange_product_name="Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)",
        oil_id="A100",
        delivery_basis_id="ANK",
        delivery_basis_name="Ангарск-группа станций",
        delivery_type_id="F",
        volume=60,
        total=3292320,
        count=1,
        date=date(2023, 1, 13)
    )
