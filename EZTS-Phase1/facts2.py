fact_list_tuple=(2,5,7,9,10)
for i in fact_list_tuple:
    f=1
    for j in range(1,i+1):
        f=f*j
    print("factorial of %d"%i,f)
        