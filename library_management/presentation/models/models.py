
from typing import Optional
from pydantic import BaseModel, EmailStr



# Pydantic Models for Validation
class BookIn(BaseModel):
    title: str
    author: str

class BookOut(BookIn):
    book_id: int
    is_borrowed: bool
    borrowed_date: Optional[str]
    borrowed_by: Optional[int]

class MemberIn(BaseModel):
    name: str
    email: EmailStr

class MemberOut(MemberIn):
    member_id: int
