from fastapi import FastAPI
from app.routers import auth, users, productos, ordenes

app = FastAPI(title="Diego de Almagro API", version="1.0.0")

app.include_router(auth.router, prefix="/api/v1/auth")
app.include_router(users.router, prefix="/api/v1/users")
app.include_router(productos.router, prefix="/api/v1/productos")
app.include_router(ordenes.router, prefix="/api/v1/ordenes")
