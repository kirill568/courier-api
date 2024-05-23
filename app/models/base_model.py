from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)

    def dict(self):
        return {field.name:getattr(self, field.name) for field in self.__table__.c}