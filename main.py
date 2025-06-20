from fastapi import FastAPI
from contextlib import asynccontextmanager
from sqlalchemy.exc import SQLAlchemyError
from app.database.db import engine
from app.routers import auth_route, user_route, product_route, order_route
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.begin() as conn:
            await conn.run_sync(lambda _: None)
        print("✅ Database connection successful.")
    except SQLAlchemyError as e:
        print(f"❌ Database connection failed: {e}")
        raise e

    yield  

app = FastAPI(
    title="Diego de Almagro API",
    version="1.0.0",
    description="API RESTful para el sistema de gestión Diego de Almagro.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_route.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(user_route.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(product_route.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(order_route.router, prefix="/api/v1/orders", tags=["Orders"])
