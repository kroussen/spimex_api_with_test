from models.spimex import SpimexData
from schemas.spimex import DateLastSchema, TradingDynamicsSchema, TradingResultSchema
from utils.repository import SQLAlchemyRepository

from sqlalchemy import select


class SpimexRepository(SQLAlchemyRepository):
    model = SpimexData

    async def get_last_trading_dates(self, schema: DateLastSchema = None):
        query = (
            select(self.model.date)
            .distinct()
            .order_by(self.model.date.desc())
            .limit(schema.count_last_days)
        )

        result = await self.session.execute(query)

        dates = result.all()
        return dates

    async def get_dynamics(self, schema: TradingDynamicsSchema):
        filters = {
            "oil_id": schema.oil_id,
            "delivery_type_id": schema.delivery_type_id,
            "delivery_basis_id": schema.delivery_basis_id,
        }

        query = (
            select(self.model)
            .filter(self.model.date.between(schema.start_date, schema.end_date))
        )

        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(self.model, field) == value)

        result = await self.session.execute(query)
        results = result.scalars().all()

        return results

    async def get_trading_results(self, schema: TradingResultSchema):
        filters = {
            "oil_id": schema.oil_id,
            "delivery_type_id": schema.delivery_type_id,
            "delivery_basis_id": schema.delivery_basis_id,
        }

        query = select(self.model)

        for field, value in filters.items():
            if value is not None:
                query = query.filter(getattr(self.model, field) == value)

        result = await self.session.execute(query)
        results = result.scalars().all()

        return results
