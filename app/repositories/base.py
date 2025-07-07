from typing import Type, TypeVar
from uuid import UUID
from abc import ABC, abstractmethod

from app.core.logger import get_logger
from motor.motor_asyncio import AsyncIOMotorClient

from app.core.config import settings
from app.database.models import BaseEntity

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(ABC):

    def __init__(self, client: AsyncIOMotorClient, model_cls: Type[T]) -> None:
        self.logger = get_logger(__name__)
        self.client = client
        self.db = self.client[settings.DB_NAME]
        self.collection_name = self._get_collection_name(model_cls)
        self.collection = self.db[self.collection_name]


    @staticmethod
    def _get_collection_name(model_cls):
        return model_cls.Settings.name


    async def get_by_id(self, object_id: UUID) -> BaseEntity:
        return await self.collection.find_one({"_id": object_id})

    @abstractmethod
    async def create(self, object_id) -> bool:
        pass

    @abstractmethod
    async def update(self, object_id, data: dict) -> bool:
        pass
