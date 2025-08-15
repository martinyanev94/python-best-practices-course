class BookCache:
    def __init__(self):
        self.cache = {}
    
    def get_book(self, book_id):
        if book_id in self.cache:
            print(f"Fetching {book_id} from cache.")
            return self.cache[book_id]
        
        print(f"{book_id} not found in cache. Fetching from database...")
        book = self.fetch_book_from_db(book_id)
        self.cache[book_id] = book
        return book

    def fetch_book_from_db(self, book_id):
        # Simulate a database call
        time.sleep(2)
        return f"Book data for {book_id}"

book_cache = BookCache()
print(book_cache.get_book(1))  # Fetches from database
print(book_cache.get_book(1))  # Fetches from cache
