from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from app.database.db import get_db
from app.models.user_model import User
from app.models.product_model import Product
from app.models.order_model import Order
from app.schemas.order_schema import OrderCreate, OrderResponse,OrderItemBase
from app.core.security import get_current_user

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(
    order_data: OrderCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    total = 0.0
    items_to_add = []

    # Check stock and calculate total
    for item in order_data.items:
        result = await db.execute(select(Product).filter(Product.id == item.product_id))
        product = result.scalars().first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Product ID {item.product_id} not found")
        if product.stock < item.quantity:
            raise HTTPException(status_code=400, detail=f"Insufficient stock for product ID {item.product_id}")
        total += product.price * item.quantity
        items_to_add.append(OrderItemBase(product_id=product.id, quantity=item.quantity))

    new_order = Order(
        total=total,
        status="pending",
        user_id=current_user.id,
        items=items_to_add
    )
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order
