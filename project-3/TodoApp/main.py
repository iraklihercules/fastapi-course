from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

# Runs only if the database doesn't exist
models.Base.metadata.create_all(bind=engine)
