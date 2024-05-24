from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class CreateOrderSchema(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=100)]
    district_id: Annotated[int, Field(gt=0)]