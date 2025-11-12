A simple Python application that manages a library's book catalog using Object-Oriented Programming (OOP) principles.
Originally implemented in Java, this version has been re-implemented in Python using dataclasses for cleaner, more readable code.

✨ Features

Add Books – Add new books to the library catalog

Remove Books – Remove books from the catalog by their ISBN

Search Books – Search for books by their title (case-insensitive)

List Books – Display all books currently in the catalog

🏗️ Class Overview
🧾 Book Class

Represents a book in the library.

Attributes

title – The title of the book

author – The author of the book

ISBN – The ISBN number of the book

publisher – The publisher of the book

year – The year the book was published

Methods

__str__() – Returns a string representation of the book’s details

🏛️ Library Class

Manages a collection of Book objects.

Methods

add_book(book) – Adds a new book to the library

remove_book(ISBN) – Removes a book using its ISBN

search_book_by_title(title) – Searches for a book by title (case-insensitive)

list_books() – Lists all books in the library

▶️ main.py

Demonstrates the functionality of the Library and Book classes.

💻 Example Usage
from library import Library
from book import Book

library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Scribner", 1925)
book2 = Book("1984", "George Orwell", "9780451524935", "Signet Classic", 1949)

library.add_book(book1)
library.add_book(book2)

print("\nAll books in library:")
library.list_books()

print("\nSearching for '1984':")
print(library.search_book_by_title("1984"))

print("\nRemoving '1984' by ISBN:")
library.remove_book("9780451524935")

print("\nAll books after removal:")
library.list_books()

⚙️ How to Run

Clone this repository:

git clone https://github.com/<your-username>/Library-Book-Catalog.git
cd Library-Book-Catalog


(Optional) Create a virtual environment:

python -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows


Run the main file:

python main.py

🧪 Testing (optional)

If you use pytest for testing:

pip install pytest
pytest -q
