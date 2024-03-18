#in python method overloading i snot possible but we can use the default value of the parameter to achieve the same
# we use the default value of the parameter to achieve the same

class myclass:
    def __init__(self):
        print("This is the constructor of myclass")
        
        
        #in python there is no putre concept of method overloading in python 
        
    def display(self, name=None):
        if name is not None:
            print("This is the display method of myclass with name ", name)
        else:
            print("This is the display method of myclass")
            
            
obj1 = myclass()
obj1.display()