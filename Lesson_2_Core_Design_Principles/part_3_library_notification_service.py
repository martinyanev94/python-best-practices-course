class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Library:
    def __init__(self):
        self.books = []
        self.email_service = EmailService()

    def add_book(self, book):
        self.books.append(book)
        self.email_service.send_email(f"New book added: {book.title}")

class Book:
    def __init__(self, title):
        self.title = title

library = Library()
library.add_book(Book("1984"))
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class EmailService(NotificationService):
    def notify(self, message):
        print(f"Sending email: {message}")

class SMSService(NotificationService):
    def notify(self, message):
        print(f"Sending SMS: {message}")

class Library:
    def __init__(self, notification_service: NotificationService):
        self.books = []
        self.notification_service = notification_service

    def add_book(self, book):
        self.books.append(book)
        self.notification_service.notify(f"New book added: {book.title}")

library = Library(EmailService())
library.add_book(Book("1984"))
