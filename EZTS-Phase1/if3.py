p1=float(input("Enter p1 height"))
p2=float(input("Enter p2 height"))
p3=float(input("Enter p3 height"))
p4=float(input("Enter p4 height"))
if(p1>p2 and p1>p3 and p1>p4):
    print("p1 taller")
elif(p2>p3 and p2>p4):
    print("p2 taller")
elif(p3>p4):
    print("p3 taller")
else:
    print("p4 taller")
