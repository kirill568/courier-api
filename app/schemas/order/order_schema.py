from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class OrderSchema(BaseSchema):
    courier_id: Annotated[int, Field(gt=0, example="123", description="Courier ID")]
    status: Annotated[int, Field(example="1", description="Order status, 1 - in progress, 2 - completed")]