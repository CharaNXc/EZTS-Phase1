year=int(input("enter the year"))
if(year%4==0 and year%400==0):
    print("yes its leap year")
elif(year%4==0 and year%100!=0):
    print("yes its leap year")
else:
    print("no its not a leap year")