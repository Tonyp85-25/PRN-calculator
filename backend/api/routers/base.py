from fastapi import APIRouter

from .calculations import router as calculations_router

api_router = APIRouter()
api_router.include_router(calculations_router, prefix="", tags=["calculations"])
