from app.schemas.base_schema import BaseSchema
from pydantic import Field
from typing import Annotated

class SuccessMessage(BaseSchema):
    message: Annotated[str, Field(example="Entity successfully updated", description="Success message")]