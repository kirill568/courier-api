from app.schemas.base_schema import BaseSchema

class ActiveOrderSchema(BaseSchema):
    order_id: int
    order_name: str