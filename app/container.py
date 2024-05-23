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