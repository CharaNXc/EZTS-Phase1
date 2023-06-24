email="balaji@gmail.com"
pwd="123456"
email_inp=input("enter mail id")
pwd_inp=input("enter pwd")
if(email==email_inp):
    if(pwd==pwd_inp):
        print("login success")
    else:
        print("pwd incorrect")
else:
    print("email incorrect")
        