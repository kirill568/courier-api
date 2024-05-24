from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Courier
from app.repository.base_repository import BaseRepository

class CourierRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Courier)