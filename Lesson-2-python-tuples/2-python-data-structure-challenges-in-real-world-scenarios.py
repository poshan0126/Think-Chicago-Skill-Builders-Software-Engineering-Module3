class LibrarySystem:
    def __init__(self, initial_books):
        self.library = initial_books

    def add_book(self, new_book):
        """
        Adds a new book to the library if it's not a duplicate.
        Each book is represented as a tuple (book_name, author).
        """
        if new_book in self.library:
            return "This book already exists in the library."
        else:
            self.library.append(new_book)
            return f"Book '{new_book[0]}' by {new_book[1]} added to the library."

    def display_library(self):
        """
        Displays all books in the library.
        """
        for book in self.library:
            print(f"'{book[0]}' by {book[1]}")

# Existing library data
library_data = [
    ("1984", "George Orwell"),
    ("Brave New World", "Aldous Huxley")
]

# Create an instance of the LibrarySystem with the existing library data
library_system = LibrarySystem(library_data)

# Adding new books and a duplicate to demonstrate functionality
print(library_system.add_book(("The Great Gatsby", "F. Scott Fitzgerald")))
print(library_system.add_book(("1984", "George Orwell")))  # Attempt to add a duplicate

# Displaying the library to show the update
print("\nUpdated Library Data:")
library_system.display_library()
