# built in function overriding in pytrhon  

class employee:
    # There are the magic methods in python 
    def __str__(self):
        return "Employee class"


obj1= employee()
print(obj1)
