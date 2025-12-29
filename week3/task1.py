import math

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def circle_area(r):
    return math.pi * r ** 2

def rectangle_area(a, b):
    return a * b


print("Площадь треугольника со сторонами 3,4,5:", triangle_area(3,4,5))
print("Площадь круга r=5:", circle_area(5))
print("Площадь прямоугольника 4x6:", rectangle_area(4,6))


arr1 = [1, 2, 3, 4]
arr2 = [10, 20, 30]
arr3 = [5, 15, 25, 35, 45]

def sum_and_avg(arr):
    s = sum(arr)
    avg = s / len(arr)
    return s, avg

for i, arr in enumerate([arr1, arr2, arr3], 1):
    s, avg = sum_and_avg(arr)
    print(f"Массив {i}: сумма = {s}, среднее = {avg}")