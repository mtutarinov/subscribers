from uuid import UUID

from app.services.base import BaseService


class SubscriptionService(BaseService):

    async def pay(self, user_id: str):
        pass


    async def change_status(self, subscription_id: UUID):
        pass


