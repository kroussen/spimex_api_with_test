from datetime import date

TEST_DATE_LAST_SCHEMA_PARAMS = [
    ({"count_last_days": 5}, 5, False),
    ({"count_last_days": None}, None, False),
    ({"count_last_days": 0}, None, True),
    ({"count_last_days": -3}, None, True),
    ({}, None, False),
]

TEST_TRADING_RESULT_SCHEMA_PARAMS = [
    (
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1"
        },
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1"
        },
        False
    ),
    (
        {
            "oil_id": None,
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1"
        },
        {
            "oil_id": None,
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1"
        },
        False
    ),
    (
        {
            "oil_id": None,
            "delivery_type_id": None,
            "delivery_basis_id": None
        },
        {
            "oil_id": None,
            "delivery_type_id": None,
            "delivery_basis_id": None
        },
        False
    ),
    (
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
        },
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
            "delivery_basis_id": None
        },
        False
    ),
]

TEST_TRADING_DYNAMICS_SCHEMA_PARAMS = [
    (
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1",
            "start_date": date(2024, 1, 1),
            "end_date": date(2024, 2, 28),
        },
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1",
            "start_date": date(2024, 1, 1),
            "end_date": date(2024, 2, 28),
        },
        False
    ),
    (
        {
            "oil_id": None,
            "delivery_type_id": None,
            "delivery_basis_id": None,
            "start_date": date(2024, 1, 1),
            "end_date": date(2024, 2, 28),
        },
        {
            "oil_id": None,
            "delivery_type_id": None,
            "delivery_basis_id": None,
            "start_date": date(2024, 1, 1),
            "end_date": date(2024, 2, 28),
        },
        False
    ),
    (
        {
            "oil_id": "oil_1",
            "delivery_type_id": "type_1",
            "delivery_basis_id": "basis_1",
            "start_date": date(2024, 2, 28),
            "end_date": date(2024, 1, 1),
        },
        None,
        True
    ),
]

TEST_SPIMEX_DATA_SCHEMA_PARAMS = [
    (
        {
            "id": 1,
            "exchange_product_id": "prod_1",
            "exchange_product_name": "Product 1",
            "oil_id": "oil_1",
            "delivery_basis_id": "basis_1",
            "delivery_basis_name": "Basis 1",
            "delivery_type_id": "type_1",
            "volume": 1000,
            "total": 500000,
            "count": 10,
            "date": date(2024, 8, 21),
        },
        {
            "id": 1,
            "exchange_product_id": "prod_1",
            "exchange_product_name": "Product 1",
            "oil_id": "oil_1",
            "delivery_basis_id": "basis_1",
            "delivery_basis_name": "Basis 1",
            "delivery_type_id": "type_1",
            "volume": 1000,
            "total": 500000,
            "count": 10,
            "date": date(2024, 8, 21),
        },
        False
    ),
    (
        {
            "id": 2,
            "exchange_product_id": "prod_2",
            "exchange_product_name": "Product 2",
            "volume": 2000,
            "total": 1000000,
            "count": 20,
            "date": date(2024, 8, 22),
        },
        {
            "id": 2,
            "exchange_product_id": "prod_2",
            "exchange_product_name": "Product 2",
            "oil_id": None,
            "delivery_basis_id": None,
            "delivery_basis_name": None,
            "delivery_type_id": None,
            "volume": 2000,
            "total": 1000000,
            "count": 20,
            "date": date(2024, 8, 22),
        },
        False
    ),
    (
        {
            "id": 3,
            "exchange_product_id": "",
            "exchange_product_name": "Product 3",
            "volume": -500,
            "total": 1000,
            "count": -5,
            "date": date(2024, 8, 23),
        },
        None,
        True
    ),
]
