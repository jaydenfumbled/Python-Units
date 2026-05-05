class Library:
    def __init__(self, book, author):
        self.book = book
        self.author = author
        self.available = True

    def checkout(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Not available")

    def return_book(self):
        self.available = True
        print("Book returned")

    def display(self):
        print(self.book, "-", "Available" if self.available else "Not Available")


b = Library("Python", "Guido")
b.display()
b.checkout()
b.display()
