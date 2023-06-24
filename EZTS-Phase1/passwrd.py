pwd=str(input("Enter the pwd:"))
for i in range(len(pwd)):
    if(i==0):
        print(int(i)+97,end="")
    elif(i==1):
        print(int(i)+98,end="")
    elif(i==2):
        print(int(i)+99,end="")
    elif(i==3):
        print(int(i)+100,end="")