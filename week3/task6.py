#  НОД и НОК
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("a = "))
b = int(input("b = "))
g = gcd(a, b)
lcm = a * b // g
print(f"НОД({a}, {b}) = {g}")
print(f"НОК({a}, {b}) = {lcm}")

#Площадь выпуклого четырёхугольника по 4 сторонам и диагонали
# Делим на два треугольника
a = float(input("Сторона a = "))
b = float(input("Сторона b = "))
c = float(input("Сторона c = "))
d = float(input("Сторона d = "))
diag = float(input("Диагональ между a и c = "))

# Площадь двух треугольников: a, b, diag и c, d, diag
p1 = (a + b + diag) / 2
p2 = (c + d + diag) / 2
area = math.sqrt(p1*(p1-a)*(p1-b)*(p1-diag)) + math.sqrt(p2*(p2-c)*(p2-d)*(p2-diag))
print(f"Площадь четырёхугольника: {area:.2f}")