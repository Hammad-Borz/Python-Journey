class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} is a dog")
    def eat(self):
        print("Animals eat food.")
class Dog(Animal):
    def bark(self):
        print("Dogs bark.")
dog = Dog("Buddy")
dog.eat()
dog.bark()