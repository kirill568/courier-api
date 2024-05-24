from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
import enum

class CourierStatuses(enum.Enum):
    idle = "idle"
    busy = "busy"

class Courier(BaseModel):
    __tablename__ = "courier"

    name = Column(String(100), nullable=False)
    status = Column(Enum(CourierStatuses), nullable=False)

    districtCouriers = relationship("DistrictCourier", cascade="all, delete-orphan", lazy="selectin")
    orders = relationship("Order", lazy="selectin")