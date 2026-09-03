class Car:
    pass
car1 = Car()
car2 = Car()
class Student:
    def study(self):
        print("Studying Python...")
student = Student()
student.study()
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
book1 = Book("Python Programming", "John Doe", 29.99)
book2 = Book("Data Structures", "Jane Smith", 39.99)
print(f"Book 1: {book1.title} by {book1.author}, Price: ${book1.price}")
print(f"Book 2: {book2.title} by {book2.author}, Price: ${book2.price}")
