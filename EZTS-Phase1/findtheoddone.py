'''Python implementation optimized 
'''
n = input().split()
for i in n:
    if n.count(i) == 1:
        print(i)
'''Brute force'''
'''You can also use 2 for loops '''
'''TIme Complexcity o(n) for loop and for nested loops (n^m) m= number of loops inside the loop  '''
'''Time complexity depends on the powers but not constants'''
'''Consider the highest time if have multiple o(n)'''