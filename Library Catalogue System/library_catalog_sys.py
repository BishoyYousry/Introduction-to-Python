class Book:
    def __init__(self, title, author, availability_status):
        self.title = title
        self.author = author
        self.availability_status = availability_status

    def checkout_book(self):
        self.availability_status = False

    def return_book(self):
        self.availability_status = True

    def is_available(self):
        return self.availability_status
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
class Catalog(Book):
    def __init__(self):
        self.books = []

    def add_book(self, title, author, availability_status=True):
        new_book = Book(title, author, availability_status)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} added to the catalog.")

    def display_books(self):
        if not self.books:
            print("No books in the catalog.")
        for book in self.books:
            availability = "Available" if book.is_available() else "Checked out"
            print(f"Title: {book.get_title()}, Author: {book.get_author()}, Status: {availability}")


catalog = Catalog()


catalog.add_book("The Great Gatsby", "F. Scott Fitzgerald")
catalog.add_book("1984", "George Orwell", False)

catalog.display_books()