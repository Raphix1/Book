from fastapi import FastAPI
from api.photos.photo_api import photo_router
from api.files.file_api import file_router
from api.users.user_api import user_router
from api.books.book_api import book_router
from api.genres.genre_api import genre_route
from database import Base, engine

Base.metadata.create_all(engine)

app = FastAPI(docs_url="/")

app.include_router(book_router)
app.include_router(photo_router)
app.include_router(file_router)
app.include_router(user_router)
app.include_router(genre_route)