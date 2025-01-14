from library import Library
from book import Book 
from member import Member

class LibrarySystem:
    def __init__(self):
        self.library = Library()


    def setup_library(self): 
        book_1 = Book("A Game of Thrones", "George RR Martin", True) 
        book_2 = Book("The Winds of Winter", "George RR Martin", True) 
        
        member_1 = Member(1, "Dan") 
        member_2 = Member(2, "John") 
        
        self.library.add_book(book_1) 
        self.library.add_book(book_2) 
        self.library.add_member(member_1) 
        self.library.add_member(member_2)

    def execute(self):
        self.setup_library()
        self.library.display_books()
        self.library.display_members()


if __name__ == "__main__":
    library_system = LibrarySystem()
    library_system.execute()