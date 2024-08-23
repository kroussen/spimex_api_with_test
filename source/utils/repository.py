from abc import ABC
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_


class AbstractRepository(ABC):
    pass


class SQLAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_last_trading_dates(self, schema: Any = None, **kwargs: Any):
        query = (
            select(self.model.date)
            .distinct()
            .filter_by(**kwargs)
            .order_by(self.model.date.desc())
            .limit(schema.count_last_days if schema else None)
        )

        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_dynamics(self, schema, **kwargs: Any):
        filters = [
            getattr(self.model, field) == value
            for field, value in schema.__dict__.items()
            if value is not None and hasattr(self.model, field)
        ]

        query = select(self.model).filter(
            and_(self.model.date.between(schema.start_date, schema.end_date), *filters)
        )

        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_trading_results(self, schema, **kwargs: Any):
        filters = [
            getattr(self.model, field) == value
            for field, value in schema.__dict__.items()
            if value is not None and hasattr(self.model, field)
        ]

        query = select(self.model).filter(*filters)

        result = await self.session.execute(query)
        return result.scalars().all()
