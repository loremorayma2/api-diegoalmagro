from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.database.db import get_db
from app.models.user_model import User
from app.models.product_model import Product
from app.schemas.product_schema import ProductoCreate, ProductoResponse
from app.core.security import get_current_user

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[ProductoResponse])
async def list_products(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    products = result.scalars().all()
    return products

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductoCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_product = Product(**product.dict(), owner_id=current_user.id)
    db.add(new_product)
    await db.commit()
    await db.refresh(new_product)
    return new_product
