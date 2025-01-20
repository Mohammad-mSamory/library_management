
from typing import List,Optional
from sqlalchemy.orm import Session
from sqlalchemy import UUID

from library_management.infrastructure.database.schema import BookModel, MemberModel


# Repositories (Infrastructure Layer)
class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, book: BookModel):
        self.db.add(book)
        self.db.commit()

    def get(self, book_id: int) -> Optional[BookModel]:
        return self.db.query(BookModel).filter(BookModel.book_id == book_id).first()

    def list(self) -> List[BookModel]:
        return self.db.query(BookModel).all()

    def delete(self, book_id: int):
        book = self.get(book_id)
        if book:
            self.db.delete(book)
            self.db.commit()

    def update(self, book: BookModel):
        self.db.commit()

class MemberRepository:
    def __init__(self, db: Session):
        self.db = db

    def add(self, member: MemberModel):
        self.db.add(member)
        self.db.commit()

    def get(self, member_id: int) -> Optional[MemberModel]:
        return self.db.query(MemberModel).filter(MemberModel.member_id == member_id).first()

    def list(self) -> List[MemberModel]:
        return self.db.query(MemberModel).all()

    def delete(self, member_id: int):
        member = self.get(member_id)
        if member:
            self.db.delete(member)
            self.db.commit()

    def update(self, member: MemberModel):
        self.db.commit()
