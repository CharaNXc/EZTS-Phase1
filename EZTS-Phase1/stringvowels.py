name='879 balaji miss u all after dasara'
vc=0
sc=0
cc=0
nc=0
for i in range(len(name)):
    if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
        vc=vc+1
    elif(name[i]==' '):
        sc=sc+1
    elif(name[i]>='0' and name[i]<='9'):
        nc=nc+1
    else:
        cc=cc+1
print("vowels count= ",vc)
print("space count= ",sc)
print("consonents count= ",cc)
print("numbers count= ",nc)
        
