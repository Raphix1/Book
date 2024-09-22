from database.models import Book, Genre
from database import get_db

def add_book_db(author_name, header, genre=None, description=None):
    with next(get_db()) as db:
        new_book = Book(author_name=author_name, header=header, genre=genre, description=description)
        db.add(new_book)
        db.commit()
        return new_book.id

def get_all_books_db():
    with next(get_db()) as db:
        all_books = db.query(Book).all()
        return all_books

def get_exact_book_by_header_db(book_header):
    with next(get_db()) as db:
        book = db.query(Book).filter_by(header=book_header).all()
        if book:
            return book
        return "Такой книги нет"

def get_exact_book_by_id_db(book_id):
    with next(get_db()) as db:
        book = db.query(Book).filter_by(id=book_id).first()
        if book:
            return book
        return "Такой книги нет"


def get_books_author_db(author_name):
    with next(get_db()) as db:
        book = db.query(Book).filter_by(author_name=author_name).all()
        if book:
            return book
        return "Такого автора нет"

def change_book_db(book_id, change_info, new_info):
    with next(get_db()) as db:
        book = db.query(Book).filter_by(id=book_id).first()
        if book:
            if change_info == "header":
                book.header = new_info
            elif change_info == "genre":
                book.genre = new_info
            elif change_info == "description":
                book.description = new_info
            db.commit()
            return True
        return "Такой книги нет"

def delete_book_db(book_id):
    with next(get_db()) as db:
        book_del = db.query(Book).filter_by(id=book_id).first()
        if book_del:
            db.delete(book_del)
            db.commit()
            return True
        return "Такой книги нет"

def add_genre_db(genre_name):
    with next(get_db()) as db:
        new_genre = Genre(genre_name=genre_name)
        db.add(new_genre)
        db.commit()
        return new_genre.id

def get_all_books_by_genre_db(size, genre_name):
    with next(get_db()) as db:
        exact_genre = db.query(Genre).filter_by(genre_name=genre_name).first()
        if exact_genre:
            exact_books = db.query(Book).filter_by(genre=genre_name).limit(size).all()
            return exact_books
        return False
