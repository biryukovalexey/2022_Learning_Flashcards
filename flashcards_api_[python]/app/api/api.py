from fastapi import APIRouter

from api.endpoints import flashcards

api_router = APIRouter()
api_router.include_router(router=flashcards.router, prefix="/flashcards")