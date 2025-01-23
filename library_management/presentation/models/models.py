
from typing import Optional

from pydantic import UUID4, BaseModel, EmailStr


# Pydantic Models for Book
class BookBase(BaseModel):
    title: str
    author: str
    is_borrowed: bool = False
    borrowed_date: Optional[str] = None
    borrowed_by: Optional[UUID4] = None


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    book_id: UUID4


# Pydantic Models for Member
class MemberBase(BaseModel):
    name: str
    email: EmailStr


class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    pass


class Member(MemberBase):
    member_id: UUID4
