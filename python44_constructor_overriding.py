# constructor overriding in python 

class employee:
    def __init__(self):
        print("Employee class constructor")
        self.name="sagar"
        
class manager(employee):
    pass
# here child constructor is getting the parent constructor as it is not made
obj1= manager()
print(obj1.__dict__)

# constructor overriding in python
class person:
    def __init__(self):
        print("Person class constructor")
        
class student(person):
    def __init__(self):
        print("Student class constructor")
        self.varname= "sagar"
        
obj1= student()
print(obj1.__dict__ )