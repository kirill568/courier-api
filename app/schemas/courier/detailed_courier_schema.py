from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated
from app.schemas.order import ActiveOrderSchema
from typing import Union
from datetime import time

class DetailedCourierSchema(BaseSchema):
    id: Annotated[int, Field(gt=0, example="123", description="Courier ID")]
    name: Annotated[str, Field(min_length=2, max_length=100, example="Kirill", description="Courier name")]
    active_order: Union[None, ActiveOrderSchema]
    avg_order_complete_time: Annotated[time, Field(example="03:23:06.611011", description="Average order complete time")]
    avg_day_orders: Annotated[int, Field(example="2", description="Average number of completed orders per day")]