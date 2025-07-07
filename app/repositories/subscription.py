from uuid import UUID

from app.database.models import Subscription
from app.repositories.base import BaseRepository

class SubscriptionRepository(BaseRepository):

    async def create(self, user_id: UUID) -> bool:
        subscription = Subscription(
            _id=user_id,
            active=True,
        )
        await self.collection.insert_one(subscription)
        return True

    async def update(self, data: dict, subscription_id: UUID) -> bool:
        await self.collection.update_one(
            {'_id': subscription_id},
            {'$set': data}
        )
        return True






