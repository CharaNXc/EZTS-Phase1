name=input('enter the name')
for i in name:
    if (i=='a'or i=='e'or i=='i'or i=='o'or i=='u'):
        print(chr(ord(i)+1),end=' ')
    else:
        print(chr(ord(i)-1),end=' ')