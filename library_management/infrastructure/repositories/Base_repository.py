from uuid import UUID
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import SQLAlchemyError

from library_management.infrastructure.database.engine import engine


class DatabaseError(Exception):
    """Custom exception for database-related errors."""
    def __init__(self, message="An error occurred with the database operation"):
        self.message = message
        super().__init__(self.message)


class BaseRepository:
    def __init__(self, table, entity_type, pk_column):
        self.table = table
        self.entity_type = entity_type
        self.pk_column = pk_column  # "book_id" or "member_id"

    def _convert_to_entity(self, data):
        if not data:
            return None
        return self.entity_type.from_dict(data._asdict())

    def add(self, entity):
        try:
            with engine.connect() as conn:
                stmt = insert(self.table).values(**entity.to_dict())
                conn.execute(stmt)
                conn.commit()
            return entity
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to add entity: {e}")

    def get(self, entity_id: UUID):
        try:
            with engine.connect() as conn:
                stmt = select(self.table).where(
                    getattr(self.table.c, self.pk_column) == entity_id
                )
                result = conn.execute(stmt)
                return self._convert_to_entity(result.fetchone())
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to retrieve entity with ID {entity_id}: {e}")

    def list_all(self):
        try:
            with engine.connect() as conn:
                result = conn.execute(select(self.table))
                return [self._convert_to_entity(row) for row in result]
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to list all entities: {e}")

    def update(self, entity):
        try:
            with engine.connect() as conn:
                stmt = (
                    update(self.table)
                    .where(
                        getattr(self.table.c, self.pk_column) ==
                        getattr(entity, self.pk_column)
                    )
                    .values(entity.to_dict())
                )
                conn.execute(stmt)
                conn.commit()
            return entity
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to update entity: {e}")

    def delete(self, entity_id: UUID):
        try:
            with engine.connect() as conn:
                stmt = delete(self.table).where(
                    getattr(self.table.c, self.pk_column) == entity_id
                )
                conn.execute(stmt)
                conn.commit()
        except SQLAlchemyError as e:
            raise DatabaseError(f"Failed to delete entity with ID {entity_id}: {e}")


class BookRepository(BaseRepository):
    def __init__(self):
        from library_management.domain.Book.entity import Book
        from library_management.infrastructure.database.schema import books_table
        super().__init__(
            table=books_table,
            entity_type=Book,
            pk_column="book_id"
        )


class MemberRepository(BaseRepository):
    def __init__(self):
        from library_management.domain.Member.entity import Member
        from library_management.infrastructure.database.schema import members_table
        super().__init__(
            table=members_table,
            entity_type=Member,
            pk_column="member_id"
        )
