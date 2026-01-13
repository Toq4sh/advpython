class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, salary, bonus):
        super().__init__(salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

def print_employees(employees):
    for e in employees:
        print(e.get_role(), e.get_salary())

emp = Employee(3000)
mgr = Manager(5000, 1000)

print_employees([emp, mgr])
