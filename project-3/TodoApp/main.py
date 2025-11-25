from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
import models
from models import Todos
from database import engine, SessionLocal

app = FastAPI()

# Runs only if the database doesn't exist
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.get("/")
async def get_all_todos(db: db_dependency):
    return db.query(Todos).all()
