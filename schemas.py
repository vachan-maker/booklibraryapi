from pydantic import BaseModel

class BookCreate(BaseModel):
    title: str
    author: str
    description: str = ""
    year: int
    available: bool = True
