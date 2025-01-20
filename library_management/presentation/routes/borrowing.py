from fastapi import APIRouter, Depends, HTTPException
from library_management.infrastructure.database.engine import get_db
from library_management.infrastructure.repositories.Base_repository import BookRepository, MemberRepository
from library_management.application.book_service import BookService
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/{book_id}/{member_id}")
def borrow_book(book_id: int, member_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    member_repo = MemberRepository(db)

    # Check if the book exists
    book = book_repo.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Check if the member exists
    member = member_repo.get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")

    # Perform borrow operation
    book_service = BookService(book_repo)
    book_service.borrow_book(book_id, member_id)
    return {"message": "Book borrowed successfully"}

@router.post("/return/{book_id}")
def return_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)

    # Check if the book exists
    book = book_repo.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    # Perform return operation
    book_service = BookService(book_repo)
    book_service.return_book(book_id)
    return {"message": "Book returned successfully"}
