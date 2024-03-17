# in python we create class by keyword class 
# three types of constriuctor 
# 1. default constructor
# 2. parameterized constructor

class employee:
    def __init__(self, name,salary):
        self.salary=name
        self.name=salary
        print("The employee name is ", self.name)
        print("The employee salary name is ",self.salary)
    def display(self):
        print("The employee name is ", self.name)
        print("The employee salary name is ",self.salary)
        
        
obj1=employee("Ram",1000)
obj2=employee("sagar",45000)
obj1.display()