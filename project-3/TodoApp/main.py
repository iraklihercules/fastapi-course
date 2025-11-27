from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos

app = FastAPI()

# Runs only if the database doesn't exist
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
