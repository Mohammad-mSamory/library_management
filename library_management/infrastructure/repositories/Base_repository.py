from uuid import UUID
from sqlalchemy import delete, insert, select, update
from library_management.infrastructure.database.engine import engine


class BaseRepository:
    def __init__(self, table, entity_type, pk_column):
        self.table = table
        self.entity_type = entity_type
        self.pk_column = pk_column  # "book_id" or "member_id"

    def _convert_to_entity(self, data):
        return self.entity_type.from_dict(dict(data)) if data else None
    
    def add(self, entity):
        with engine.connect() as conn:
            stmt = insert(self.table).values(**entity.to_dict())
            conn.execute(stmt)
            conn.commit()  
        return entity  

    def get(self, entity_id: UUID):
        with self.engine.connect() as conn:
            stmt = select(self.table).where(
                getattr(self.table.c, self.pk_column) == entity_id
            )
            result = conn.execute(stmt)
            return self._convert_to_entity(result.fetchone())

 
    def list_all(self):
        with engine.connect() as conn:
            result = conn.execute(select(self.table))
            return [self._convert_to_entity(row) for row in result]

    def update(self, entity):
        with engine.connect() as conn:
            stmt = (
                update(self.table)
                .where(self.table.c.book_id == entity.book_id)
                .values(entity.to_dict())
            )
            conn.execute(stmt)
            return entity

    def delete(self, entity_id: UUID):
        with engine.connect() as conn:
            stmt = delete(self.table).where(self.table.c.book_id == entity_id)
            conn.execute(stmt)

class BookRepository(BaseRepository):
    def __init__(self):
        from library_management.infrastructure.database.schema import books_table
        from library_management.domain.Book.entity import Book
        super().__init__(
            table=books_table,
            entity_type=Book,
            pk_column="book_id"  
        )

class MemberRepository(BaseRepository):
    def __init__(self):
        from library_management.infrastructure.database.schema import members_table
        from library_management.domain.Member.entity import Member
        super().__init__(
            table=members_table,
            entity_type=Member,
            pk_column="member_id"  
        )