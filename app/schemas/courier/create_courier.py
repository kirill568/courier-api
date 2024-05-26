from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated, List

class CreateCourierSchema(BaseSchema):
    name: Annotated[str, Field(min_length=2, max_length=100, example="Kirill", description="Courier name")]
    districts_ids: Annotated[List[int], Field(example=[1, 2, 3], description="List of IDs of districts in which the courier will work")]