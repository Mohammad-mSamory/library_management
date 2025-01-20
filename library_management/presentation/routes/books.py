from fastapi import APIRouter, Depends, HTTPException
from typing import List
from library_management.presentation.models.models import BookIn, BookOut
from library_management.infrastructure.database.engine import get_db
from library_management.infrastructure.repositories.Base_repository import BookRepository
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=BookOut)
def add_book(book: BookIn, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    new_book = book_repo.add(book.model_dump())
    return new_book

@router.get("/", response_model=List[BookOut])
def list_books(db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    return book_repo.list()

@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book = book_repo.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookIn, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    existing_book = book_repo.get(book_id)
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.model_dump().items():
        setattr(existing_book, key, value)
    book_repo.update(existing_book)
    return existing_book

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book_repo.delete(book_id)
    return {"message": "Book deleted successfully"}
