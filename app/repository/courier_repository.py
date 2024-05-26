from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Courier, DistrictCourier, CourierStatuses, Order, OrderStatuses
from app.repository.base_repository import BaseRepository
from sqlalchemy.future import select
from sqlalchemy.sql import func
from sqlalchemy.orm import aliased
from typing import Union
from datetime import datetime
from math import floor

class CourierRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, Courier)

    async def get_idle_courier_by_district_id(self, district_id: int) -> Union[Courier, None]:
        async with self.session() as session:
            stmt = (
                select(Courier)
                .join(Courier.districtCouriers)
                .where(DistrictCourier.district_id == district_id)
                .where(Courier.status == CourierStatuses.idle)
            )
            result = await session.execute(stmt)
            return result.scalar()

    async def get_avg_order_complete_time(self, courier_id: int) -> datetime:
        async with self.session() as session:
            stmt = (
                select(func.avg(Order.finish_date - Order.start_date).label("average"))
                .where(Order.courier_id == courier_id)
                .where(Order.status == OrderStatuses.finished)
            )
            result = await session.execute(stmt)
            return datetime.strptime(str(result.scalar()), '%H:%M:%S.%f').time()

    async def get_avg_day_orders(self, courier_id: int) -> int:
        async with self.session() as session:
            subq = (
                select(func.count("*").label("count"))
                .where(Order.courier_id == courier_id)
                .where(Order.status == OrderStatuses.finished)
                .group_by(func.date_part("day", Order.finish_date))
                .subquery()
            )

            stmt = (
                select(func.avg(subq.columns.count))
            )

            result = await session.execute(stmt)
            return floor(result.scalar())