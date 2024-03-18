# destructor in python 

class A:
    def __init__(self):
        print("A class constructor")
    
    
    def __del__(self):
        print("A class destructor")
        
        
obj1 = A()
del obj1 # delete the object