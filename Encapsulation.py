class Employee:

    company = "Borz Industries"

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def change(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"Changed: ${amount}. Updated salary: ${self.__salary}")
        else:
            print("Amount not modified.")

    def display(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"Salary: ${self.__salary}")

    def get_salary(self):
        return self.__salary


employee = Employee("John", 70000)

employee.display()

employee.change(700)

employee.display()