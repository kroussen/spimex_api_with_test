import pytest

from pydantic import ValidationError

from source.schemas.spimex import DateLastSchema, TradingDynamicsSchema, TradingResultSchema, SpimexDataSchema

from tests.fakes.fake_params_schema import (
    TEST_DATE_LAST_SCHEMA_PARAMS,
    TEST_TRADING_DYNAMICS_SCHEMA_PARAMS,
    TEST_TRADING_RESULT_SCHEMA_PARAMS,
    TEST_SPIMEX_DATA_SCHEMA_PARAMS
)


@pytest.mark.parametrize("input_data, expected_output, should_raise", TEST_DATE_LAST_SCHEMA_PARAMS)
def test_date_last_schema(input_data, expected_output, should_raise):
    if should_raise:
        with pytest.raises(ValidationError):
            DateLastSchema(**input_data)
    else:
        schema = DateLastSchema(**input_data)
        assert schema.count_last_days == expected_output


@pytest.mark.parametrize("input_data, expected_output, should_raise", TEST_TRADING_DYNAMICS_SCHEMA_PARAMS)
def test_trading_dynamics_schema(input_data, expected_output, should_raise):
    if should_raise:
        with pytest.raises((ValidationError, ValueError)):
            TradingDynamicsSchema(**input_data)
    else:
        schema = TradingDynamicsSchema(**input_data)
        assert schema.dict() == expected_output


@pytest.mark.parametrize("input_data, expected_output, should_raise", TEST_TRADING_RESULT_SCHEMA_PARAMS)
def test_trading_result_schema(input_data, expected_output, should_raise):
    if should_raise:
        with pytest.raises(ValidationError):
            TradingResultSchema(**input_data)
    else:
        schema = TradingResultSchema(**input_data)
        assert schema.dict() == expected_output


@pytest.mark.parametrize("input_data, expected_output, should_raise", TEST_SPIMEX_DATA_SCHEMA_PARAMS)
def test_spimex_data_schema(input_data, expected_output, should_raise):
    if should_raise:
        with pytest.raises(ValidationError):
            SpimexDataSchema(**input_data)
    else:
        schema = SpimexDataSchema(**input_data)
        assert schema.dict() == expected_output
