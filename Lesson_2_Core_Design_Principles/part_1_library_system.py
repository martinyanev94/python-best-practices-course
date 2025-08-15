class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def print_books(self):
        for book in self.books:
            print(book.title)

class Book:
    def __init__(self, title):
        self.title = title

library = Library()
library.add_book(Book("1984"))
library.add_book(Book("To Kill a Mockingbird"))
library.print_books()
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

class BookPrinter:
    @staticmethod
    def print_books(books):
        for book in books:
            print(book.title)

class Book:
    def __init__(self, title):
        self.title = title

library = Library()
library.add_book(Book("1984"))
library.add_book(Book("To Kill a Mockingbird"))
BookPrinter.print_books(library.books)
