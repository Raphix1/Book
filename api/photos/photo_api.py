from fastapi import APIRouter, UploadFile, File
import random

photo_router = APIRouter(prefix="/photo",
                         tags=["Photo API"])
@photo_router.post("/add_photo1")
async def add_photo1(book_id: int,
                     photo_file: UploadFile=File(...)):
    file_id = random.randint(1, 1000000000000)
    if photo_file:
        photo = open(f"database/photos/photo_{file_id}_{book_id}.jpg",
                     "wb")
        try:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        finally:
            photo.close()
        return {"status": 1, "message": "Успешно загружен"}
    return {"status": 0, "message": "Ошибка загрузки"}

@photo_router.post("/add_photo2")
async def add_photo2(post_id: int,
                     photo_file: UploadFile=File(...)):
    file_id = random.randint(1, 1000000000000)
    if photo_file:
        with open(f"database/photos/photo_{file_id}_{post_id}.jpg",
                    "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
        return {"status": 1, "message": "Успешно загружен"}
    return {"status": 0, "message": "Ошибка загрузки"}
