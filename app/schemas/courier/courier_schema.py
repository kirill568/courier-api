from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class CourierSchema(BaseSchema):
    id: Annotated[int, Field(gt=0, example="123", description="Courier ID")]
    name: Annotated[str, Field(min_length=2, max_length=100, example="Kirill", description="Courer name")]