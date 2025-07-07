from typing import Annotated, Optional
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

class Subscription(BaseEntity):

    _id: UUID = Field(description="User identifier")
    active: bool = Field(description='Subscribe status')
    datetime_start: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="Subscription start date"
    )
    datetime_end: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc) + timedelta(days=30),
        description="Subscription expiration date (in 30 days)"
    )

    class Settings:
        name = "subscriptions"


class Payment(BaseEntity):
    _id:UUID = Field(default_factory=uuid4, description="Payment identifier")
    user_id: Annotated[UUID, Indexed()] = Field(description="User identifier")
    payment_datetime:datetime = Field(description='Payment date')

    class Settings:
        name = "payments"
