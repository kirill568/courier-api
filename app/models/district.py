from sqlalchemy import Column, String
from app.models.base_model import BaseModel
from sqlalchemy.orm import relationship

class District(BaseModel):
    __tablename__ = "district"

    name = Column(String(200), nullable=False)

    districtCouriers = relationship("DistrictCourier", cascade="all, delete-orphan", lazy="selectin")
    orders = relationship("Order", lazy="selectin")