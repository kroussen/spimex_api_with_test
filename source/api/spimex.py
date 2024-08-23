from typing import List

from fastapi import APIRouter, Depends

from services.spimex import SpimexService
from schemas.spimex import DateLastSchema, TradingResultSchema, TradingDynamicsSchema, SpimexDataSchema
from utils.cache import get_redis_client

router = APIRouter(prefix='/api', tags=['spimex'])


@router.get('/last_trading_dates')
async def get_last_trading_dates(schema: DateLastSchema = Depends(),
                                 service: SpimexService = Depends(SpimexService),
                                 cache=Depends(get_redis_client)):
    dates = await service.get_last_trading_dates(schema=schema, cache=cache)
    return dates


@router.get('/dynamics', response_model=List[SpimexDataSchema])
async def get_dynamics(schema: TradingDynamicsSchema = Depends(),
                       service: SpimexService = Depends(SpimexService),
                       cache=Depends(get_redis_client)):
    trading_result = await service.get_dynamics(schema=schema, cache=cache)
    return trading_result


@router.get('/trading_results', response_model=List[SpimexDataSchema])
async def get_trading_results(schema: TradingResultSchema = Depends(),
                              service: SpimexService = Depends(SpimexService),
                              cache=Depends(get_redis_client)) -> List[SpimexDataSchema]:
    trading_result: List[SpimexDataSchema] = await service.get_trading_results(schema=schema, cache=cache)
    return trading_result
