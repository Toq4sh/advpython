a=int(input("ticket num: "))
c=str(a)
b=list(c)
d=int(int(b[0])+int(b[1])+int(b[2]))
e=int(int(b[3])+int(b[4])+int(b[5]))
if d==e:
    print("yes")
else:
    print("no")