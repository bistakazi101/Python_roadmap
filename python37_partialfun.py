# partial function in python 
# partial function i sused to make default arguments or yo unchange the values of formal arguments

# first we have tto import partial from functool 
from functools import partial

def addition(n1, n2, n3, n4):
    return n1 + n2 + n3 + n4

add = partial(addition, 2, 3)  # First and second default values
print(add(4, 5)) # this is third and fourth arguments 
