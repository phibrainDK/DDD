from fastapi import APIRouter
from api.routes.endpoints import router as router_users

router = APIRouter()

router.include_router(router_users, tags=["Users"])
