strng=input('enter a name')
length=len(strng)
revlength=length-1
s1=length-1
s3=length-1
for i in range (0,length):
    print(strng[i],end='')
    for j in range (0,s1-i):
        print(' ',end='')
    print(strng[revlength-i],end='')
    for l in range (0,2*i):
        print(' ',end='')
    print(strng[i],end='')
    for k in range (0,s3-i):
        print(' ',end='')
    print(strng[revlength-i],end='')    
    print('\n')