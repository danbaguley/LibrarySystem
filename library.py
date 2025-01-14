
from book import Book 
from member import Member

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.available == True:
            book.available = False
            member.borrowed_books.append(book)
            print(f"{book.title} has been lent to {member.name}")
        else:
            print(f"Sorry, {book.title} is not available for lending")

    def display_books(self): 
        for book in self.books: 
            if book.available == True:
                status = 'Available' 
            else:
                status = 'Not available' 
            print(f"{book.title} by {book.author} - {status}")

    def display_members(self): 
        for member in self.members: 
           print(f"Name: {member.name}, ID: {member.member_id}")  

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{member.name} did not borrow {book.title}")


library = Library()

book_1 = Book("A Game of Thrones", "George RR Martin", True)
book_2 = Book("The Winds of Winter", "George RR Martin", True)

member_1 = Member(1, "Dan")
member_2 = Member(2, "John")



library.add_book(book_1)
library.add_book(book_2)

#library.display_books()

library.add_member(member_1)
library.add_member(member_2)

library.display_members()


library.lend_book(book_1, member_1)

#library.display_books()

library.return_book(book_1, member_1)

#library.display_books()