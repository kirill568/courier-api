from app.services import BaseService
from app.repository import DistrictRepository
from app.exceptions import NotFoundError
from app.models import District

class DistrictService(BaseService):
    def __init__(self, district_repository: DistrictRepository) -> None:
        super().__init__(district_repository)
