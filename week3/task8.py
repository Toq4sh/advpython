#  Числа, делящиеся на каждую свою цифру
n = int(input("n = "))
result = []
for num in range(1, n+1):
    s = str(num)
    if '0' in s:
        continue
    if all(num % int(d) == 0 for d in s):
        result.append(num)

print(' '.join(map(str, result)) if result else "нет таких")

# Поменять местами первый и последний элемент массива
m = int(input("Длина массива m = "))
A = []
for i in range(m):
    A.append(int(input(f"A[{i}] = ")))

print("Исходный массив:", ' '.join(map(str, A)))

if m >= 2:
    A[0], A[-1] = A[-1], A[0]

print("Изменённый массив:", ' '.join(map(str, A)))