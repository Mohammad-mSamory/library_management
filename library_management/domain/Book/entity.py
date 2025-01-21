from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from dataclasses import dataclass



@dataclass
class BookID:
    id: UUID

    @staticmethod
    def create():
        return BookID(id=uuid4())


@dataclass
class Book:
    book_id: BookID
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime]
    borrowed_by: Optional[UUID]

