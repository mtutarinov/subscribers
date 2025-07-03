from pydantic import Field
from datetime import datetime

from app.schemas.base import BaseEntity

class Payment(BaseEntity):

    payment_datetime:datetime = Field(description='Payment date')