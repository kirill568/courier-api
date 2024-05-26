from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class CreateOrderSchema(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=100, example="Pizza", description="Order name")]
    district_id: Annotated[int, Field(gt=0, example="3", description="District ID")]