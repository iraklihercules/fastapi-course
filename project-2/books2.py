from fastapi import FastAPI

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
