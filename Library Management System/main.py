from library import Library

print("Welcome to Library Management System")

library = Library()

# def addMember():
#     print("Add new Member:")
#     print("Enter Member Details:")
#     print("=================================")

#     name = input("Enter Member Name: ")
#     ## Validate that the name is not empty
#     if not name.strip():
#         print("Member name cannot be empty. Please enter a valid name.")
#         return

#     member_id = input("Enter Member ID: ")
#     ## Validate there is no duplicate Member ID
#     for member in members:
#         if member['id'] == member_id:
#             print("A member with this ID already exists. Please enter a unique ID.")
#             return

#     email = input("Enter Member Email: ")
#     ## Validate that the email is not empty
#     if not email.strip():
#         print("Member email cannot be empty. Please enter a valid email.")
#         return

#     member = {
#         "name": name,
#         "id": member_id,
#         "email": email,
#         "borrowed_books": []
#     }
#     members.append(member)
#     print("Member added successfully!")

# def viewMember():
#     print("View Members:")
#     print("=================================")

#     if len(members) == 0:
#         print("No members available.")
#         return

#     print("Total Members:", len(members))
#     print(f"{'Name':<25} {'ID':<15} {'Email':<30}")
#     print("-"* 70)
#     for member in members:
#         print(f"{member['name']:<25} {member['id']:<15} {member['email']:<30}")

# def findMember(member_id):
#     for member in members:
#         if member['id'] == member_id:
#             return member
#     return None

# def viewMemberHistory():
#     member_id = input("Enter Member ID to view history: ")
#     member = findMember(member_id)
#     if not member:
#         print("Member not found. Please check the Member ID.")
#         return

#     print(f"Borrowed Books for Member {member['name']} (ID: {member['id']}):")
#     print("=================================")
#     if len(member['borrowed_books']) == 0:
#         print("No borrowed books.")
#         return

#     print(f"{'Title':<25} {'Author':<20} {'ISBN':<15}")
#     print("-"* 60)
#     for isbn in member['borrowed_books']:
#         for book in books:
#             if book['isbn'] == isbn:
#                 print(f"{book['title']:<25} {book['author']:<20} {book['isbn']:<15}")

# def addBook():
#     print("Add new Book:")
#     print("Enter Book Details:")
#     print("=================================")

#     title = input("Enter Book Title: ")
#     ## Validate that the title is not empty
#     if not title.strip():
#         print("Book title cannot be empty. Please enter a valid title.")
#         return

#     author = input("Enter Book Author: ")
#     ## Validate that the author is not empty
#     if not author.strip():
#         print("Book author cannot be empty. Please enter a valid author.")
#         return

#     isbn = input("Enter Book ISBN: ")
#     ## Validate there is no duplicate ISBN
#     for book in books:
#         if book['isbn'] == isbn:
#             print("A book with this ISBN already exists. Please enter a unique ISBN.")
#             return

#     ##Validate that total copies is a positive integer
#     while True:
#         try:
#             total_copies = int(input("Enter Total Copies: "))
#             if total_copies <=0 :
#                 print("Total Copies must be a positive integer. Please enter a valid number.")
#                 continue
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid integer for Total Copies.")

#     copies_available = total_copies

#     book = {
#         "title": title,
#         "author": author,
#         "isbn": isbn,
#         "total_copies": total_copies,
#         "copies_available": copies_available
#     }
#     books.append(book)
#     print("Book added successfully!")

# def viewBook():
#     print("View Books:")
#     print("=================================")

#     if len(books) == 0:
#         print("No books available.")
#         return

#     print("Total Books:", len(books))
#     print(f"{'Title':<25} {'Author':<20} {'ISBN':<15} {'Total':<8} {'Available':<10}")
#     print("-"* 80)
#     for book in books:
#         print(f"{book['title']:<25} {book['author']:<20} {book['isbn']:<15} {book['total_copies']:<8} {book['copies_available']:<10}")

# def searchBook():
#     print("Search Book")
#     print("=================================")
#     search_book = input("Enter Book Title or Author: ").lower()
#     result = []
#     for book in books:
#         if search_book in book['title'].lower() or search_book in book['author'].lower():
#             result.append(book)
#     if result:
#         print(f"{'Title':<25} {'Author':<20} {'ISBN':<15} {'Total':<8} {'Available':<10}")
#         print("-" * 80)
#         for book in result:
#             print(f"{book['title']:<25} {book['author']:<20} {book['isbn']:<15} {book['total_copies']:<8} {book['copies_available']:<10}")
#     else:
#         print("No matching book found.")

