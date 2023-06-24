n=int(input("Enter the Number: "))
def factorial(n):
    return 1 if ( n==0 or n==1) else n * factorial(n - 1);
print("Factorial of",n,"is",
factorial(n))