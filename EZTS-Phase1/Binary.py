k=int(input())
a=13
b=bin(a)
b=b[2:]
b=b[: : -1]
print(b)
if(b[k-1]=='1'):
    print("True")
else:
    print("False")
'''
bin converts int into string in binary
int changes to string 
'''

