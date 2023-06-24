while(1):
    ttldays = int(input("Enter the Days used:"))
    if (ttldays < 0):
        print("Enter Valid Input")
    else:
        if (ttldays > 84):
            print("Recharge Expired")
        else:
            usedcall = int(input("Enter calls used "))
            if (usedcall < 0):
                print("Enter Valid Input")
            usedsms = int(input("Enter sms used "))
            if (usedsms < 0):
                print("Enter Valid Input")
            useddata = float(input("Enter data used "))
            if (useddata < 0):
                print("Enter Valid Input")
            if(useddata>=2.0):
                print("Data Exhausted")
            else:
                print(2.0 - useddata, "Data left")
            if(usedsms>=100):
                print("SMS are Exhausted Unable make sms's=",(usedsms-100))
            else:
                print(100 - usedsms, "SMS's left")
            if(usedcall>=3000):
                print("Calls capacity is ExceededUnable make ",(usedcall-3000))
            else:
                print(3000-usedcall,"calls are left")
            break