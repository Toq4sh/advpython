import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for s in students:
    s["average"] = sum(s["grades"]) / len(s["grades"])

with open("students_updated.json", "w", encoding="utf-8") as f:
    json.dump(students, f, indent=4)
