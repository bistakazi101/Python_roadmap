# class variable   

class employee:
    myname="sagar"
    def __init__(self):
        print("The function in the variable ")
        print(employee.myname)
        # FOr modification we only have to use class variable not object refrence 
        # example employee.myname = "Ram" should be used for modificatiuon
        # not obj1.myname="Ram" it is wrong 
    
    @classmethod
    def class_method(cls,instance):
        # here instannce member cannot bbe called directly 
        print("The class myname  is called is and instance name is ",cls.myname,instance)
obj1=employee()
obj2=employee.class_method("Bista")
# we can call by7 object method 
obj1.class_method("Bista")