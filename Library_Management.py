class Library:
    def __init__(self, books):
        self.books = books  # Dictionary {book_name: "Free"/borrower_name}

    def show_avail_books(self):
        print("\nOur Library Can Offer You The Following Books:")
        print("================================================")
        available = False
        for book, borrower in self.books.items():
            if borrower == "Free":
                print(book)
                available = True
        if not available:
            print("No books available right now.")

    def lend_book(self, requested_book, name):
        if requested_book not in self.books:
            print(f"Sorry, {requested_book} is not in our library.")
            return False

        if self.books[requested_book] == "Free":
            print(f"{requested_book} has been marked as 'Borrowed' by {name}")
            self.books[requested_book] = name
            return True
        else:
            print(
                f"Sorry, {requested_book} is currently on loan to {self.books[requested_book]}"
            )
            return False

    def return_book(self, returned_book):
        if returned_book not in self.books:
            print(f"{returned_book} is not from our library.")
            return False
        self.books[returned_book] = "Free"
        return True # Successfully returned


class Student:
    def __init__(self, name, library):
        self.name = name
        self.books = []  # list of borrowed books
        self.library = library

    def view_borrowed(self):
        if not self.books:
            print(f"\n{self.name}, you haven't borrowed any books yet.")
        else:
            print(f"\nBooks borrowed by {self.name}:")
            for book in self.books:
                print(book)

    def request_book(self):
        book = input("Enter the name of the book you'd like to borrow >> ")
        if self.library.lend_book(book, self.name):
            self.books.append(book)

    def return_book(self):
        book = input("Enter the name of the book you'd like to return >> ")
        if book in self.books:
            if self.library.return_book(book):
                self.books.remove(book)
                print(f"Thanks for returning {book}, {self.name}")
        else:
            print(f"{self.name}, you haven't borrowed that book, try another...")


def create_lib():
    books = {
        "It Ends With Us": "Free",
        "The Hunger Games": "Free",
        "Cracking the Coding Interview": "Free",
    }
    library = Library(books)

    # Ask user’s name
    name = input("Hi, what's your name? >> ")
    student_example = Student(name, library)

    while True:
        print(f"""
        ========== LIBRARY MENU ===========
        Hello {student_example.name}, please choose an option:
        1. Display Available Books
        2. Borrow a Book
        3. Return a Book
        4. View Your Books
        5. Exit
        """)

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-5.")
            continue

        if choice == 1:
            library.show_avail_books()
        elif choice == 2:
            student_example.request_book()
        elif choice == 3:
            student_example.return_book()
        elif choice == 4:
            student_example.view_borrowed()
        elif choice == 5:
            print(f"Goodbye {student_example.name}, come back soon!")
            break
        else:
            print("Invalid choice, please select from 1 to 5.")


if __name__ == "__main__":
    create_lib()
