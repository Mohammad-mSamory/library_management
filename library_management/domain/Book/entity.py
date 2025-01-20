from datetime import datetime
from uuid import UUID, uuid4
from typing import Optional
from dataclasses import dataclass


@dataclass
class Book:
    book_id: UUID
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime]
    borrowed_by: Optional[UUID]


