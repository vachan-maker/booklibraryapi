from fastapi import FastAPI,Depends,Request
import models,database
from sqlalchemy.orm import Session

models.Base.metadata.create_all(database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal() # for creating a new local connection
    try:
        yield db
    finally:
        db.close() #close the session afterwards

@app.post("/books")
async def create_book(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    book = models.Book(
        title=data.get("title"),
        author=data.get("author"),
        description=data.get("description", ""),
        year=data.get("year_published"),
        available=data.get("available", True)
    )
    db.add(book)
    db.commit()
    db.refresh(book)

    return {"id":book.id,"message":"Book added Successfully"}

@app.get("/book")
async def get_book(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books