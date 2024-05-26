from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class ErrorMessage(BaseSchema):
    message: Annotated[str, Field(example="Not found entity with id 123", description="Error message")]