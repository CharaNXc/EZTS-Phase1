n = int(input("Enter number of rows to form pyramid: "))
############################################
for i in range(n):
    for j in range(i+1):
        print("* ", end="")
    print()
###########################################
print('\n')
for i in range(n):
    for j in range(i,n):
        print("* ", end="")
    print()
print('\n')
###############################################
for i in range(n):
    for s in range(i):
        print(" ", end="")
    for r in range(i, n):
        print("* ", end="")
    print()
print('\n')
#####################################################
s=1
for i in range(n):
    for j in range(i+1):
        print(s, end=" ")
        s = s+1
    s = 1
    print()
print('\n')
################################################################
s = 97
for i in range(n):
    for j in range(i+1):
        c = chr(s)
        print(c, end=" ")
        s = s+1
    print()
print('\n')
###########################################################
################################################################
s = 97
for i in range(n):
    for j in range(i+1):
        c = chr(s)
        print(c, end=" ")
    s = s+1
    print()
print('\n')
#######################################################E
##########################################################
for i in range(n):
    for j in range(i+1):
        print(chr(j + 97), end=" ")
    print()
print('\n')
#######################################################E
##########################################################
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for j in range((n-i)):
        print(chr(97 + j), end=' ')
    print()