
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, UUID
from library_management.infrastructure.database.engine import Base


BookModel = Table(
    'books',
    Base,
    Column('book_id', UUID(as_uuid=True), primary_key=True),
    Column('title',String ),
    Column('author', String),
    Column('is_borrowed', Boolean, default=False),
    Column('borrowed_date', DateTime, nullable=True),
    Column('borrowed_by', Integer, nullable=True)
)

MemberModel = Table(
    'members',
    Base,
    Column('member_id', UUID(as_uuid=True), primary_key=True),
    Column('name',String ),
    Column('email', String),
    
)