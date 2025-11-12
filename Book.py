from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    ISBN: str
    publisher: str
    year: int

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year}) - ISBN: {self.ISBN}"
