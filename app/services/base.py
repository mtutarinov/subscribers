from abc import ABC, abstractmethod
from uuid import UUID

from app.repositories.base import BaseRepository

class BaseService(ABC):

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    @abstractmethod
    async def change_status(self, object_id: UUID):
        pass