
from sqlalchemy import (
    Table,
    Column,
    String,
    Boolean,
    DateTime,
    UUID,
)

from uuid import uuid4
from library_management.infrastructure.database.engine import metadata, engine


# Book Table
books_table = Table(
    "books",
    metadata,
    Column("book_id", UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column("title", String, nullable=False),
    Column("author", String, nullable=False),
    Column("is_borrowed", Boolean, default=False),
    Column("borrowed_date", DateTime, nullable=True),
    Column("borrowed_by", UUID(as_uuid=True), nullable=True),
)

# Member Table
members_table = Table(
    "members",
    metadata,
    Column("member_id", UUID(as_uuid=True), primary_key=True, default=uuid4),
    Column("name", String, nullable=False),
    Column("email", String, nullable=False, unique=True),
)


metadata.create_all(engine)