class Animal:
    def sound(self):
        print("Animals make sounds.")

class Dog(Animal):
    def sound(self):
        print("Dogs bark.")
class Cat(Animal):
    def sound(self):
        print("Cats meow.")
dog = Dog()
cat = Cat()
dog.sound()
cat.sound()