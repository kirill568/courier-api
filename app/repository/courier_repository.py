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
    
    async def get_active_order(self, courier_id: int) -> Union[Order, None]:
        async with self.session() as session:
            stmt = (
                select(Order)
                .join(Order.courier)
                .where(Courier.id == courier_id)
                .where(Order.status == OrderStatuses.created)
            )
            result = await session.execute(stmt)
            return result.scalar()
    
    # SELECT AVG(finish_date - start_date) as "diff"
    # FROM "order"
    # WHERE courier_id = 12
    async def get_avg_order_complete_time(self, courier_id: int) -> datetime:
        async with self.session() as session:
            stmt = (
                select(func.avg(Order.finish_date - Order.start_date).label("average"))
                .where(Order.courier_id == courier_id)
                .where(Order.status == OrderStatuses.finished)
            )
            result = await session.execute(stmt)
            return datetime.strptime(str(result.scalar()), '%H:%M:%S.%f').time()

    # SELECT avg(count) FROM (
    #     SELECT COUNT(*)
    #     FROM "order"
    #     WHERE courier_id = 12
    #     GROUP BY date_part('day', finish_date)
    # ) as count
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