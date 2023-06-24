n = int(input("Enter number of rows to form pyramid: "))
s = 97
for i in range(n):
    for j in range(i+1):
        c = chr(s)
        print(c, end=" ")
        s = s+1
    print()
print('\n')