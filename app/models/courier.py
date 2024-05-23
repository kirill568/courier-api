from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

class Courier(BaseModel):
    __tablename__ = "courier"

    name = Column(String(100), nullable=False)

    districtCouriers = relationship("DistrictCourier", cascade="all, delete-orphan", lazy="selectin")
    orders = relationship("Order", lazy="selectin")