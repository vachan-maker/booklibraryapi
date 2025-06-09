from fastapi import FastAPI
from . import models,database
from sqlalchemy.orm import Session

models.Base.metadata.create_all(database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal() # for creating a new local connection
    try:
        yield db
    finally:
        db.close()