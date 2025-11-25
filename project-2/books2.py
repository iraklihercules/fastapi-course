from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

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
    # id: Optional[int] = None
    id: Optional[int] = Field(
        description="ID is not required for creation", default=None
    )
    title: str = Field(min_length=3)
    author: str = Field(min_lengt=3, max_length=20)
    rating: int = Field(gt=-1, lt=6)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "New book",
                "author": "New author",
                "rating": 5,
            }
        }
    }


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
    new_book.id = generate_book_id()
    BOOKS.append(new_book)


def generate_book_id():
    return BOOKS[-1].id + 1 if BOOKS else 1
