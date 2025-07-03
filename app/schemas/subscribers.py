from pydantic import Field, field_validator
from datetime import datetime, timezone, timedelta

from app.schemas.base import BaseEntity

class Subscribe(BaseEntity):

    active: bool = Field(description='Subscribe status')
    date_start: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Subscription start date"
    )
    date_end: datetime = Field(
        description="Subscription expiration date (in 30 days)"
    )

    @field_validator('date_end')
    def set_date_end(self, v, values):
        if v is None:
            return values['date_start'] + timedelta(days=30)
        return v