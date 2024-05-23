from pydantic import BaseModel

class BaseSchema(BaseModel):
    def dict(self):
        return self.model_dump()