days=int(input("enter the days"))
if(days<=84):
   data=float(input("enter the data"))
   msg=int(input("enter the msg"))
   calls=int(input("enter the calls"))
   if(calls<=3000):
       calls=3000-calls
       print(calls,"yet to use")
   else:
        print("calls could not be connected. kindly top up")
    
   if(msg<=100):
       msg=100-msg
       print(msg,"yet to use")
   else:
        print("msg failed to sent")
        
   if(data<=2):
       data=2-data
       print(data,"data yet to use")
   else:
        print("data speed reduced. you exhausted yur data limit")
print(84-days,"your plan will be expired")
else:
    print("plan expired")