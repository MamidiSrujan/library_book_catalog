public class Book {
    private String title;
    private String author;
    private String ISBN;
    private String publisher;
    private int year;

    public Book(String title, String author, String ISBN, String publisher, int year) {
        this.title = title;
        this.author = author;
        this.ISBN = ISBN;
        this.publisher = publisher;
        this.year = year;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public String getISBN() {
        return ISBN;
    }

    public String getPublisher() {
        return publisher;
    }

    public int getYear() {
        return year;
    }

    @Override
    public String toString() {
        return title + " by " + author + " (" + year + ") - ISBN: " + ISBN;
    }
}
