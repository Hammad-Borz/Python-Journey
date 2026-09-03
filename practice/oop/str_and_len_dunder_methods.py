class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title} contains {self.pages} pages."

    def __len__(self):
        return self.pages


book = Book("Stay Hard", 700)

print(book)
print(len(book))
