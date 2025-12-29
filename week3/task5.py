# 1. Вычитание дробей A/B - C/D
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

# Приводим к общему знаменателю: (A*D - B*C)/(B*D)
numer = A * D - B * C
denom = B * D

if numer == 0:
    print("0")
else:
    g = gcd(abs(numer), denom)
    if numer < 0:
        print(f"-{abs(numer)//g}/{denom//g}")
    else:
        print(f"{numer//g}/{denom//g}")

# 2. Все делители числа
n = int(input("Введите число: "))
divisors = [i for i in range(1, n+1) if n % i == 0]
print(' '.join(map(str, divisors)))