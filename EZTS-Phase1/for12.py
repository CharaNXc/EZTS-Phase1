s=int(input("Enter the starting value:"))
e=int(input("Enter the end point value:"))
t=0
for i in range(s,e):
    if(i%4==0):
        t=t+1
        print(i,end=" ")
#name=input("name")
print("total numer count=",t)