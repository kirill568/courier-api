from app.services import BaseService
from app.repository import DistrictRepository, OrderRepository, CourierRepository
from app.schemas.order import CreateOrderSchema
from app.exceptions import NotFoundError
from app.models import District, Order, Courier, OrderStatuses, CourierStatuses
from typing import List
import datetime

class OrderService(BaseService):
    def __init__(self, order_repository: OrderRepository, courier_repository: CourierRepository, district_repository: DistrictRepository) -> None:
        self.order_repository = order_repository
        self.courier_repository = courier_repository
        self.district_repository = district_repository
        super().__init__(order_repository)

    async def create_order(self, schema: CreateOrderSchema) -> Order:
        district: District = await self.district_repository.get_by_id(schema.district_id)
        if district is None:
            raise NotFoundError("District not found")

        courier: Courier = await self.courier_repository.get_idle_courier_by_district_id(schema.district_id)
        if courier is None:
            raise NotFoundError("No suitable courier found")
        courier.status = CourierStatuses.busy
        await self.courier_repository.update_attr(courier.id, "status", CourierStatuses.busy)
        
        order: Order = await self.order_repository.create(Order(
            name = schema.name,
            courier_id = courier.id,
            district_id = district.id,
            start_date = datetime.datetime.now(),
            status = OrderStatuses.created
        ))

        return order