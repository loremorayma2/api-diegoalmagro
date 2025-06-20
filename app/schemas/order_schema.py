from typing import List
from pydantic import BaseModel

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    items: List[OrderItemBase]

class OrderItemResponse(OrderItemBase):
    id: int

    class Config:
        orm_mode = True

class OrderResponse(BaseModel):
    id: int
    total: float
    status: str
    items: List[OrderItemResponse]

    class Config:
        orm_mode = True
