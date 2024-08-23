from datetime import date
from typing import Optional, Self

from pydantic import BaseModel, Field, model_validator

from schemas.aliases.description import desc_aliases


class DateLastSchema(BaseModel):
    count_last_days: Optional[int] | None = Field(None, ge=1, description=desc_aliases['count'])


class TradingResultSchema(BaseModel):
    oil_id: Optional[str] | None = Field(None, description=desc_aliases['oil_id'])
    delivery_type_id: Optional[str] | None = Field(None, description=desc_aliases['delivery_type_id'])
    delivery_basis_id: Optional[str] | None = Field(None, description=desc_aliases['delivery_basis_id'])


class TradingDynamicsSchema(TradingResultSchema):
    start_date: date = Field(..., description=desc_aliases['start_date'], json_schema_extra="2024-01-01")
    end_date: date = Field(..., description=desc_aliases['last_date'], json_schema_extra="2024-02-31")

    @model_validator(mode='after')
    def check_dates(self) -> Self:
        start_date = self.start_date
        end_date = self.end_date

        if start_date > end_date:
            raise ValueError('start_date should be less then end_date')

        return self


class SpimexDataSchema(BaseModel):
    id: int
    exchange_product_id: str = Field(..., min_length=1, description=desc_aliases['exchange_product_id'])
    exchange_product_name: str = Field(..., min_length=1, description=desc_aliases['exchange_product_name'])
    oil_id: Optional[str] = None
    delivery_basis_id: Optional[str] = None
    delivery_basis_name: Optional[str] = None
    delivery_type_id: Optional[str] = None
    volume: int = Field(..., gt=0, description=desc_aliases['volume'])
    total: int = Field(..., gt=0, description=desc_aliases['total'])
    count: int = Field(..., gt=0, description=desc_aliases['count'])
    date: date

    model_config = {'from_attributes': True}
