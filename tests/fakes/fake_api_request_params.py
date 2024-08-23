from datetime import date

TEST_API_REQUEST_GET_LAST_TRADING_DATA = [(3, 3), (5, 5), (1, 1)]

TEST_API_REQUEST_GET_DYNAMICS = [
    (date(2023, 1, 1), date(2023, 2, 17), 2),
    (date(2023, 1, 1), date(2023, 5, 10), 5),
    (date(2023, 2, 1), date(2023, 4, 20), 3),
]

TEST_API_REQUEST_GET_TRADING_RESULTS = [
    ('A95', None, None, 2),
    (None, None, "UFA", 1),
    (None, None, None, 5),
]
