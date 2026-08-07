class Animal:
    def sound(self):
        print("Animals make sounds.")
class Dog(Animal):
    def sound(self):
        print("Dogs bark.")
class Cat(Animal):
    def sound(self):
        print("Cats meow.")
class Cow(Animal):
    def sound(self):
        print("Cows moo.")
aniamls = [Dog(), Cat(), Cow()]
for animal in aniamls:
    animal.sound()