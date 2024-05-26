from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class DistrictSchema(BaseSchema):
    id: Annotated[int, Field(gt=0, example="123", description="District ID")]
    name: Annotated[str, Field(min_length=2, max_length=200, example="Central", description="District name")]