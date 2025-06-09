from .database import Base
from sqlalchemy import Integer,String,Boolean,Column

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True,index=True) #indexing helps imrpove performance
    title = Column(String,index=True)
    author = Column(String)
    description = Column(String)
    year = Column(Integer)
    isbn = Column(String)
    available = Column(Boolean,default=True)
