class Book:
    def __init__(self, title, author, isbn, total_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.total_copies = total_copies
        self.copies_available = total_copies

    def __str__(self):  # pythons built-in method to return a string representation of the object
        return f"{self.title:<25} {self.author:<20} {self.isbn:<15} {self.total_copies:<8} {self.copies_available:<10}"

