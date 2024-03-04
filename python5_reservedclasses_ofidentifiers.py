# python reserved class of identifiers
# not imported from by module 
# Example
# Module: my_module.py
# Contents: _variable = 42

#1) This won't import _variable when using "from my_module import *"
# __all__ = ['some_function']

# _variable = 42

# def some_function():
#     print("Hello from some_function")
# 2)Soft Keyword in Case Pattern:
# Example
def check_value(x):
    match x:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case _:
            print("Value is something else")

# Using the function with different values
check_value(1)
check_value(3)

# 3)interactive interpretar usage
# ininteractive module the last value is stored in _(underscore) 
# the value is stored in built in models
x=10
y=20
_=x+y
print(_) # or _ you have to work with python interpretaor

#4regular identifier
_="i am a regular identifier"
print(_)

#4)- System-Defined Names ("Dunder" Names):
# Example - Dunder name usage
class MyClass:
    def __init__(self):
        self.__my_private_variable = 42

    def get_private_variable(self):
        return self.__my_private_variable

obj = MyClass()
print(obj.get_private_variable())  # Prints 42


