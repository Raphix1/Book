# from fastapi import APIRouter, UploadFile, File
# import random
#
# file_router = APIRouter(prefix="/file",
#                          tags=["File API"])
# @file_router.post("/add_file")
# async def add_file(book_id: int,
#                    bookfile: UploadFile=File(...)):
#     file_id = random.randint(1, 1000000000000)
#     if bookfile:
#         photo = open(f"database/files/file_{file_id}_{book_id}.pdf",
#                      "wb")
#         try:
#             file_to_save = await bookfile.read()
#             photo.write(file_to_save)
#         finally:
#             photo.close()
#         return {"status": 1, "message": "Успешно загружен"}
#     return {"status": 0, "message": "Ошибка загрузки"}
