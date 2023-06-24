n=int(input("Enter the Number: "))
##############################################
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
##################################################
def factorial(n):
    return 1 if ( n==0 or n==1) else n * factorial(n - 1);
print("Factorial of",n,"is",
factorial(n))
##################################################
s = 0
temp = n
while temp > 0:
   digit = temp % 10
   s += digit ** 3
   temp //= 10
if n == s:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
###################################################

###############################################
n = 44
t = n
rev = 0
while(t>0):
    rem = t%10
    rev = (rev*10)+rem
    t = t//10
if n == rev:
  print('Palindrome')
else:
  print("Not Palindrome")
#########################################################
def fib(k):
   if k <= 1:
       return k
   else:
       return(fib(k-1) + fib(k-2))
if n <= 0:
   print("Plese Valid Number")
else:
   print("Fibonacci sequence upto N terms:")
   for i in range(n):
       print(fib(i))

  

