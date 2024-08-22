from fastapi import APIRouter

from app.api.api_v1.endpoints.books import router as book

router = APIRouter(
    prefix='/v1'
)

router.include_router(book)
