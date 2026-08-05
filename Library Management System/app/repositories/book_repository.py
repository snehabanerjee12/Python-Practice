from books import Book

class BookRepository:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        
    def get_all_books(self):
        return self.books
    
    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def delete_book(self, isbn):
        book = self.find_book_by_isbn(isbn)
        if book:
            self.books.remove(book)
            return True
        return False

