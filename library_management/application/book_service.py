from datetime import datetime

from library_management.infrastructure.repositories.Base_repository import \
    BookRepository


class BookService:
    def __init__(self, book_repo: BookRepository):
        self.book_repo = book_repo

    def add_book(self, book_data: dict):
        return self.book_repo.add(book_data)

    def get_book(self, book_id: int):
        return self.book_repo.get(book_id)

    def list_books(self):
        return self.book_repo.list()

    def update_book(self, book_id: int, book_data: dict):
        return self.book_repo.update(book_id, book_data)

    def delete_book(self, book_id: int):
        return self.book_repo.delete(book_id)

    def borrow_book(self, book_id: int, member_id: int):
        book = self.book_repo.get(book_id)
        if book["is_borrowed"]:
            raise ValueError("Book is already borrowed")
        book["is_borrowed"] = True
        book["borrowed_date"] = datetime.utcnow()
        book["borrowed_by"] = member_id
        return self.book_repo.update(book_id, book)

    def return_book(self, book_id: int):
        book = self.book_repo.get(book_id)
        if not book["is_borrowed"]:
            raise ValueError("Book is not currently borrowed")
        book["is_borrowed"] = False
        book["borrowed_date"] = None
        book["borrowed_by"] = None
        return self.book_repo.update(book_id, book)
