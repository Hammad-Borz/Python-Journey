class Student:
    school = "Apex College"  # Class variable
    def __init__(self, name, age,):
        self.name = name
        self.age = age
student1 = Student("John", 20,)
student2 = Student("Alice", 22,)
print(f"{student1.name} is {student1.age} years old and studies at {student1.school}.")
print(f"{student2.name} is {student2.age} years old and studies at {student2.school}.")
