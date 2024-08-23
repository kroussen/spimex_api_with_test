from datetime import date

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Date

from models.base import Base
from schemas.spimex import SpimexDataSchema


class SpimexData(Base):
    __tablename__ = 'spimex_trading_result_async'

    __table_args__ = {
        'extend_existing': True
    }

    id: Mapped[int] = mapped_column(primary_key=True)
    exchange_product_id: Mapped[str] = mapped_column(String(11))
    exchange_product_name: Mapped[str] = mapped_column(String(100))
    oil_id: Mapped[str] = mapped_column(String(4))
    delivery_basis_id: Mapped[str] = mapped_column(String(3))
    delivery_basis_name: Mapped[str] = mapped_column(String(70))
    delivery_type_id: Mapped[str] = mapped_column(String(1))
    volume: Mapped[int] = mapped_column(Integer)
    total: Mapped[int] = mapped_column(Integer)
    count: Mapped[int] = mapped_column(Integer)
    date: Mapped[date] = mapped_column(Date)

    def to_pydantic_schema(self) -> SpimexDataSchema:
        return SpimexDataSchema(
            id=self.id,
            exchange_product_id=self.exchange_product_id,
            exchange_product_name=self.exchange_product_name,
            oil_id=self.oil_id,
            delivery_basis_id=self.delivery_basis_id,
            delivery_basis_name=self.delivery_basis_name,
            delivery_type_id=self.delivery_type_id,
            volume=self.volume,
            total=self.total,
            count=self.count,
            date=self.date
        )
