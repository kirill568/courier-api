from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Courier, DistrictCourier, CourierStatuses
from app.repository.base_repository import BaseRepository
from sqlalchemy.future import select
from typing import Union

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