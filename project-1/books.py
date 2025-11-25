from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "science"},
    {"title": "Title Two", "author": "Author Two", "category": "science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "math"},
    {"title": "Title Five", "author": "Author Five", "category": "math"},
    {"title": "Title Six", "author": "Author Two", "category": "math"},
]


@app.get("/")
async def first_endpoint():
    return {"message": "Hello world!"}


# Path parameters
@app.get("/params/{dynamic_param}")
async def dynamic_param(dynamic_param: str):
    return {"dynamic_param": dynamic_param}


# Query parameters
@app.get("/params/")
async def query_param(query_param: str):
    return {"query_param": query_param}


@app.get("/books")
async def get_books():
    return BOOKS


@app.get("/books_by_title/{book_title}")
async def get_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books_by_category")
async def get_books_by_category(category: str):
    result = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            result.append(book)
    return result


@app.get("/books_by_author_and_category/{category}")
async def get_books_by_author_and_category(author: str, category: str):
    result = []
    for book in BOOKS:
        if (
            book.get("author").casefold() == author.casefold()
            and book.get("category").casefold() == category.casefold()
        ):
            result.append(book)
    return result


@app.post("/books")
async def create(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books")
async def update(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get("title").casefold():
            BOOKS[i] = updated_book
            break
