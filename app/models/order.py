from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, Enum
from sqlalchemy.orm import relationship
from app.models.base_model import BaseModel
import enum

class OrderStatuses(enum.Enum):
    created = "created"
    finished = "finished"

class Order(BaseModel):
    __tablename__ = "order"

    name = Column(String(100), nullable=False)
    courier_id = Column(Integer, ForeignKey("courier.id", ondelete='SET NULL'), nullable=True)
    district_id = Column(Integer, ForeignKey("district.id", ondelete='SET NULL'), nullable=True)
    start_date = Column(DateTime, index=True, nullable=False)
    finish_date = Column(DateTime, index=True, nullable=True)
    status = Column(Enum(OrderStatuses), nullable=False)

    district = relationship("District", back_populates="orders")
    courier = relationship("Courier", back_populates="orders")