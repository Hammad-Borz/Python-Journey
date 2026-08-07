class Person:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        print(f"{self.name} is {self.age} years old and obtained a grade of {self.grade}.")
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age, grade)
        self.grade = grade
student = Student("Alice", 20, "A")
student.name