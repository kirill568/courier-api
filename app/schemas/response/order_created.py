from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class OrderCreated(BaseSchema):
    order_id: Annotated[int, Field(gt=0, example="123", description="Created order ID")]
    courier_id: Annotated[int, Field(gt=0, example="456", description="ID of the courier who took the order")]