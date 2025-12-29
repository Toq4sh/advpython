import math
#Гипотенуза двух прямоугольных треугольников
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

a1 = float(input("Треугольник 1: катет a = "))
b1 = float(input("Треугольник 1: катет b = "))
a2 = float(input("Треугольник 2: катет a = "))
b2 = float(input("Треугольник 2: катет b = "))

h1 = hypotenuse(a1, b1)
h2 = hypotenuse(a2, b2)

print(f"Гипотенуза 1: {h1:.2f}")
print(f"Гипотенуза 2: {h2:.2f}")
if h1 > h2:
    print("Гипотенуза первого треугольника больше")
elif h2 > h1:
    print("Гипотенуза второго треугольника больше")
else:
    print("Гипотенузы равны")

s = input("Введите строку: ")
words = s.split()
result = []
for word in words:
    result.append(''.join(sorted(word)))
print(' '.join(result))