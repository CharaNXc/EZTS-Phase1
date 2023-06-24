n=int(input("Enter the Number: "))
f = 1
if n == 1:
    print(n, "is not a prime number")
elif n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            f = 0
            break
    if f==0:
        print(n, "is not a prime number")
    else:
        print(n, "is a prime number")