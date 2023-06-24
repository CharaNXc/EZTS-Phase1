n=list(map(int,input().split()))
j=0
for i in range(0,len(n)):
    j=j^n[i]
print(j)