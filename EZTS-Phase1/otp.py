email="balaji@gmail.com"
pwd="123456"
otp=4567
email_inp=input("enter the email")
pwd_inp=input("enter the pwd")
if(email==email_inp):
    if(pwd==pwd_inp):
        otp_inp=int(input("enter the otp"))
        if(otp==otp_inp):
            print("transaction success")
        else:
            print("transaction failed")
    else:
        print("Invalid pwd")
else:
    print("Invalid email")
    