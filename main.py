from fastapi import FastAPI,Depends,Request,HTTPException
import models,database,schemas
from sqlalchemy.orm import Session
import random

models.Base.metadata.create_all(database.engine)
app = FastAPI()

def get_db():
    db = database.SessionLocal() # for creating a new local connection
    try:
        yield db
    finally:
        db.close() #close the session afterwards

@app.post("/books/")
async def create_book(book:schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(**book.model_dump()
    )
    db.add(book)
    db.commit()
    db.refresh(book)

    return {"id":book.id,"message":"Book added Successfully"}

@app.get("/book/")
async def get_book(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    return books

@app.get("/book/{id}/")
async def get_book(id:int,db:Session = Depends(get_db)):
    book = db.query(models.Book).get(id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    else:
        return book
@app.delete("/book/{id}/")
async def delete_book(id:int,db:Session = Depends(get_db)):
    book = db.query(models.Book).get(id)
    if book is None:
        raise HTTPException(status_code=404,detail="Book not found")
    else:
        db.delete(book)
        db.commit()
        return ("Book deleted successfully")
    
@app.get("/random/")
async def get_random_book(db:Session = Depends(get_db)):
    random_number = random.randint(1,10)
    book = db.query(models.Book).get(random_number)
    return book
