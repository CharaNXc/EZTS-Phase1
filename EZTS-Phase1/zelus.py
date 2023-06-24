k=int(input("Enter the day of the Month"))
m=int(input("Enter the Number of the Month"))
y=int(input("Enter the Year"))
if(k>31 or k<0 or m<0 or m>12 or y>9999 or y<1000 ):
    print("Invalid Input")
if((m==4 or m==6 or m==11 or m==9) and k>30):
    print("Invalid Input")
elif(k>29 and m==2):
    print("Invalid Input")
elif(k>=29  and (y%4)!=0 and m==2):
    print("The Year is not a Leap year\n The day of the Month is invalid.")
else:
    if(m==1):
        m=13
        y=y-1
    if(m==2):
        m=14
        y=y-1
    d=y%100
    c=y//100
    F = k+ (13*(m+1)//5) +d+ (d//4) + (c//4) +5*c
    result = F%7
    print(result)
    if(result==1):
        print("Sunday")
    elif(result==2):
        print("Monday")
    elif(result==3):
        print("Tuesday")
    elif(result==4):
        print("Wednesday")
    elif(result==5):
        print("Thursday")
    elif(result==6):
        print("Friday")
    elif(result==0):
        print("Saturday")