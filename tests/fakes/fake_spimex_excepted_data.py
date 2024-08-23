from datetime import date

from source.schemas.spimex import TradingDynamicsSchema, TradingResultSchema

# FIRST_PARAM - REQUEST, SECOND_PARAM - EXCEPTED
FAKE_SPIMEX_REQUEST_EXCEPTED_LAST_TRADING_DATES = [
    (1, ['2023-05-10']),
    (3, ['2023-05-10', '2023-04-20', '2023-03-01']),
    (5, ['2023-05-10', '2023-04-20', '2023-03-01', '2023-02-17', '2023-01-13'])
]

# FIRST_PARAM - REQUEST, SECOND_PARAM - EXCEPTED
FAKE_SPIMEX_REQUEST_EXCEPTED_DYNAMICS = [
    (TradingDynamicsSchema(
        start_date="2023-01-13",
        end_date="2023-01-14",
        oil_id=None,
        delivery_type_id=None,
        delivery_basis_id=None
    ), [{
        "id": 1,
        "exchange_product_id": "A100ANK060F",
        "exchange_product_name": "Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)",
        "oil_id": "A100",
        "delivery_basis_id": "ANK",
        "delivery_basis_name": "Ангарск-группа станций",
        "delivery_type_id": "F",
        "volume": 60,
        "total": 3292320,
        "count": 1,
        "date": date(2023, 1, 13)
    }])
]

# FIRST_PARAM - REQUEST, SECOND_PARAM - EXCEPTED
FAKE_SPIMEX_REQUEST_EXCEPTED_TRADING_RESULTS = [
    (TradingResultSchema(
        oil_id="A100",
        delivery_type_id=None,
        delivery_basis_id=None
    ), [{
        "id": 1,
        "exchange_product_id": "A100ANK060F",
        "exchange_product_name": "Бензин (АИ-100-К5), Ангарск-группа станций (ст. отправления)",
        "oil_id": "A100",
        "delivery_basis_id": "ANK",
        "delivery_basis_name": "Ангарск-группа станций",
        "delivery_type_id": "F",
        "volume": 60,
        "total": 3292320,
        "count": 1,
        "date": date(2023, 1, 13)
    }])
]
