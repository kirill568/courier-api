from fastapi import APIRouter, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from app.models import Courier
from app.schemas.courier import CreateCourierSchema, CourierSchema
from app.schemas.response import EntityCreated
from app.repository import CourierRepository
from app.services import CourierService
from app.container import Container

router = APIRouter(
    prefix="/courier", 
    tags=["courier"]
)

@router.get("", response_model=Union[List[CourierSchema], None])
@inject
async def get_couriers(repository: CourierRepository = Depends(Provide[Container.courier_repository])):
    return await repository.get_all()

@router.post("", response_model=EntityCreated)
@inject
async def create_courier(item: CreateCourierSchema, service: CourierService = Depends(Provide[Container.courier_service])):
    courier: Courier = await service.create_courier(item)

    return EntityCreated(id=courier.id)