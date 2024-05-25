from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from app.models import Order
from app.repository import OrderRepository
from app.container import Container
from app.exceptions import NotFoundError

@inject
async def valid_order_id(id: int, repository: OrderRepository = Depends(Provide[Container.order_repository])):
    order: Order = await repository.get_by_id(id)
    if order == None:
        raise NotFoundError("Order not found")
    
    return order