from fastapi import APIRouter, Path, Depends
from dependency_injector.wiring import Provide, inject
from typing import Union, List
from app.models import District
from app.schemas.district import CreateDistrictSchema, DistrictSchema
from app.schemas.response import EntityCreated
from app.repository import DistrictRepository
from app.container import Container

router = APIRouter(
    prefix="/district", 
    tags=["district"]
)

@router.get(
    "", 
    response_model=Union[List[DistrictSchema], None],
    summary="Get all districts",
    response_description="List of districts"
)
@inject
async def get_districts(repository: DistrictRepository = Depends(Provide[Container.district_repository])):
    return await repository.get_all()

@router.post(
    "", 
    response_model=EntityCreated,
    summary="Create district",
    response_description="Created district ID"
)
@inject
async def create_district(item: CreateDistrictSchema, repository: DistrictRepository = Depends(Provide[Container.district_repository])):
    item: District = await repository.create(item)

    return EntityCreated(id=item.id)