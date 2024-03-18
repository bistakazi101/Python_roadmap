# python [polymorphism 
# this is example of function overloading in python 
# 3 Object type is looked in python type rather  than the value 


class myclass:
    def __init__(self):
        print("This is the constructor of myclass")
        
    def display(self):
        print("This is the display method of myclass")
        
class subclass(myclass):
    def __init__(self):
        print("This is the constructor of subclass")
        
    def display(self):
        print("This is the display method of subclass")
        
        
obj1 = subclass()
