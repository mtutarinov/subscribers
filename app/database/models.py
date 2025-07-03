from typing import Annotated
from beanie import Document, Indexed
from pydantic import Field, field_validator
from uuid import UUID, uuid4
from datetime import datetime, timedelta, timezone

class BaseEntity(Document):

    class Config:
        json_encoders = {
            UUID: str,
            datetime: lambda dt: dt.isoformat()
        }

class Subscribe(BaseEntity):

    user_id: UUID = Field(alias='_id', description="User identifier")
    active: bool = Field(description='Subscribe status')
    datetime_start: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Subscription start date"
    )
    datetime_end: datetime = Field(
        description="Subscription expiration date (in 30 days)"
    )

    @classmethod
    @field_validator('datetime_end')
    def set_datetime_end(cls, v, values):
        if v is None:
            return values['datetime_start'] + timedelta(days=30)
        return v

class Payment(BaseEntity):
    payment_id:UUID = Field(default_factory=uuid4, alias="_id", description="Payment identifier")
    user_id: Annotated[UUID, Indexed()] = Field(description="User identifier")
    payment_datetime:datetime = Field(description='Payment date')

