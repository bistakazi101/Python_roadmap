# python getter and setter name 

class employee:
    def setName(self,name):
        self.name=name
        # here it set the value in python 
        
        
    def getName(self):
        # it only prints the value 
        print("My name is sagar",self.name)
        
obj1= employee()
obj1.setName("sagar")
obj1.getName()