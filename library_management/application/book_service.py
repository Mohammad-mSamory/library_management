from datetime import datetime,timezone
from uuid import UUID, uuid4


from library_management.domain.Book.entity import Book
from library_management.infrastructure.repositories.Base_repository import BookRepository

class BookService:
    def __init__(self, repository):
        self.repo = repository
    def add_book(self, data: dict) -> Book:
        is_borrowed = data.get("is_borrowed", False)
        
        # Validate borrowed fields only if the book is marked as borrowed
        if is_borrowed:
            borrowed_date = data.get("borrowed_date", datetime.now(timezone.utc))
            borrowed_by = data.get("borrowed_by")
            if not borrowed_by:
                raise ValueError("borrowed_by is required when is_borrowed is True")
        else:
            borrowed_date = None
            borrowed_by = None

        new_book = Book(
            book_id=uuid4(),
            title=data["title"],
            author=data["author"],
            is_borrowed=is_borrowed, 
            borrowed_date=borrowed_date,  
            borrowed_by=borrowed_by  
        )
        return self.repo.add(new_book)

    def update_book(self, book_id: UUID, data: dict) -> Book:
       
        book = self.repo.get(book_id)
        if not book:
            raise ValueError("Book not found")
        
       
        if "title" in data: book.title = data["title"]
        if "author" in data: book.author = data["author"]
        
        return self.repo.update(book)

    
    def borrow_book(self, book_id: UUID, member_id: UUID) -> Book:
        book = self.repo.get(book_id)
        if not book:
            raise ValueError("Book not found")
        
        if book.is_borrowed:
            raise ValueError("Book already borrowed")
        
        book.is_borrowed = True
        book.borrowed_date = datetime.now(timezone.utc)
        book.borrowed_by = member_id
        return self.repo.update(book)

    def return_book(self, book_id: UUID) -> Book:
        book = self.repo.get(book_id)
        if not book:
            raise ValueError("Book not found")
        
        book.is_borrowed = False
        book.borrowed_date = None
        book.borrowed_by = None
        return self.repo.update(book)
    
    def get_book(self, book_id: UUID) -> Book:
        book = self.repo.get(book_id)
        if not book:
            raise ValueError("Book not found")
        return book

    def list_books(self) -> list[Book]:
        return self.repo.list_all()

    def delete_book(self, book_id: UUID) -> None:
        if not self.repo.get(book_id):
            raise ValueError("Book not found")
        self.repo.delete(book_id)