from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from app.models import Courier
from app.repository import CourierRepository
from app.container import Container
from app.exceptions import NotFoundError

@inject
async def valid_courier_id(id: int, repository: CourierRepository = Depends(Provide[Container.courier_repository])):
    courier: Courier = await repository.get_by_id(id)
    if courier == None:
        raise NotFoundError("Courier not found")
    
    return courier