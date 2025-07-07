from app.database.models import Payment
from app.repositories.base import BaseRepository

class PaymentRepository(BaseRepository):

    async def create(self, data: dict) -> bool:
        payment = Payment(**data)
        await self.collection.insert_one(payment)
        return True