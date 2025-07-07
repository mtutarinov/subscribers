from uuid import UUID

from app.services.base import BaseService

class PaymentService(BaseService):

    async def create(self, data: dict):
        pass

    async def change_status(self, payment_id: UUID):
        pass