class Employee:
    company = "Tech Solutions"  # Class variable
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
employee1 = Employee("David", 50000)
employee2 = Employee("Emma", 60000)
print(f"{employee1.name} earns ${employee1.salary} and works at {employee1.company}.")
print(f"{employee2.name} earns ${employee2.salary} and works at {employee2.company}.")
Employee.company = "Innovative Tech"  # Changing the class variable
print(f"{employee1.name} earns ${employee1.salary} and works at {employee1.company}.")
print(f"{employee2.name} earns ${employee2.salary} and works at {employee2.company}.")
