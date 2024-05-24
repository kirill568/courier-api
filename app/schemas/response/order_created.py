from app.schemas.base_schema import BaseSchema

class OrderCreated(BaseSchema):
    order_id: int
    courier_id: int