from library import Library
from book import Book 
from member import Member

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