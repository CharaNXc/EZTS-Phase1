l1=[10,20,30,40,50]
def biggest():
    print(max(l1))
    
def smallest():
    print(min(l1))
    
def average():
    sum=0
    for i in l1:
        sum=sum+i
    print(sum/len(l1))
        
    
biggest()
smallest()
average()
    
