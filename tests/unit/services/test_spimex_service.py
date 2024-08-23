import pytest
import json

from source.services.spimex import SpimexService
from source.schemas.serializers.serializers import datetime_to_string
from source.schemas.spimex import DateLastSchema

from tests.fakes.fake_spimex_excepted_data import (
    FAKE_SPIMEX_REQUEST_EXCEPTED_LAST_TRADING_DATES,
    FAKE_SPIMEX_REQUEST_EXCEPTED_DYNAMICS,
    FAKE_SPIMEX_REQUEST_EXCEPTED_TRADING_RESULTS
)


@pytest.mark.parametrize("count_last_days, expected_dates_list", FAKE_SPIMEX_REQUEST_EXCEPTED_LAST_TRADING_DATES)
async def test_get_last_trading_dates(mock_redis_client, clean_database, add_data, count_last_days,
                                      expected_dates_list):
    await clean_database()
    await add_data()

    service = SpimexService()
    schema = DateLastSchema(count_last_days=count_last_days)

    result = await service.get_last_trading_dates(schema=schema, cache=mock_redis_client)

    assert result == expected_dates_list

    mock_redis_client.get.assert_called_once_with(f"last_trading_dates:{schema.count_last_days}")
    mock_redis_client.set.assert_called_once_with(f"last_trading_dates:{schema.count_last_days}",
                                                  json.dumps(expected_dates_list))


@pytest.mark.parametrize("trading_dynamics_schema, expected_result", FAKE_SPIMEX_REQUEST_EXCEPTED_DYNAMICS)
async def test_get_dynamics(mock_redis_client, clean_database, add_data, trading_dynamics_schema, expected_result):
    await clean_database()
    await add_data()

    service = SpimexService()
    schema = trading_dynamics_schema

    result = await service.get_dynamics(schema=schema, cache=mock_redis_client)
    cache_key = f"dynamics:{schema.start_date}:{schema.end_date}:{schema.oil_id}:{schema.delivery_type_id}:{schema.delivery_basis_id}"

    assert result == expected_result

    mock_redis_client.get.assert_called_once_with(cache_key)
    mock_redis_client.set.assert_called_once_with(cache_key, json.dumps(expected_result, default=datetime_to_string))


@pytest.mark.parametrize("trading_result_schema, expected_result", FAKE_SPIMEX_REQUEST_EXCEPTED_TRADING_RESULTS)
async def test_get_trading_results(mock_redis_client, clean_database, add_data, trading_result_schema, expected_result):
    await clean_database()
    await add_data()

    service = SpimexService()
    schema = trading_result_schema

    result = await service.get_trading_results(schema=schema, cache=mock_redis_client)
    cache_key = f"trading_results:{schema.oil_id}:{schema.delivery_type_id}:{schema.delivery_basis_id}"

    assert result == expected_result

    mock_redis_client.get.assert_called_once_with(cache_key)
    mock_redis_client.set.assert_called_once_with(cache_key, json.dumps(expected_result, default=datetime_to_string))
