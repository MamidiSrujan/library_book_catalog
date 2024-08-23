public class Main {
    public static void main(String[] args) {
        Library library = new Library();

        Book book1 = new Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "Scribner", 1925);
        Book book2 = new Book("1984", "George Orwell", "9780451524935", "Signet Classic", 1949);

        library.addBook(book1);
        library.addBook(book2);

        System.out.println("\nListing all books in the library:");
        library.listBooks();

        System.out.println("\nSearching for '1984':");
        Book searchedBook = library.searchBookByTitle("1984");
        if (searchedBook != null) {
            System.out.println("Book found: " + searchedBook);
        } else {
            System.out.println("Book not found.");
        }

        System.out.println("\nRemoving '1984' by ISBN:");
        library.removeBook("9780451524935");

        System.out.println("\nListing all books in the library after removal:");
        library.listBooks();
    }
}
