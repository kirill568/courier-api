from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class ActiveOrderSchema(BaseSchema):
    order_id: Annotated[int, Field(gt=0, example="123", description="Active order ID")]
    order_name: Annotated[str, Field(min_length=2, max_length=100, example="Pizza", description="Active order name")]