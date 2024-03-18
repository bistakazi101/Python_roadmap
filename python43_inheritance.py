# all class are derived from built in class object class 




class employee(object):
    bonus= 1000
    def display(self):
        print("employee class")
        
class manager(employee):
    bonus=3000
    def display(self):
        print("Display method of manager class")
        
obj1=manager()
print(obj1.bonus)
obj1.display()