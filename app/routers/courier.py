from fastapi import APIRouter, Path, Depends, status
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from app.models import Courier, Order
from app.schemas.courier import CreateCourierSchema, CourierSchema, DetailedCourierSchema
from app.schemas.order import ActiveOrderSchema
from app.schemas.response import EntityCreated, ErrorMessage
from app.repository import CourierRepository
from app.services import CourierService
from app.container import Container
from app.dependencies.courier_dependencies import valid_courier_id
from datetime import time

router = APIRouter(
    prefix="/courier", 
    tags=["courier"]
)

@router.get("", response_model=Union[List[CourierSchema], None])
@inject
async def get_couriers(repository: CourierRepository = Depends(Provide[Container.courier_repository])):
    return await repository.get_all()

@router.get("/{id}", response_model=DetailedCourierSchema, responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessage}})
@inject
async def get_courier(courier: Courier = Depends(valid_courier_id), repository: CourierRepository = Depends(Provide[Container.courier_repository])):
    active_order: Union[Order, None] = await repository.get_active_order(courier.id)
    avg_order_complete_time: time = await repository.get_avg_order_complete_time(courier.id)
    avg_day_orders: int = await repository.get_avg_day_orders(courier.id)

    active_order_schema = None
    if active_order is not None:
        active_order_schema = ActiveOrderSchema(order_id=active_order.id, order_name=active_order.name)

    return DetailedCourierSchema(
        id=courier.id, 
        name=courier.name, 
        active_order=active_order_schema, 
        avg_order_complete_time=avg_order_complete_time, 
        avg_day_orders=avg_day_orders
    )

@router.post("", response_model=EntityCreated)
@inject
async def create_courier(item: CreateCourierSchema, service: CourierService = Depends(Provide[Container.courier_service])):
    courier: Courier = await service.create_courier(item)

    return EntityCreated(id=courier.id)