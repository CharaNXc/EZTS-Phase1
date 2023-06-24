n=int(input("Enter the Range:-"))
l1=[]
l2=[]
i=7
while(i<n):
    l1.append(i)
    i=i+10
s=10
while(s<n):
    l2.append(s)
    s=s+10
print(sum(l1))
print(l1+l2)
