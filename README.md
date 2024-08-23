# Library Book Catalog

A simple Java application that manages a library's book catalog using Object-Oriented Programming (OOP) principles.

## Features

- **Add Books**: Add new books to the library catalog.
- **Remove Books**: Remove books from the catalog by their ISBN.
- **Search Books**: Search for books by their title.
- **List Books**: Display a list of all books currently in the catalog.

## Class Overview

### Book Class
Represents a book in the library.

**Attributes:**
- `title`: The title of the book.
- `author`: The author of the book.
- `ISBN`: The ISBN number of the book.
- `publisher`: The publisher of the book.
- `yearPublished`: The year the book was published.
- `isAvailable`: Availability status of the book.

**Methods:**
- `getTitle()`, `getAuthor()`, `getISBN()`, `getPublisher()`, `getYearPublished()`: Return corresponding attributes.
- `isAvailable()`: Returns whether the book is available or not.
- `setAvailable(boolean available)`: Sets the availability status of the book.
- `toString()`: Returns a string representation of the book's details.

### Library Class
Manages a collection of `Book` objects.

**Methods:**
- `addBook(Book book)`: Adds a new book to the library.
- `removeBook(String ISBN)`: Removes a book from the library using its ISBN.
- `searchBookByTitle(String title)`: Searches for a book by its title.
- `listBooks()`: Lists all books in the library.

### Main Class
Demonstrates the functionality of the `Library` and `Book` classes.

**Methods:**
- `main(String[] args)`: The entry point of the application, where books are added, searched, removed, and listed.

## Example Usage

```java
Library library = new Library();

Book book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Scribner", 1925);
Book book2 = new Book("1984", "George Orwell", "9780451524935", "Signet Classic", 1949);

library.addBook(book1);
library.addBook(book2);

library.listBooks();

library.searchBookByTitle("1984");

library.removeBook("9780451524935");

library.listBooks();
