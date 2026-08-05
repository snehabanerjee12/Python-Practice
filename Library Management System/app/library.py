from book_repository import BookRepository
from member_repository import MemberRepository

from books import Book
from members import Member


class Library:
    def __init__(self):
        self.book_repo = BookRepository()
        self.member_repo = MemberRepository()

    def add_Book(self, title, author, isbn, total_copies):
        if not title.strip():
            print("Book title cannot be empty. Please enter a valid title.")
            return
        if not author.strip():
            print("Book author cannot be empty. Please enter a valid author.")
            return
        if self.book_repo.find_book_by_isbn(isbn):
            print("A book with this ISBN already exists. Please enter a unique ISBN.")
            return
        
        if total_copies <= 0:
            print("Total Copies must be a positive integer. Please enter a valid number.")
            return
        
        book = Book(title, author, isbn, total_copies)
        self.book_repo.add_book(book)
        print("Book added successfully!")


    def view_Books(self):
        books = self.book_repo.get_all_books()
        if not books:
            print("No books available.")
            return
        print(f"{'Title':<25} {'Author':<20} {'ISBN':<15} {'Total':<8} {'Available':<10}")
        print("-"* 80)
        for book in books:
            print(book)

    def search_Book(self, keyword):
        key = keyword.lower()
        found_books = [book for book in self.book_repo.get_all_books() if key in book.title.lower() or key in book.author.lower()]
        if not found_books:
            print("No books found.")
            return
        for book in found_books:
            print(book)

    def issue_Book(self, member_id, keyword):
        member = self.member_repo.find_member_by_id(member_id)
        if member is None:
            print("Member not found.")
            return

        keyword = keyword.lower()
        results = [b for b in self.book_repo.get_all_books() if keyword in b.title.lower() or keyword in b.author.lower()]

        if not results:
            print("No matching book found.")
            return

        if len(results) == 1:
            selected_book = results[0]
        else:
            print("Multiple books found:")
            for i, book in enumerate(results, start=1):
                print(f"{i}. {book}")
            choice = input(f"Enter the number of the book to issue (1-{len(results)}): ")
            if not choice.isdigit() or not (1 <= int(choice) <= len(results)):
                print("Invalid choice.")
                return
            selected_book = results[int(choice) - 1]

        if selected_book.copies_available <= 0:
            print(f"'{selected_book.title}' is currently not available.")
            return

        selected_book.copies_available -= 1
        member.borrowed_books.append(selected_book.isbn)
        print(f"'{selected_book.title}' issued to {member.name} successfully!")

    def return_Book(self, member_id, isbn):
        member = self.member_repo.find_member_by_id(member_id)
        if member is None:
            print("Member not found.")
            return
        if not isbn.strip():
            print("ISBN cannot be empty. Please enter a valid ISBN.")
            return
        
        if isbn not in member.borrowed_books:
            print("This book was not borrowed by the member.")
            return
        
        book = self.book_repo.find_book_by_isbn(isbn)
        if book is None:
            print("Book record not found (data inconsistency).")
            return
        
        member.borrowed_books.remove(isbn)
        book.copies_available += 1
        print(f"'{book.title}' returned successfully by {member.name}.")

    def add_Member(self, name, id, email):
        if not name.strip():
            print("Member name cannot be empty. Please enter a valid name.")
            return
        if not email.strip():
            print("Member email cannot be empty. Please enter a valid email.")
            return
        
        member = self.member_repo.find_member_by_id(id)
        if member:
            print("A member with this ID already exists. Please enter a unique ID.")
            return
        
        member = Member(name, id, email)
        self.member_repo.add_member(member)
        print("Member added successfully!")
    
    def view_Member(self):
        members = self.member_repo.get_all_members()
        if not members:
            print("No members available.")
            return
        for member in members:
          print(f"Name: {member.name}, ID: {member.id}, Email: {member.email}")

    def find_Member(self, id):
        return self.member_repo.find_member_by_id(id)

    def view_Member_History(self, id):
        member = self.member_repo.find_member_by_id(id)
        if not member:
            print("Member not found.")
            return
        if not member.borrowed_books:
            print("No borrowed books found.")
            return
        print(f"Books borrowed by {member.name}:")
        for isbn in member.borrowed_books:
            book = self.book_repo.find_book_by_isbn(isbn)
            if book:
                print(f"- {book.title} by {book.author}")
