from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated
from app.schemas.order import ActiveOrderSchema
from typing import Union
from datetime import time

class DetailedCourierSchema(BaseSchema):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=100)]
    active_order: Union[None, ActiveOrderSchema]
    avg_order_complete_time: time
    avg_day_orders: int