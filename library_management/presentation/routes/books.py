from typing import List
from uuid import UUID

from fastapi import APIRouter, HTTPException

from library_management.application.book_service import BookService
from library_management.infrastructure.repositories.Base_repository import \
    BookRepository
from library_management.presentation.models.models import (Book, BookCreate,
                                                           BookUpdate)

router = APIRouter()

# Initialize repository and service
book_repo = BookRepository()
book_service = BookService(book_repo)


def raise_http_exception(status_code: int, detail: str):
    """Helper function to raise HTTPException."""
    raise HTTPException(status_code=status_code, detail=detail)


@router.post("/", response_model=Book)
def add_book(book_data: BookCreate):
    new_book = book_service.add_book(book_data.model_dump())
    if not new_book:
        raise_http_exception(400, "Book not added.")
    return new_book


@router.get("/", response_model=List[Book])
def get_books():
    books = book_service.list_books()
    if not books:
        raise_http_exception(404, "No books found.")
    return books


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: UUID):
    book = book_service.get_book(book_id)
    if not book:
        raise_http_exception(404, "Book not found.")
    return book


@router.put("/{book_id}", response_model=Book)
def update_book(book_id: UUID, book_data: BookUpdate):
    updated_book = book_service.update_book(book_id, book_data.model_dump())
    if not updated_book:
        raise_http_exception(404, "Book not found.")
    return updated_book


@router.delete("/{book_id}")
def delete_book(book_id: UUID):
    try:
        book_service.delete_book(book_id)
    except ValueError as e:
        raise_http_exception(404, str(e))
    return {"detail": "Book deleted successfully."}
