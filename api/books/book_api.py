from fastapi import APIRouter
from api import result_message
from database.bookservice import add_book_db, get_all_books_db, get_exact_book_by_id_db, get_exact_book_by_header_db, get_books_author_db, change_book_db, delete_book_db

book_router = APIRouter(prefix="/book", tags=["Book API"])

@book_router.post("/add_book")
async def add_book_api(author_name: str, header: str, genre: str = None, description: str = None):
    result = add_book_db(author_name, header, genre, description)
    return result_message(result)

@book_router.get("/get_all_books")
async def get_all_books_api():
    return get_all_books_db()


@book_router.get("/get_exact_by_name_book")
async def get_exact_book_api(book_header: str):
    result = get_exact_book_by_header_db(book_header)
    return result_message(result)

@book_router.get("/get_exact_by_id_book")
async def get_exact_book_api(book_id: int):
    result = get_exact_book_by_id_db(book_id)
    return result_message(result)

@book_router.get("/get_book_by_author")
async def get_books_author_api(author_name: str):
    result = get_books_author_db(author_name)
    return result_message(result)

@book_router.put("/change_book")
async def change_post_api(book_id: int, change_info: str, new_info: str):
    result = change_book_db(book_id, change_info, new_info)
    return result_message(result)

@book_router.delete("/delete_book")
async def delete_book_api(book_id: int):
    result = change_book_db(book_id)
    return result_message(result)