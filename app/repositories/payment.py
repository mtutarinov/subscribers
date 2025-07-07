from uuid import UUID

from app.database.models import Payment
from app.repositories.base import BaseRepository

class PaymentRepository(BaseRepository):

    async def create(self, data: dict) -> bool:
        payment = Payment(**data)
        await self.collection.insert_one(payment)
        return True

    async def update(self, payment_id: UUID, data: dict) -> bool:
        await self.collection.update_one(
            {'_id': payment_id},
            {'$set': data}
        )
        return True