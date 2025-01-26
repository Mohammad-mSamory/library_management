
from datetime import datetime

from pydantic import UUID4, BaseModel, EmailStr


# Pydantic Models for Book
class BookBase(BaseModel):
    title: str
    author: str
    is_borrowed: bool = False
    borrowed_date: datetime | None = None
    borrowed_by: UUID4 | None = None


class BookCreate(BookBase):
    title: str
    author: str


class BookUpdate(BookBase):
    is_borrowed: bool = False
    borrowed_date: datetime | None = None
    borrowed_by: UUID4 | None = None


class Book(BookBase):
    book_id: UUID4


# Pydantic Models for Member
class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    name: str
    email: EmailStr


class MemberUpdate(MemberBase):
    name: str
    email: EmailStr


class Member(MemberBase):
    member_id: UUID4
