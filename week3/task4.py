#Деление дробей A/B на C/D → (A*D)/(B*C), несократимая
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

numer = A * D
denom = B * C
g = gcd(numer, denom)
print(f"{numer//g}/{denom//g}")

#Точки внутри круга (xa)^2 + (yb)^2 = R^2
def is_inside(x, y, xa, yb, R):
    return (x - xa)**2 + (y - yb)**2 < R**2

xa = float(input("xa = "))
yb = float(input("yb = "))
R = float(input("R = "))

points = []
for name in ['P', 'F', 'L']:
    p1 = float(input(f"{name}(x) = "))
    p2 = float(input(f"{name}(y) = "))
    points.append((p1, p2, name))

count = 0
for x, y, name in points:
    if is_inside(x, y, xa, yb, R):
        print(f"Точка {name} внутри круга")
        count += 1
    else:
        print(f"Точка {name} вне круга")

print(f"Всего внутри: {count}")