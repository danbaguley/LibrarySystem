from library import Library
from book import Book 
from member import Member

class LibrarySystem:
    def __init__(self):
        self.library = Library()


    def library_menu(self):

        running = True

        while running == True:
            print("Welcome to the library system.")
            print("------------------------------")
            print("1 - Add a new book")
            print("2 - Lend a book to a member")
            print("3 - Mark a book as returned")
            print("4 - Register a new member")
            print("9 - Exit program")
            print("------------------------------")
            user_input = input("Please select an option from above: ")

            user_int = int(user_input)

            if user_int == 1: 
                print("Add book")
            elif user_int == 2: 
                print("Lend book") 
            elif user_int == 3: 
                print("Mark book as returned") 
            elif user_int == 4: 
                print("Register member")
            elif user_int == 9:
                running = False
                print("Exiting program")
            else:
                print("Invalid Input")
        

    #Func to test whether things work un comment in execute function to use, make sure you comment out the library menu function if you want to use this
    def library_test(self): 
        book_1 = Book("A Game of Thrones", "George RR Martin", True) 
        book_2 = Book("The Winds of Winter", "George RR Martin", True) 
        
        member_1 = Member(1, "Dan") 
        member_2 = Member(2, "John") 
        
        self.library.add_book(book_1) 
        self.library.add_book(book_2) 
        self.library.add_member(member_1) 
        self.library.add_member(member_2)

        self.library.lend_book(book_1, member_1)

        self.library.display_books()

        self.library.return_book(book_1, member_1)

        self.library.display_books()

        self.library.display_members()

    def execute(self):
        self.library_menu()
        #self.library_test()
    


