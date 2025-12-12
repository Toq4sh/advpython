a=int(input("enter num1 "))
b=input("enter operation ")
c=int(input("enter num2 "))
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
