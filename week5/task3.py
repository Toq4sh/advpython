# Базовый класс Person
class Person:
    def __init__(self, name):
        # Защищённое поле (доступно в классе и его наследниках)
        self._name = name

    def get_info(self):
        # Метод возвращает информацию о человеке
        return f"Person: {self._name}"


# Класс Student наследуется от Person
class Student(Person):
    def __init__(self, name, student_id):
        # Вызов конструктора родительского класса
        super().__init__(name)

        # Приватное поле (доступно только внутри класса Student)
        self.__student_id = student_id

    def get_info(self):
        # Переопределённый метод родительского класса
        return f"Student: {self._name}, ID: {self.__student_id}"


# Создаём объект класса Person
p = Person("Juma")

# Создаём объект класса Student
s = Student("Artem", 67)

# Выводим информацию о человеке
print(p.get_info())

# Выводим информацию о студенте
print(s.get_info())

