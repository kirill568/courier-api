from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated, List

class CreateCourierSchema(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=100)]
    districts_ids: List[int]