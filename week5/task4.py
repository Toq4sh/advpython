# Класс Employee (сотрудник)
class Employee:
    def __init__(self, salary):
        # Приватное поле зарплаты (нельзя обратиться напрямую)
        self.__salary = salary

    def get_salary(self):
        # Метод для получения зарплаты
        return self.__salary

    def get_role(self):
        # Возвращает роль сотрудника
        return "Employee"


# Класс Manager наследуется от Employee
class Manager(Employee):
    def __init__(self, salary, bonus):
        # Вызов конструктора родительского класса
        super().__init__(salary)

        # Бонус менеджера
        self.bonus = bonus

    #def get_role(self):
        # Переопределение метода (полиморфизм)
        #return "Manager"

    def get_bonus(self):
        # Метод для получения бонуса
        return self.bonus


# Функция для вывода списка сотрудников
def print_employees(employees):
    for e in employees:
        # Вызов методов через общий интерфейс
        print(e.get_role(), e.get_salary())


# Создаём обычного сотрудника
emp = Employee(3000)

# Создаём менеджера
mgr = Manager(5000, 1000)

# Передаём разных сотрудников в одну функцию
print_employees([emp, mgr])
