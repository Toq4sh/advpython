a, b, c = input("Enter num, operation, num: ").split()
a = int(a)
c = int(c)
if b=="+":
    print(a+c)
elif b=="-":
    print(a-c)
elif b=="*":
    print(a*c)
elif b=="/" and c==0:
    print("division by zero")
elif b=="/":
        print(a/c)
