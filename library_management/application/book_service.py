from datetime import date
from uuid import UUID
from library_management.domain.Book.entity import BookID



class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def borrow_book(self, book_id: BookID, member_id: UUID):
        book = self.book_repository.get(book_id)
        if book.is_borrowed:
            raise ValueError("Book is already borrowed")
        book.is_borrowed = True
        book.borrowed_date = date.today()
        book.borrowed_by = member_id
        self.book_repository.update(book)

    def return_book(self, book_id: BookID):
        book = self.book_repository.get(book_id)
        if not book.is_borrowed:
            raise ValueError("Book is not borrowed")
        book.is_borrowed = False
        book.borrowed_date = None
        book.borrowed_by = None
        self.book_repository.update(book)


# Use Cases
class BorrowBookUseCase:
    def __init__(self, book_service: BookService):
        self.book_service = book_service

    def execute(self, book_id: BookID, member_id: UUID):
        self.book_service.borrow_book(book_id, member_id)


class ReturnBookUseCase:
    def __init__(self, book_service: BookService):
        self.book_service = book_service

    def execute(self, book_id: BookID):
        self.book_service.return_book(book_id)