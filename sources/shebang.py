my_supernumber = 333

def add_number(my_supernumber):
    print(my_supernumber)
    my_supernumber += my_supernumber
    return(my_supernumber)
    
my_supernumber = add_number(my_supernumber)
print(my_supernumber)

