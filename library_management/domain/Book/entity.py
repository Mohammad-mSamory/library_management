from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from library_management.domain.shared.base_entity import BaseEntity

@dataclass
class Book(BaseEntity):
    book_id: UUID
    title: str
    author: str
    is_borrowed: bool
    borrowed_date: datetime
    borrowed_by: UUID
