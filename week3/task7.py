import math

#Площадь четырёхугольника с прямым углом между X и Y
X = float(input("X = "))
Y = float(input("Y = "))
Z = float(input("Z = "))
T = float(input("T = "))

# Прямоугольный треугольник XY + прямоугольник или два треугольника
# Площадь = площадь прямоугольника XY + два треугольника по диагонали
area_rect = X * Y
diag = math.sqrt(X**2 + Y**2)
area_tri1 = 0.5 * diag * Z
area_tri2 = 0.5 * diag * T
total_area = area_rect + area_tri1 + area_tri2
print(f"Площадь: {total_area}")

# Перевод в восьмеричную систему с ведущими нулями (10 цифр)
n = int(input("Введите число: "))
oct_str = f"{n:010o}"
print(oct_str)