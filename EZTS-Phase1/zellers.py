'''F=k+ [(13*m-1)/5] +D+ [D/4] +[C/4]-2*C

k is  the day of the month.
m is the month number.
D is the last two digits of the year.
C is the first two digits of the year.
'''
k=int(input("Enter the date"))
m=int(input("Enter the month"))
y=int(input("Enter the year"))
c=y//100
d=y%100
if(m==1):
    m=11
f=k+ (13*m-1)//5 +d+ (d//4) +(c//4)-2*c
result=f%7
#print(f)
#print(result)
if(result==0):
    print("Sunday")
elif(result==1):
    print("Monday")
elif(result==2):
    print("Tuesday")
elif(result==3):
    print("Wednesday")
elif(result==4):
    print("Thursday")
elif(result==5):
    print("Friday")
else:
    print("Saturday")