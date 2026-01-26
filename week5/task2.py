import json  # Модуль для работы с JSON файлами

# Открываем файл students.json и загружаем данные
with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)  # Загружаем список студентов

# Проходим по каждому студенту
for s in students:
    # Считаем средний балл студента
    s["average"] = round(sum(s["grades"]) / len(s["grades"]))

# Сохраняем обновлённые данные в новый файл
with open("students_updated.json", "w", encoding="utf-8") as f:
    # Записываем JSON с отступами для удобства чтения
    json.dump(students, f, indent=4)
