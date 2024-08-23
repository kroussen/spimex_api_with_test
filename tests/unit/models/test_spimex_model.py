from datetime import date

from sqlalchemy import select

from models.spimex import SpimexData
from schemas.spimex import SpimexDataSchema


async def test_spimex_data_model(async_session, clean_database, add_data):
    await clean_database()
    await add_data()

    result = await async_session.execute(select(SpimexData))
    data_in_db = result.scalars().first()

    assert data_in_db is not None
    assert data_in_db.exchange_product_id == "A100ANK060F"
    assert data_in_db.exchange_product_name == "Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)"
    assert data_in_db.oil_id == "A100"
    assert data_in_db.delivery_basis_id == "ANK"
    assert data_in_db.delivery_basis_name == "Ангарск-группа станций"
    assert data_in_db.delivery_type_id == "F"
    assert data_in_db.volume == 60
    assert data_in_db.total == 3292320
    assert data_in_db.count == 1
    assert data_in_db.date == date(2023, 1, 13)
    await async_session.close()


async def test_spimex_data_to_pydantic_schema(spimex_data_model):
    pydantic_schema = spimex_data_model.to_pydantic_schema()

    assert pydantic_schema == SpimexDataSchema(
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
