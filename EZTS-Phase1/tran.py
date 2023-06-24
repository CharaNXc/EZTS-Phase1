

'''while(mon<0 ):
    tx=3'''
mon=25000
tx=3
while(tx!=0):
    a=int(input('entr amnt'))
    mon=mon-a
    tx=tx-1
    if(mon<0):
        print('tx money exceeded')
        tx=0
    if(tx==0):
        print('tx limit exceeded')

    
     