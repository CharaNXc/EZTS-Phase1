n = int(input("Enter number of rows to form pyramid: "))
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range((n-i)):
        print(chr(97 + j), end=' ')
    print()