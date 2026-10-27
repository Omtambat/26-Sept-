class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
        print("Title:", self.title)
        print("Author:", self.author)


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "added to", self.name)

    def show_books(self):
        print("\nBooks in", self.name)
        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                print("-", book.title, "by", book.author)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("You borrowed:", book.title)
                return book

        print("Book is not available in", self.name)
        return None

    def return_book(self, book):
        self.books.append(book)
        print(book.title, "returned to", self.name)


# Creating books
book1 = Book("Science", "Dipak")
book2 = Book("Data Structures", "Om")
book3 = Book("Science", "Dipak")

# Creating two libraries
library1 = Library("Central Library")
library2 = Library("College Library")

# Adding books
library1.add_book(book1)
library1.add_book(book2)

library2.add_book(book3)

# Showing books
library1.show_books()
library2.show_books()

# Borrowing a book
borrowed_book = library1.borrow_book("Python Programming")

# Showing books after borrowing
library1.show_books()

# Returning the book
if borrowed_book:
    library1.return_book(borrowed_book)

# Showing books after returning
library1.show_books()