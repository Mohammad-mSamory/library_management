from fastapi import  Depends, HTTPException
from typing import List


from app import app
from library_management.presentation.models.models import BookIn , BookOut , MemberIn , MemberOut
from library_management.infrastructure.database.engine import get_db
from library_management.infrastructure.database.schema import BookModel , MemberModel
from library_management.infrastructure.repositories.Base_repository import BookRepository , MemberRepository
from library_management.application.book_service import BookService
from library_management.application.member_service import MemberService
from sqlalchemy.orm import  Session

# Book Endpoints
@app.post("/books/", response_model=BookOut)
def add_book(book: BookIn, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    new_book = BookModel(**book.model_dump())
    book_repo.add(new_book)
    return new_book

@app.get("/books/", response_model=List[BookOut])
def list_books(db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    return book_repo.list()

@app.get("/books/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book = book_repo.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.put("/books/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookIn, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    existing_book = book_repo.get(book_id)
    if not existing_book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in book.model_dump().items():
        setattr(existing_book, key, value)
    book_repo.update(existing_book)
    return existing_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book_repo.delete(book_id)
    return {"message": "Book deleted successfully"}

# Member Endpoints
@app.post("/members/", response_model=MemberOut)
def add_member(member: MemberIn, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    new_member = MemberModel(**member.model_dump())
    member_repo.add(new_member)
    return new_member

@app.get("/members/", response_model=List[MemberOut])
def list_members(db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    return member_repo.list()

@app.get("/members/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    member = member_repo.get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member

@app.put("/members/{member_id}", response_model=MemberOut)
def update_member(member_id: int, member: MemberIn, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    existing_member = member_repo.get(member_id)
    if not existing_member:
        raise HTTPException(status_code=404, detail="Member not found")
    for key, value in member.model_dump().items():
        setattr(existing_member, key, value)
    member_repo.update(existing_member)
    return existing_member

@app.delete("/members/{member_id}")
def delete_member(member_id: int, db: Session = Depends(get_db)):
    member_repo = MemberRepository(db)
    member_repo.delete(member_id)
    return {"message": "Member deleted successfully"}

# Book Borrowing Endpoints
@app.post("/borrow/{book_id}/{member_id}")
def borrow_book(book_id: int, member_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book_service = BookService(book_repo)
    book_service.borrow_book(book_id, member_id)
    return {"message": "Book borrowed successfully"}

@app.post("/return/{book_id}")
def return_book(book_id: int, db: Session = Depends(get_db)):
    book_repo = BookRepository(db)
    book_service = BookService(book_repo)
    book_service.return_book(book_id)
    return {"message": "Book returned successfully"}
