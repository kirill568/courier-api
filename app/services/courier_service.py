from app.services import BaseService
from app.repository import DistrictRepository, CourierRepository, DistrictCourierRepository
from app.exceptions import NotFoundError
from app.models import District, Courier, DistrictCourier, CourierStatuses
from app.schemas.courier import CreateCourierSchema
from typing import List, Union

class CourierService(BaseService):
    def __init__(self, courier_repository: CourierRepository, district_repository: DistrictRepository, district_courier_repository: DistrictCourierRepository) -> None:
        self.courier_repository = courier_repository
        self.district_repository = district_repository
        self.district_courier_repository = district_courier_repository
        super().__init__(courier_repository)

    async def create_courier(self, schema: CreateCourierSchema) -> Courier:        
        courier: Courier = await self.courier_repository.create(Courier(
            name = schema.name,
            status = CourierStatuses.idle
        ))

        for district_id in schema.districts_ids:
            district: Union[District, None] = await self.district_repository.get_by_id(district_id)
            if district is None:
                await self.courier_repository.delete(courier.id)
                raise NotFoundError(f"District with id {district_id} not exist")
            
            await self.district_courier_repository.create(DistrictCourier(
                district_id = district_id,
                courier_id = courier.id
            ))
        
        return courier
            
