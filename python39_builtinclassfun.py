# built in class function 
# the python has many types of the builyt in class function 
# getattr, setattr, delattr,hasattr 

class employee:
    def __init__(self, name,salary):
        self.name=name
        self.salary=salary
        print("The employee name is ", self.name)
        print("The employee salary name is ",self.salary)
    def display(self):
        print("The employee name is ", self.name)
        print("The employee salary name is ",self.salary)
        
        
obj1=employee("Ram",1000)
obj2=employee("sagar",45000)


# These are built in class methods 
print(getattr(obj1,"name"))
print(hasattr(obj1,"name"))
print(setattr(obj1,"name","sagar"))
print(obj1.__dict__)
print(delattr(obj1,"name"))




# These are built in variables in class in python 
print(employee.__dict__)
print(employee.__doc__)
print(employee.__name__)
print(employee.__class__)


# isinstanceof object 

print(isinstance(obj1,employee))