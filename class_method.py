class Employee:
    company = "Borz Industries"
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
    def __init__(self, name, company):
        self.name = name
employee1 = Employee("Starc", "Global Tech")
employee2 = Employee("Smith", "Gloabl Tech")
Employee.change_company("Global Tech")
print(f"{employee1.name} work at {employee1.company}")
print(f"{employee2.name} work at {employee2.company}")