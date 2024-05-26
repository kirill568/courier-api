from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class EntityCreated(BaseSchema):
    id: Annotated[int, Field(gt=0, example="123", description="Created entity ID")]