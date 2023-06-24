n = int(input("Enter number of rows to form pyramid: "))
s=1
for i in range(n):
    for j in range(i+1):
        print(s, end=" ")
        s = s+1
    s = 1
    print()
print('\n')