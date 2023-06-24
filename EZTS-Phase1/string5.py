name="balaji srinivasan oops678@gmail.com"
vc=0
sc=0
nc=0
cc=0
spc=0
for i in range(len(name)):
    if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
        vc=vc+1
    elif(name[i]==' '):
        sc=sc+1
    elif(name[i]>='0' and name[i]<='9'):
        nc=nc+1
    elif(!(chr(name[i]>=65) and chr(name[i]<=90)) or (!(chr(name[i]>=97) and chr(name[i]<=122))) or (!(chr(name[i]>=48) and chr(name[i]<=57)))):
        spc=spc+1
    else:
        cc=cc+1
        
        
print("vowels count=",vc)
print("space count=",sc)
print("number count=",nc)
print("consonent count=",cc)
print("special char count=",spc)
