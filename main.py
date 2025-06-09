from fastapi import FastAPI
from . import models,database
from sqlalchemy.orm import Session

app = FastAPI()