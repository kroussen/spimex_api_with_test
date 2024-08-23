from utils.unit_of_work import UnitOfWork, transaction_mode


class BaseService:
    base_repository: str

    def __init__(self) -> None:
        self.uow: UnitOfWork = UnitOfWork()

    @transaction_mode
    async def get_last_trading_dates(self, schema):
        return await self.uow.__dict__[self.base_repository].get_last_trading_dates(schema=schema)

    @transaction_mode
    async def get_dynamics(self, schema):
        return await self.uow.__dict__[self.base_repository].get_dynamics(schema=schema)

    @transaction_mode
    async def get_trading_results(self, schema):
        return await self.uow.__dict__[self.base_repository].get_trading_results(schema=schema)
