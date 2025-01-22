from sqlalchemy import Table, insert, select, update, delete
from library_management.infrastructure.database.engine import engine
from library_management.infrastructure.database.schema import books_table , members_table


class BookRepository:
    def add(self, book_data: dict):
        with engine.connect() as conn:
            stmt = insert(books_table).values(book_data).returning(books_table)
            return conn.execute(stmt).fetchone()

    def get(self, book_id: int):
        with engine.connect() as conn:
            stmt = select(books_table).where(books_table.c.book_id == book_id)
            return conn.execute(stmt).fetchone()

    def list(self):
        with engine.connect() as conn:
            stmt = select(books_table)
            return conn.execute(stmt).fetchall()

    def update(self, book_id: int, book_data: dict):
        with engine.connect() as conn:
            stmt = update(books_table).where(books_table.c.book_id == book_id).values(book_data)
            conn.execute(stmt)

    def delete(self, book_id: int):
        with engine.connect() as conn:
            stmt = delete(books_table).where(books_table.c.book_id == book_id)
            conn.execute(stmt)


class MemberRepository:
    def add(self, member_data: dict):
        with engine.connect() as conn:
            stmt = insert(members_table).values(member_data).returning(members_table)
            return conn.execute(stmt).fetchone()

    def get(self, member_id: int):
        with engine.connect() as conn:
            stmt = select(members_table).where(members_table.c.member_id == member_id)
            return conn.execute(stmt).fetchone()

    def list(self):
        with engine.connect() as conn:
            stmt = select(members_table)
            return conn.execute(stmt).fetchall()

    def update(self, member_id: int, member_data: dict):
        with engine.connect() as conn:
            stmt = update(members_table).where(members_table.c.member_id == member_id).values(member_data)
            conn.execute(stmt)

    def delete(self, member_id: int):
        with engine.connect() as conn:
            stmt = delete(members_table).where(members_table.c.member_id == member_id)
            conn.execute(stmt)
