m1=int(input("Enter tamil marks"))
m2=int(input("Enter english marks"))
m3=int(input("Enter maths marks"))
m4=int(input("Enter science marks"))
m5=int(input("Enter commerce marks"))
total=m1+m2+m3+m4+m5
if(total>450 and total<=500):
    print("A grade")
elif(total>400 and total<=450):
    print("B grade")
elif(total>350 and total<=400):
    print("C grade")
elif(total>300 and total<=350):
    print("D grade")
else:
    print("F grade")
