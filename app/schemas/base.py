from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4
from datetime import datetime

class BaseEntity(BaseModel):

    id: UUID = Field(default_factory=uuid4, alias='_id')
    user: UUID = Field(description='User UUID')

    class Config:
        json_encoders = {
            UUID: str,
            datetime: lambda dt: dt.isoformat()
        }