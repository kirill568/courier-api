from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Order, OrderStatuses, Courier
from app.repository.base_repository import BaseRepository
from sqlalchemy.future import select
from typing import Union

class OrderRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Order)

    async def get_active_order_by_courier_id(self, courier_id: int) -> Union[Order, None]:
        async with self.session() as session:
            stmt = (
                select(Order)
                .join(Order.courier)
                .where(Courier.id == courier_id)
                .where(Order.status == OrderStatuses.created)
            )
            result = await session.execute(stmt)
            return result.scalar()