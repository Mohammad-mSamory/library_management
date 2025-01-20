from datetime import datetime


class BookService:
    def __init__(self, book_repo):
        self.book_repo = book_repo

    def borrow_book(self, book_id: int, member_id: int):
        book = self.book_repo.get(book_id)
        if not book or book.is_borrowed:
            raise ValueError("Book not available for borrowing.")
        book.is_borrowed = True
        book.borrowed_date = datetime.now()
        book.borrowed_by = member_id
        self.book_repo.update(book)

    def return_book(self, book_id: int):
        book = self.book_repo.get(book_id)
        if not book or not book.is_borrowed:
            raise ValueError("Book is not borrowed.")
        book.is_borrowed = False
        book.borrowed_date = None
        book.borrowed_by = None
        self.book_repo.update(book)
