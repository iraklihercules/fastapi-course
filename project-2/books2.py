from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    rating: int

    def __init__(self, id: int, title: str, author: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating


class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    rating: int


BOOKS = [
    Book(1, "Book 1", "Author 1", 5),
    Book(2, "Book 2", "Author 1", 4),
    Book(3, "Book 3", "Author 2", 3),
    Book(4, "Book 4", "Author 2", 2),
    Book(5, "Book 5", "Author 3", 5),
]


@app.get("/books")
def get_books():
    return BOOKS


# @app.post("/books")
# def create_book(book_request=Body()):
#     BOOKS.append(book_request)


@app.post("/books")
def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)
