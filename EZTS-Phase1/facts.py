a=[]
size=int(input("enter the number of list size"))
for i in range(size):
    a.append(int(input("Enter the data")))

for j in a:
    f=1
    for k in range(1,j+1):
        f=f*k
    print(f)