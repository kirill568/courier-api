from fastapi import APIRouter, Path, Depends, status
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from app.models import Courier, Order
from app.schemas.courier import CreateCourierSchema, CourierSchema, DetailedCourierSchema
from app.schemas.order import ActiveOrderSchema
from app.schemas.response import EntityCreated, ErrorMessage
from app.repository import CourierRepository, OrderRepository
from app.services import CourierService
from app.container import Container
from app.dependencies.courier_dependencies import valid_courier_id
from datetime import time

router = APIRouter(
    prefix="/courier", 
    tags=["courier"]
)

@router.get(
    "", 
    response_model=Union[List[CourierSchema], None],
    response_description="List of couriers",
    summary="Get info about all couriers in the system"
)
@inject
async def get_couriers(repository: CourierRepository = Depends(Provide[Container.courier_repository])):
    return await repository.get_all()

@router.get(
    "/{id}", 
    response_model=DetailedCourierSchema, 
    response_description="Detailed info about courier",
    summary="Get detailed info about courier",
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ErrorMessage, "description": "Courier not found"}
    }
)
@inject
async def get_courier(
    courier: Courier = Depends(valid_courier_id), 
    courier_repository: CourierRepository = Depends(Provide[Container.courier_repository]),
    order_repository: OrderRepository = Depends(Provide[Container.order_repository])
):
    active_order: Union[Order, None] = await order_repository.get_active_order_by_courier_id(courier.id)
    avg_order_complete_time: time = await courier_repository.get_avg_order_complete_time(courier.id)
    avg_day_orders: int = await courier_repository.get_avg_day_orders(courier.id)

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

@router.post(
    "", 
    response_model=EntityCreated,
    summary="Registering a courier in the system",
    response_description="Registered courier ID",
    responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessage, "description": "District not found"}}
)
@inject
async def create_courier(item: CreateCourierSchema, service: CourierService = Depends(Provide[Container.courier_service])):
    courier: Courier = await service.create_courier(item)

    return EntityCreated(id=courier.id)