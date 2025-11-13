from typing import List, Optional
from Book import Book

class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        print("Book added:", book.title)

    def remove_book(self, ISBN: str) -> None:
        book_to_remove: Optional[Book] = None
        for book in self.books:
            if book.ISBN == ISBN:
                book_to_remove = book
                break
        if book_to_remove is not None:
            self.books.remove(book_to_remove)
            print("Book removed:", book_to_remove.title)
        else:
            print("Book not found.")

    def search_book_by_title(self, title: str) -> Optional[Book]:
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def list_books(self) -> None:
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

