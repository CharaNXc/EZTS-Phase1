a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))
d=int(input("enter d:"))
if(a>b and a>c and a>d):
    print(a)
elif(b>c and b>d):
    print(b)
elif(c>d):
    print(c)
else:
    print(d)