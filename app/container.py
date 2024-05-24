from dependency_injector import containers, providers

from app.config import POSTGRES_DATABASE_URL
from app.database import DatabaseSessionManager
from app.repository import *
from app.services import *

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.routers",
            "app.dependencies",
        ]
    )

    db = providers.Singleton(DatabaseSessionManager, db_url=POSTGRES_DATABASE_URL)

    district_repository = providers.Factory(DistrictRepository, session=db.provided.session)
    courier_repository = providers.Factory(CourierRepository, session=db.provided.session)
    district_courier_repository = providers.Factory(DistrictCourierRepository, session=db.provided.session)

    courier_service = providers.Factory(CourierService, courier_repository=courier_repository, district_repository=district_repository, district_courier_repository=district_courier_repository)
    district_service = providers.Factory(DistrictService, district_repository=district_repository)