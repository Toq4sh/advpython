class Person:
    def __init__(self, name):
        self._name = name

    def get_info(self):
        return f"Person: {self._name}"

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.__student_id = student_id

    def get_info(self):
        return f"Student: {self._name}, ID: {self.__student_id}"

p = Person("John")
s = Student("Alice", 101)

print(p.get_info())
print(s.get_info())
