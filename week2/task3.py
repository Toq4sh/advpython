e=input().strip()
a, op, b, _, c = e
if a == 'x':
    A = None
else:
    A = int(a)
if b == 'x':
    B = None
else:
    B = int(b)
if c == 'x':
    C = None
else:
    C = int(c)
if op == "+":
    if A == None:
        print (C-B)
    elif B == None:
        print (C-A)
    else: print (A+B)
elif op == "-":
    if A == None:
        print(B+C)
    elif B == None:
        print(A-C)