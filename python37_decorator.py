# decorator function 
# the decorator function modifies the function it decorates 
# it is used to extend the functionalities in the [program ]
def my_decorator(func):
    def inner():
        func()
        print("Print third times")
    return inner


def printer():
    print("Welcome")
    print("Welcome second times")
    
value=my_decorator(printer)
print(value())