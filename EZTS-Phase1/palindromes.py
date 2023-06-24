palindrom_list_tuple=['madam','mam','125','check','202']
for i in palindrom_list_tuple:
    a=i[::-1]
    if(a==i):
        print(a," is palindrom")
    else:
        print(a," is not palindrom")