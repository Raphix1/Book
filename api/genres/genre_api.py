from fastapi import APIRouter
from api import result_message
from database import get_db
from database.bookservice import add_genre_db, get_all_books_by_genre_db

genre_route = APIRouter(prefix="/genre", tags=["Genre API"])

@genre_route.post("/add_genre")
async def add_genre_api(genre_name):
    with next(get_db()) as db:
        result = add_genre_db(genre_name)
        return result_message(result)

@genre_route.get("/get_book_genre")
async def get_all_books_by_genre_api(genre_name):
    result = get_all_books_by_genre_db(genre_name)
    return result_message(result)