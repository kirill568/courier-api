from app.schemas.base_schema import BaseSchema

class OrderSchema(BaseSchema):
    courier_id: int
    status: int