e1,e2,e3,e4,e5,e6=100000,20000,35000,45000,5000,15000
if(e1>e2 and e1>e3 and e1>e4 and e1>e5 and e1>e6):
    print("e1")
elif(e2>e3 and e2>e4 and e2>e5 and e2>e6):
    print(e2)
elif(e3>e4 and e3>e5 and e3>e6):
    print(e3)
elif(e4>e5 and e4>e6):
    print("e4")
elif(e5>e6):
    print(e5)
else:
    print(e6)