from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class DistrictSchema(BaseSchema):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=200)]