from fastapi import APIRouter, Path, Depends, status
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from app.models import Order, OrderStatuses
from app.schemas.order import CreateOrderSchema, OrderSchema
from app.schemas.response import OrderCreated, ErrorMessage, SuccessMessage
from app.repository import OrderRepository
from app.services import OrderService
from app.container import Container
from app.dependencies.order_dependencies import valid_order_id
from typing import Dict

router = APIRouter(
    prefix="/order", 
    tags=["order"]
)

@router.post("", response_model=OrderCreated)
@inject
async def create_order(item: CreateOrderSchema, service: OrderService = Depends(Provide[Container.order_service])):
    order: Order = await service.create_order(item)

    return OrderCreated(order_id=order.id, courier_id=order.courier_id)

@router.get("/{id}", response_model=OrderSchema, responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessage}})
@inject
async def get_order(order: Order = Depends(valid_order_id)):
    status_map: Dict[str, int] = {
        OrderStatuses.created: 1,
        OrderStatuses.finished: 2
    }

    return OrderSchema(courier_id=order.courier_id, status=status_map[order.status])

@router.post("/{id}", response_model=SuccessMessage, responses={status.HTTP_404_NOT_FOUND: {"model": ErrorMessage}, status.HTTP_409_CONFLICT: {"model": ErrorMessage}})
@inject
async def finalize_order(order: Order = Depends(valid_order_id), service: OrderService = Depends(Provide[Container.order_service])):
    await service.finilize_order(order)

    return SuccessMessage(message="Order completed successfully")