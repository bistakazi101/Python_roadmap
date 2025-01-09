def greet():
    """ greet the person """
    print("hello how are you")

greet()

#parsing the information to the function
def greet(name):
    """greet the person"""
    print(f"hello  {name} ")
    
greet("sagar")

# returning the function in python 
def greet():
    """returning the function in python"""
    return "hello returning the word"

name= greet()
print(name)


# function with multiple parameters
def sum(a,b):
    """sum of two numbers """
    return a+b

sum1= sum(10,20)
print(sum1)