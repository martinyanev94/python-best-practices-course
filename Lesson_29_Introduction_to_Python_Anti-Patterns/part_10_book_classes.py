class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

b = Book("Title", "Author")
print(b._title)
class BetterBook:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

b = BetterBook("Title", "Author")
print(b.get_title())
