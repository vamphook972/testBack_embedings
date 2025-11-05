from fastapi import APIRouter
from app.api.v1.routes import wine

api_router_v1 = APIRouter()
api_router_v1.include_router(wine.router, prefix="/wines", tags=["Wines"])