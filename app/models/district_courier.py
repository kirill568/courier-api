from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel

class DistrictCourier(BaseModel):
    __tablename__ = "district_courier"

    district_id = Column(Integer, ForeignKey("district.id", ondelete='CASCADE'), nullable=False)
    courier_id = Column(Integer, ForeignKey("courier.id", ondelete='CASCADE'), nullable=False)

    district = relationship("District", back_populates="districtCouriers")
    courier = relationship("Courier", back_populates="districtCouriers")