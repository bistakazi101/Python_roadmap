#polymorphism inn python and object   


class car1:
    def __init__(self):
        print("This is the constructor of car1")
        
    def display(self):
        print("This is the display method of car1")
        
class car2:
    def __init__(self):
        print("This is the constructor of car2")
    
    def display(self):
        print("This is the display method of car2")
        
        
#normal function 

def display(obj):
    obj.display()   
    obj.display()
    
obj1=car1()
obj2=car2()

display(obj1)
display(obj2)   