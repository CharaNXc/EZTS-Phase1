n = int(input("Enter number of rows to form pyramid: "))
for i in range(n):
    for s in range(i):
        print(" ", end="")
    for r in range(i, n):
        print("* ", end="")
    print()
print('\n')