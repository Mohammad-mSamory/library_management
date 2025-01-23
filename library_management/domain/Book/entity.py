from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class Book:
    book_id: UUID
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: Optional[datetime]
    borrowed_by: Optional[UUID]
