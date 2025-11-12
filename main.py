from library import Library
from book import Book

def main():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Scribner", 1925)
    book2 = Book("1984", "George Orwell", "9780451524935", "Signet Classic", 1949)

    library.add_book(book1)
    library.add_book(book2)

    print("\nListing all books in the library:")
    library.list_books()

    print("\nSearching for '1984':")
    searched_book = library.search_book_by_title("1984")
    if searched_book is not None:
        print("Book found:", searched_book)
    else:
        print("Book not found.")

    print("\nRemoving '1984' by ISBN:")
    library.remove_book("9780451524935")

    print("\nListing all books in the library after removal:")
    library.list_books()

if __name__ == "__main__":
    main()
