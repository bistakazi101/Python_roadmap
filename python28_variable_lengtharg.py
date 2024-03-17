# python variable length arguments 

# variable length arguments 
# It is like javascript argument object 
def fun1(*args):
    z= args[0]+args[1]
    return z

value=fun1(10,20,30,40,50,60,70)
print(value)


# keyword variable length arguments 
# The keyword variable length arguments is stored in dictionery
# same like variable length but store iin key value pair 


def fun4(**kargs):
    z= kargs['name']+" "+kargs["classno"]
    return z
    
value = fun4(name="sagar",classno="10")
print(value )