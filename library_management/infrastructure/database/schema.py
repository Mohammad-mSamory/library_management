
from sqlalchemy import Column, Integer, String, Boolean, DateTime, UUID

from uuid import uuid4
from library_management.infrastructure.database.engine import Base


class BookModel(Base):
    __tablename__ = 'books'

    book_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    is_borrowed = Column(Boolean, default=False)
    borrowed_date = Column(DateTime, nullable=True)
    borrowed_by = Column(UUID(as_uuid=True), nullable=True)

# Member Model
class MemberModel(Base):
    __tablename__ = 'members'

    member_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)