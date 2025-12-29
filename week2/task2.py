a = input().strip()
b = input().strip()

n = len(a)
m = len(b)

if m > n:
    print(0)
else:
    doubled_b = b + b
    count = 0
    for i in range(n - m + 1):
        substring = a[i:i + m]
        if substring in doubled_b:
            count += 1
    print(count)

