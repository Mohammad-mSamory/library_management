from fastapi import APIRouter, HTTPException
from typing import List
from library_management.presentation.models.models import Book, BookCreate, BookUpdate
from library_management.application.book_service import BookService
from library_management.infrastructure.repositories.Base_repository import BookRepository
from uuid import UUID

router = APIRouter()

# Initialize repository and service
book_repo = BookRepository()
book_service = BookService(book_repo)


@router.post("/", response_model=Book)
def add_book(book_data: BookCreate):
    new_book = book_service.add_book(book_data.model_dump())
    if not new_book:
        raise HTTPException(status_code=400, detail="Book not added.")
    return new_book


@router.get("/", response_model=List[Book])
def get_books():
    return book_service.list_books()


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    book = book_service.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: UUID, book_data: BookUpdate):
    updated_book = book_service.update_book(book_id, book_data.model_dump())
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found.")
    return updated_book


@router.delete("/{book_id}")
def delete_book(book_id: UUID):
    book_service.delete_book(book_id)
    return {"detail": "Book deleted successfully."}
