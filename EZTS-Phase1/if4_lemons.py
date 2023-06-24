exact_lemon=21
lemon=int(input("Enter the lemons:"))
if(lemon>exact_lemon):
    print("we have extra lemons")
elif(lemon<exact_lemon):
    print("we buy lemons")
else:
    print("Equal lemons")