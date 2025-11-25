from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    rating: int
    published_at: int

    def __init__(
        self, id: int, title: str, author: str, rating: int, published_at: int
    ):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating
        self.published_at = published_at


class BookRequest(BaseModel):
    # id: Optional[int] = None
    id: Optional[int] = Field(
        description="ID is not required for creation", default=None
    )
    title: str = Field(min_length=3)
    author: str = Field(min_lengt=3, max_length=20)
    rating: int = Field(gt=-1, lt=6)
    published_at: int = Field(gt=1900, lt=2026)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New book",
                "author": "New author",
                "rating": 5,
                "published_at": 2020,
            }
        }
    }


BOOKS = [
    Book(1, "Book 1", "Author 1", 5, 1985),
    Book(2, "Book 2", "Author 1", 4, 1998),
    Book(3, "Book 3", "Author 2", 3, 2015),
    Book(4, "Book 4", "Author 2", 2, 2017),
    Book(5, "Book 5", "Author 3", 5, 2022),
]


@app.get("/books")
def get_books():
    return BOOKS


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get("/books-by-rating")
def get_books_by_rating(rating: int):
    result = []
    for book in BOOKS:
        if book.rating == rating:
            result.append(book)
    return result


@app.get("/books-by-published-at")
def get_books_by_published_at(published_at: int):
    result = []
    for book in BOOKS:
        if book.published_at == published_at:
            result.append(book)
    return result


# @app.post("/books")
# def create_book(book_request=Body()):
#     BOOKS.append(book_request)


@app.post("/books")
def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    new_book.id = generate_book_id()
    BOOKS.append(new_book)


@app.put("/books")
def update_book(book_request: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_request.id:
            BOOKS[i] = Book(**book_request.dict())
            break


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break


def generate_book_id():
    return BOOKS[-1].id + 1 if BOOKS else 1
