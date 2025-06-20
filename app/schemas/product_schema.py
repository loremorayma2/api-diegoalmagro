from typing import List
from pydantic import BaseModel

class ProductoCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductoResponse(ProductoCreate):
    id: int

    class Config:
        orm_mode = True
