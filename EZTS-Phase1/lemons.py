lemon=int(input("Enter the lemon"))
if(lemon<21):
    print(21-lemon,"We need lemons")
elif(lemon>21):
    print(lemon-21,"We have extra lemons")
else:
    print("Sufficeint lemons entered into the temple")