class Book:
    def __init__(self, title, author, avaliable):
        self.title = title
        self.author = author
        self.avaliable = avaliable


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        book.avaliabe = True
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def lend_book(self, book, member):
        if book.avaliable == True:
            book.avaliable = False
            member.borrowed_books.append(book)
            print(f"{book.title} has been lent to {member.name}")
        else:
            print(f"Sorry, {book.title} is not available for lending")

    def display_books(self): 
        for book in self.books: 
            status = 'Available' if book.available else 'Not available' 
            print(f"{book.title} by {book.author} - {status}")

    def return_book(self, book, member):
        if book in member.borrowed_books:
            book.available = True
            member.borrowed_books.remove(book)
            print(f"{book.title} has been returned by {member.name}")
        else:
            print(f"{member.name} did not borrow {book.title}")


library = Library()

book_1 = Book("A Game of Thrones", "George RR Martin")
book_2 = Book("The Winds of Winter", "George RR Martin")

member_1 = Member(1, "Dan")
member_2 = Member(2, "John")

library.add_book(book_1)
library.add_book(book_2)


library.add_member(member_1)
library.add_member(member_2)

library.lend_book(book_1, member_1)