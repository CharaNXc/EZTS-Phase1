def judge():
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
        
judge()