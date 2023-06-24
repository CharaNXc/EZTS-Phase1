n = int(input("Enter number of rows to form pyramid: "))
for i in range(n):
    for j in range(i+1):
        print(chr(j + 97), end=" ")
    print()
print('\n')