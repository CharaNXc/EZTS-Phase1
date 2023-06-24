n=int(input("Enter the Number: "))
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