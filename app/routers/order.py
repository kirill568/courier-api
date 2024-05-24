from fastapi import APIRouter, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from app.models import Order
from app.schemas.order import CreateOrderSchema, OrderSchema
from app.schemas.response import OrderCreated
from app.repository import OrderRepository
from app.services import OrderService
from app.container import Container

router = APIRouter(
    prefix="/order", 
    tags=["order"]
)

@router.post("", response_model=OrderCreated)
@inject
async def create_order(item: CreateOrderSchema, service: OrderService = Depends(Provide[Container.order_service])):
    order: Order = await service.create_order(item)

    return OrderCreated(order_id=order.id, courier_id=order.courier_id)