# def issueBook():
#     member_id = input("Enter Member ID: ")
#     member = findMember(member_id)
#     if not member:
#         print("Member not found. Please check the Member ID.")
#         return
#     else:
#         issue_book = input("Enter Book Title or Author to Issue: ").lower()
#         result = []
#         if not issue_book.strip():
#             print("Input cannot be empty. Please enter a valid title or author.")
#             return
#         for book in books:
#             if issue_book in book['title'].lower() or issue_book in book['author'].lower():
#                 result.append(book)
#         if len(result) == 1:
#             book = result[0]
#             if book['copies_available'] > 0:
#                 book['copies_available'] -= 1
#                 member['borrowed_books'].append(book['isbn'])
#                 print(f"Book '{book['title']}' issued successfully!")
#                 return
#             else:
#                 print(f"Book '{book['title']}' is currently not available for issue.")
#                 return
#         elif len(result) > 1:
#             print("Multiple books found. Please specify the ISBN of the book you want to issue:")
#             for book in result:
#                 print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, Available Copies: {book['copies_available']}")
#             isbn = input("Enter ISBN of the book to issue: ")
#             for book in result:
#                 if book['isbn'] == isbn:
#                     if book['copies_available'] > 0:
#                         book['copies_available'] -= 1
#                         member['borrowed_books'].append(book['isbn'])
#                         print(f"Book '{book['title']}' issued successfully!")
#                         return
#                     else:
#                         print(f"Book '{book['title']}' is currently not available for issue.")
#                     return
#         print("Book not found or not available.")

# def returnBook():
#     member_id = input("Enter Member ID: ")
#     member = findMember(member_id)
#     if not member:
#         print("Member not found. Please check the Member ID.")
#         return
#     return_book = input("Enter Book Title or Author to Return: ").lower()
#     if not return_book.strip():
#         print("Input cannot be empty. Please enter a valid title or author.")
#         return
#     for book in books:
#         if return_book in book['title'].lower() or return_book in book['author'].lower():
#             if book['isbn'] not in member['borrowed_books']:
#                 print(f"Book '{book['title']}' was not borrowed by this member.")
#                 return
#             book['copies_available'] += 1
#             member['borrowed_books'].remove(book['isbn'])
#             print(f"Book '{book['title']}' returned successfully!")
#             return
#     print("Book not found.")


while(True):
    print("\nLibrary Management System Menu:")
    print("=================================")
    print("1. Add Member")
    print("2. View Members")
    print("3. View Member History")
    print("4. Add Book")
    print("5. View Books")
    print("6. Search Book")
    print("7. Issue Book")
    print("8. Return Book")
    print("9. Exit")
    while True:
        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            break
        else:
            print("Invalid input. Please try again.")

    match choice:

        case 1: 
            print(" Add Member Selected")
            library.add_Member(input("Enter Member Name: "), input("Enter Member ID: "), input("Enter Member Email: "))
        case 2: 
            print(" View Members Selected")       
            library.view_Member()
        case 3: 
            print(" View Member History Selected")
            library.view_Member_History(input("Enter Member ID: "))
        case 4:
            print(" Add Book Selected")
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            isbn = input("Enter Book ISBN: ")
            while True:
                total_copies = input("Enter Total Copies: ")
                if total_copies.isdigit() and int(total_copies) > 0:
                    total_copies = int(total_copies)
                    break
                else:
                    print("Invalid input. Please enter a positive integer for Total Copies.")
            library.add_Book(title, author, isbn, total_copies)
        case 5:
            print(" View Books Selected")
            library.view_Books()
        case 6:
            print(" Search Book Selected")
            library.search_Book(input("Enter search keyword: "))
        case 7:
            print(" Issue Book Selected")
            library.issue_Book(input("Enter Member ID: "), input("Enter Book Title or Author to Issue: "))
        case 8:
            print(" Return Book Selected")
            library.return_Book(input("Enter Member ID: "), input("Enter Book ISBN to Return: "))
        case 9:
            print(" Exiting...")
            exit()
        
        case _:
            print(" Invalid Choice")
          