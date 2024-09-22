from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    book_fk = relationship("Book", back_populates="author_fk")

class Book(Base):
    __tablename__ = "book"
    id = Column(Integer, primary_key=True, autoincrement=True)
    author_name = Column(String, ForeignKey("author.name"))
    header = Column(String, nullable=False)
    description = Column(String, nullable=True)
    genre = Column(String, ForeignKey("genre.genre_name"))

    author_fk = relationship("Author", lazy="subquery", back_populates="book_fk",
                           cascade="all, delete", passive_deletes=True)
    genre_fk = relationship("Genre", lazy="subquery")

class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, primary_key=True, autoincrement=True)
    genre_name = Column(String, nullable=False)

class BookPhoto(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey("book.id"))
    photo_path = Column(String, nullable=False)

    book_fk = relationship("Book", lazy="subquery")

# class BookFile(Base):
#     __tablename__ = "file"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     book_id = Column(Integer, ForeignKey("book.id"))
#     file_path = Column(String, nullable=False)
#
#     book_fk = relationship("Book", lazy="subquery")





