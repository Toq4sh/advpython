import math

def triangle_area(a):
    return (math.sqrt(3) / 4) * a ** 2

def hexagon_area(a):
    return 6 * triangle_area(a)

a = float(input("Введите сторону шестиугольника: "))
print("Площадь шестиугольника:", hexagon_area(a))

for i in range(1, 4):
    x = float(input(f"Прямоугольник {i}: сторона 1 = "))
    y = float(input(f"Прямоугольник {i}: сторона 2 = "))
    print(f"Площадь прямоугольника {i}: {x * y}\n")