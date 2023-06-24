class Balaji:
    def trainer(self):
        rc=int(input("Enter the rows count:"))
        for i in range(1,rc+1):
            for j in range(1,i+1):
                print(" * ",end= ' ')
            print()
        
        print("----------------------------")
       
class D1(Balaji):
    def judge(self):
        lemon=int(input("Enter the lemon:"))
        if(lemon>21):
            print(lemon-21, " We have an extra")
        elif(lemon<21 and lemon>0):
            print(21-lemon," We want to buy")
        elif(lemon==21):
            print("Sufficeint lemons enter into the temple")
        else:
            print("Please enter valid number")
            
        print("----------------------------")

class D2(Balaji):
    def Police(self):
        num=int(input("Enter the number odd or even:"))
        if(num%2==0):
            print("Even")
        else:
            print("Odd")

        print("----------------------------")
        
class D3(Balaji):
    def Lawyer(self):
        f=int(input("Enter the factorial number:"))
        fact=1
        for i in range(1,f+1):
            fact=fact*i
        print("The factorial result is ",fact)
        
        print("----------------------------")
        
        
d1=D1()
d1.judge()
d1.trainer()

d2=D2()
d2.Police()
d2.trainer()

d3=D3()
d3.Lawyer()
d3.trainer()
        

        


        
